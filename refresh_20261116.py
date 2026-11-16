"""Replace the FY2026 cumulative snapshot while preserving earlier typed records."""
from pathlib import Path
import argparse,csv,hashlib,json,os,sys,time
import duckdb
import build_database as b
ROOT=Path(__file__).resolve().parent
WORK=ROOT.parent
OUT=ROOT/'artifacts-2026-11-16-v2'
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def fingerprint(con,table,where):
    # Order-independent multiplicity-preserving comparison within this engine.
    return [str(x) for x in con.execute(f'SELECT count(*),sum(hash(COLUMNS(* EXCLUDE(is_latest)))) FROM {table} WHERE {where}').fetchone()]
def main(BASE):
    os.chdir(ROOT);OUT.mkdir(exist_ok=False)
    pin=json.loads((ROOT/'baseline-2026-11-16.json').read_text())
    remote={'repo':pin['repo'],'head':pin['revision']}
    entry={'size':pin['bytes'],'lfs':{'sha256':pin['sha256']}}
    assert BASE.stat().st_size==entry['size'] and sha(BASE)==entry['lfs']['sha256'],'Local baseline must match public immutable bytes'
    lock=json.loads((ROOT/'releases/source-lock-2026-11-16.json').read_text())
    for s in lock['sources']:
        p=ROOT/'data/raw-2026-11-16'/s['file'];assert p.stat().st_size==s['bytes'] and sha(p)==s['sha256']
    con=duckdb.connect(str(OUT/'dol_visas.partial.duckdb'),config={'threads':'1','memory_limit':'1GiB','max_temp_directory_size':'2GiB'})
    con.execute('INSTALL excel');con.execute('LOAD excel')
    con.execute(f"ATTACH '{BASE}' AS baseline (READ_ONLY)")
    incoming={};before={};counts={}
    for program in ['lca','perm']:
        cw=b.load_crosswalk(str(ROOT/('crosswalk_'+program+'.csv')))
        paths=sorted((ROOT/'data/raw-2026-11-16').glob(program.upper()+'_Disclosure_Data_FY2026_Q*.xlsx'))
        assert len(paths)==(4 if program=='lca' else 1)
        incoming[program]=b.build_table(con,program,paths,cw)
        print('Source date ranges',con.execute(f'SELECT source_file,count(*),min(decision_date),max(decision_date) FROM {program} GROUP BY 1').fetchall(),flush=True)
        print('incoming',program,incoming[program],flush=True)
    b.normalize_values(con)
    for program in ['lca','perm']:
        before[program]=fingerprint(con,'baseline.'+program,'fiscal_year<2026')
        assert con.execute(f'DESCRIBE {program}').fetchall()==con.execute(f'DESCRIBE baseline.{program}').fetchall(),'Schema changed'
        con.execute(f'INSERT INTO {program} SELECT * FROM baseline.{program} WHERE fiscal_year<2026')
        # Refresh the existing definition over the combined history.
        con.execute(f'''CREATE OR REPLACE TABLE {program} AS SELECT * EXCLUDE(is_latest),
            row_number() OVER(PARTITION BY case_number ORDER BY decision_date DESC NULLS LAST,
            received_date DESC NULLS LAST,fiscal_year DESC,quarter DESC NULLS LAST)=1 AS is_latest FROM {program}''')
        assert fingerprint(con,program,'fiscal_year<2026')==before[program],'Historical typed values changed'
        counts[program]=con.execute(f'SELECT count(*) FROM {program}').fetchone()[0]
        expected_quarters={'Q1','Q2','Q3','Q4'} if program=='lca' else {'Q4'}
        assert {r[0] for r in con.execute(f'SELECT DISTINCT quarter FROM {program} WHERE fiscal_year=2026').fetchall()}==expected_quarters
        print('combined',program,counts[program],flush=True)
    b.build_metadata(con,counts)
    b.build_columns_table(con,join_hints=b.JOIN_HINTS)
    b.export_dictionary(con,OUT/'DICTIONARY.md',title='dol-visas Data Dictionary',intro=b.DICTIONARY_INTRO,style='backtick',tables=('lca','perm'))
    assert b.run_validation(con,OUT/'dol_visas.partial.duckdb')==0
    con.execute('CHECKPOINT');con.close()
    db=OUT/'dol_visas.duckdb';(OUT/'dol_visas.partial.duckdb').rename(db)
    record={'source_snapshot':'2026-11-16','source_release':'FY2026 Q4','sources':lock['sources'],'baseline':{'repo':remote['repo'],'revision':remote['head'],'sha256':entry['lfs']['sha256']},'tables':counts,'incoming_rows':incoming,'historical_column_fingerprints':before,'artifact':{'bytes':db.stat().st_size,'sha256':sha(db)},'validation':'passed','scope':'FY2015-2025 unchanged except recomputed is_latest; FY2026 LCA uses all four official quarter files; PERM uses cumulative Q4; source column crosswalk retained'}
    (OUT/'sources-2026-11-16.json').write_text(json.dumps(record,indent=2));print(json.dumps(record),flush=True)
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',required=True,type=Path,help='Local copy of the immutable baseline identified in baseline-2026-11-16.json')
    main(parser.parse_args().baseline.resolve())

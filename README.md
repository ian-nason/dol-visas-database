# DOL Visas Database (H-1B LCA + PERM)

Employer applications disclosed by the Department of Labor (DOL) Office of Foreign Labor Certification for H-1B, H-1B1 and E-3 Labor Condition Applications (LCAs) and permanent labor certification (PERM). The snapshot covers fiscal year (FY) 2015 through FY2026 Q3, with determinations through June 30, 2026. Use it to study reported employers, jobs, worksites, offered wages and case statuses. Records describe applications and disclosure appearances, not issued visas or unique workers. Use `is_latest` when selecting the most recent disclosed appearance of a case, and keep program, wage unit and partial-year coverage explicit.

<a id="quick-start"></a>

## Start querying

Preview up to five latest-disclosed Labor Condition Application records for fiscal year 2025, showing the case number, employer and recorded case status. `is_latest` keeps the most recently disclosed appearance of each application. These H-1B, H-1B1 and E-3 program applications are not issued visas.

Choose R or Python. Install the datapond package once: use `install.packages("datapond")` in R, or run `python -m pip install datapond` in a terminal.

### R

```r
library(datapond)
con <- dp_connect("dol-visas")
tryCatch({
  DBI::dbExecute(con, "SET threads=1")
  DBI::dbExecute(con, "SET memory_limit='128MiB'")
  DBI::dbExecute(con, "SET max_temp_directory_size='0B'")
  print(DBI::dbGetQuery(con, "SELECT case_number,employer_name,case_status FROM lca WHERE fiscal_year=2025 AND is_latest LIMIT 5"))
}, finally = dp_disconnect(con))
```

### Python

```python
import datapond
con = datapond.connect('dol-visas')
try:
    con.execute("SET threads=1")
    con.execute("SET memory_limit='128MiB'")
    con.execute("SET max_temp_directory_size='0B'")
    print(con.execute("""SELECT case_number,employer_name,case_status FROM lca WHERE fiscal_year=2025 AND is_latest LIMIT 5""").fetchall())
finally:
    con.close()
```

Queries run on your computer and read the byte ranges they need. A small result can still require a large scan. These examples limit DuckDB to one thread and a 128 MiB buffer pool with disk spill disabled; that is not a limit on the entire R or Python process. Larger analyses may need more memory or a local download with enough disk space.

<a id="additional-dataset-notes"></a>

<a id="tables"></a>

<a id="coverage-fields-and-sources"></a>

## Tables and coverage

**About 8.8 million disclosure rows across two tables.**

| Table | Rows | Description |
|-------|------|-------------|
| `lca` | 7,479,697 | One row per LCA per disclosure file, FY2015+ (H-1B, H-1B1, E-3) |
| `perm` | 1,332,942 | One row per PERM application per disclosure file, FY2015+ |

See the [data dictionary](https://github.com/ian-nason/dol-visas-database/blob/main/DICTIONARY.md) for column definitions.

<a id="researcher-caveats--read-before-publishing-numbers"></a>

Every row carries `fiscal_year`, `quarter` (FY2020+ LCA files only), and
`source_file`.

## Interpreting applications and wages

1. **One row per disclosure appearance, not per case.** A case that is
   certified in one file and withdrawn/amended in a later one appears
   multiple times (~7-8% of LCA rows). Filter `WHERE is_latest` for
   one-row-per-case analyses; keep all rows to study case lifecycles.
   210k+ LCA case numbers legitimately span two fiscal years.
2. **An LCA is not a visa.** LCAs are employer applications (one LCA can
   cover multiple worker positions — see `total_worker_positions`) and
   precede the USCIS H-1B petition; certified LCA counts far exceed actual
   H-1B approvals. PERM certifications likewise precede I-140 petitions.
3. **Column availability varies by era.** The files changed layout in
   FY2017, FY2019, FY2020 (LCA) and FY2020, FY2024 (PERM). The per-era
   source-to-canonical mappings live in `crosswalk_lca.csv` /
   `crosswalk_perm.csv`; per-column null rates are in the `_columns` table.
   Notably: **the FY2024+ PERM form dropped `country_of_citizenship`,
   `class_of_admission`, and foreign-worker education fields entirely** —
   those are NULL for new-form rows by source design.
4. **FY2019 LCA multi-worksite groups.** The FY2019 file carried up to 10
   worksite/wage column groups per application; this database keeps the
   primary worksite (documented in the crosswalk) and drops groups 2-10.
   All other years publish a single (primary) worksite.
5. **Wages need unit filtering.** `wage_rate_of_pay_from` mixes hourly,
   weekly, monthly, and annual amounts — always filter or normalize by
   `wage_unit_of_pay`. FY2015-16 published a single wage value; that value appears in both the from/to fields.
6. **FY2026 is partial** (cumulative through Q3, June 30, 2026;
   see `quarter` and `source_file`). Pre-FY2020 LCA
   files are end-of-year snapshots; FY2020+ are per-quarter files.
7. **Stored categorical values use consistent casing and punctuation** ( `case_status` is always UPPER like `CERTIFIED-WITHDRAWN`;
   `pw_wage_level` is `I`-`IV`; Y/N flags are `Y`/`N`).
8. **Not included in v1:** H-2A, H-2B, CW-1, prevailing wage determination
   files, pre-FY2015 files (formats differ substantially; candidates for a
   future version), and the FY2026+ LCA worksites addendum.

<a id="advanced-access-quick-start-remote-query"></a>

## More example queries

These direct DuckDB examples count certified LCA records by employer, compare annual offered wages by occupation, and calculate the share of latest PERM records whose status begins with CERTIFIED. Standard Occupational Classification (SOC) identifies occupations. The wage result is the median offered annual wage in U.S. dollars, not an hourly rate; the PERM percentage counts applications, not visas or workers.

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/dol-visas-database/resolve/main/dol_visas.duckdb' AS visas (READ_ONLY);

-- Top H-1B/H-1B1/E-3 employers by certified LCA records, FY2025
SELECT employer_name, COUNT(*) AS certified
FROM visas.lca
WHERE fiscal_year = 2025 AND case_status = 'CERTIFIED' AND is_latest
GROUP BY 1 ORDER BY 2 DESC LIMIT 10;

-- Median offered wage by SOC title, FY2025 (annual salaries only)
SELECT soc_title, MEDIAN(wage_rate_of_pay_from) AS median_wage, COUNT(*) AS n
FROM visas.lca
WHERE fiscal_year = 2025 AND wage_unit_of_pay = 'Year' AND is_latest
GROUP BY 1 HAVING n >= 500 ORDER BY median_wage DESC LIMIT 20;

-- Share of latest disclosed PERM records with CERTIFIED or CERTIFIED-WITHDRAWN status
-- Denominator: all latest disclosed PERM records in each fiscal year; not visas issued
SELECT fiscal_year,
       ROUND(100.0 * COUNT(*) FILTER (WHERE case_status LIKE 'CERTIFIED%')
             / COUNT(*), 1) AS pct_certified
FROM visas.perm WHERE is_latest
GROUP BY 1 ORDER BY 1;
```

## Other ways to connect

If you only need a connection for your own queries, the [datapond](https://pypi.org/project/datapond/) package also supports this shorter setup. The first-query examples above include resource limits and connection cleanup.

```python
import datapond
visas = datapond.connect('dol-visas')
```

<a id="provenance"></a>

## Sources and maintenance

### Sources and provenance

Source: [DOL Office of Foreign Labor Certification disclosure files](https://www.dol.gov/agencies/eta/foreign-labor/performance). License: Public domain.

Source: [OFLC Performance Data](https://www.dol.gov/agencies/eta/foreign-labor/performance)
(file inventory pinned in `sources.yaml`).

### Build from Source

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
# Download (cached in data/raw/), build, validate
uv run --with duckdb --with requests --with pyyaml python build_database.py

# Publish to Hugging Face
uv run --with duckdb --with pandas --with huggingface_hub python publish_to_hf.py --token hf_YOUR_TOKEN
```

To refresh after a new quarterly release: add the new file(s) to
`sources.yaml`, re-run `build_crosswalk.py` if headers changed (it fails
loudly on unmapped columns), then rebuild and republish.

### License

Build code: MIT. Underlying data: public domain (U.S. government records).

---
license: other
license_name: public-domain
license_link: https://www.dol.gov/agencies/eta/foreign-labor/performance
task_categories:
  - tabular-classification
  - tabular-regression
tags:
  - immigration
  - h1b
  - perm
  - labor
  - visas
  - dol
pretty_name: DOL H-1B LCA & PERM Labor Certification Database
size_categories:
  - 1M<n<10M
---

# DOL Visas Database (H-1B LCA + PERM)

Employer applications disclosed by the Department of Labor (DOL) Office of Foreign Labor Certification for H-1B, H-1B1 and E-3 Labor Condition Applications (LCAs) and permanent labor certification (PERM). The snapshot covers fiscal year (FY) 2015 through FY2026 Q4, with determinations through September 30, 2026. Use it to study reported employers, jobs, worksites, offered wages and case statuses. Records describe applications and disclosure appearances, not issued visas or unique workers. Use `is_latest` when selecting the most recent disclosed appearance of a case, and keep program, wage unit and fiscal-year coverage explicit.

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

<a id="coverage-fields-and-sources"></a>

## Tables and coverage

**8,987,531 disclosure rows across two tables.**

| Table | Description | Row Count | Column Count | Date Range |
|---|---|---|---|---|
| `lca` | H-1B/H-1B1/E-3 Labor Condition Applications, one row per application per disclosure file, FY2015-FY2026 Q4 | 7,596,060 | 110 | FY2015 to FY2026 |
| `perm` | PERM permanent labor certification applications, one row per application per disclosure file, FY2015-FY2026 Q4 | 1,391,471 | 73 | FY2015 to FY2026 |

See the [data dictionary](https://github.com/ian-nason/dol-visas-database/blob/main/DICTIONARY.md) for column definitions.

## Interpreting applications and wages

Each case can appear in multiple disclosure files. Filter `is_latest` for its most recent appearance within a program, or retain all appearances to study its history. Fiscal year 2026 now covers all four quarters. Applications are not visas issued or unique workers.

Wage fields mix hourly, weekly, monthly and annual amounts; filter or normalize `wage_unit_of_pay` before comparing wages. The FY2024+ PERM form drops citizenship, admission class and foreign-worker education fields. FY2019 LCA secondary worksite groups 2–10 are not retained. H-2A, H-2B, CW-1 and prevailing-wage files are outside this dataset.

Date columns in the July 2026 release were empty because of a conversion problem; the September refresh corrected that problem. Use the refreshed release for date analyses. Full release details are below.

<a id="advanced-access-query-it-remotely"></a>

## More example queries

Count the latest disclosed certified LCA records by employer for fiscal year 2025. This example opens a direct DuckDB connection; the R and Python package examples above are alternatives.

```sql
INSTALL httpfs; LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/dol-visas-database/resolve/main/dol_visas.duckdb' AS visas (READ_ONLY);

SELECT employer_name, COUNT(*) AS certified_lcas
FROM visas.lca
WHERE fiscal_year = 2025 AND case_status = 'CERTIFIED' AND is_latest
GROUP BY 1 ORDER BY 2 DESC LIMIT 10;
```

## Sources and maintenance

### Sources and build documentation

Source: [DOL Office of Foreign Labor Certification disclosure files](https://www.dol.gov/agencies/eta/foreign-labor/performance). License: Public domain.

Build pipeline, per-era column crosswalks, and full documentation:
https://github.com/ian-nason/dol-visas-database

### Changelog

#### 2026-09-14 — Data refresh (FY2026 Q3)

- Rebuilt from the OFLC FY2026 Q3 disclosure files (determinations through
  2026-06-30, posted August 2026), replacing the cumulative Q2 files.
  Total rows 8,533,076 → 8,812,639: `lca` 7,479,697 (FY2026 to date
  437,496, was 259,200), `perm` 1,332,942 (FY2026 to date 112,550).
- **Fix: date columns were 100% NULL in the July release.** DuckDB's
  `read_xlsx(all_varchar=true)` returns Excel date serials as text (`45931`),
  which the DATE cast silently rejected, so `decision_date`, `received_date`,
  `original_cert_date` and `orig_file_date` were empty in both tables (and
  `begin_date`/`end_date` partly). The cast now converts serials, and
  validation fails if `decision_date`/`received_date` are not populated.
- DOL made no layout changes: the Q3 LCA (98 columns) and PERM (137 columns)
  headers are identical to Q2, so the crosswalks are unchanged.
- Builder now fails loudly if a source file carries a column that is neither
  in the crosswalk nor in the new `known_unmapped.json` (the 464 columns we
  intentionally drop, e.g. FY2019 secondary-worksite groups 2-10); previously
  unknown columns were dropped silently. Validation now also asserts every
  fiscal year FY2015-FY2026 is present and `is_latest` is unique per case.
- DuckDB memory limit lowered to 5 GB (was 8 GB) with 4 threads so the build
  fits the 10 GB build VM; `publish_to_hf.py --card-only` re-uploads the
  dataset card without re-uploading the file.

#### 2026-07-07 — Initial release

- `lca`: H-1B/H-1B1/E-3 Labor Condition Applications, FY2015 through
  FY2026-to-date (~7.25M rows, 106 harmonized columns from 4 source-layout
  eras).
- `perm`: PERM labor certification applications, FY2015 through
  FY2026-to-date (~1.28M rows, 69 curated analytical columns from 3 form
  eras; remaining source columns documented as drops in the crosswalk).
- All disclosure rows kept; `is_latest` flags the most recent appearance of
  each case number per program.
- Categorical domains normalized across eras (case_status casing, wage
  levels, Y/N flags, literal 'NULL' strings).
- Known upstream limits: FY2024+ PERM form drops citizenship/admission-class
  and foreign-worker education fields; FY2019 LCA secondary worksite groups
  (2-10) not retained; H-2A/H-2B/CW-1/prevailing-wage files out of scope.


### R with DBI and duckdb

Install the dependencies once with `install.packages(c("DBI", "duckdb"))`.

```r
library(DBI)
con <- dbConnect(duckdb::duckdb())
dbExecute(con, "INSTALL httpfs")
dbExecute(con, "LOAD httpfs")
dbExecute(con, "ATTACH 'https://huggingface.co/datasets/Nason/dol-visas-database/resolve/main/dol_visas.duckdb' AS visas (READ_ONLY)")
dbGetQuery(con, "SELECT fiscal_year, employer_name, case_status FROM visas.lca LIMIT 5")
dbDisconnect(con, shutdown = TRUE)
```

DuckDB uses HTTP range requests; queries run on your machine and may need substantial memory or download data. A `LIMIT` does not guarantee a small scan.


Or with the datapond packages: `pip install datapond` / `pak::pak("datapond-db/datapond-r")`.

Build pipeline, per-era column crosswalks, and full documentation:
https://github.com/ian-nason/dol-visas-database


# Changelog


### November 16, 2026 — FY2026 Q4 refresh

The verified release contains **8,987,531 stored rows**: 7,596,060 LCA and 1,391,471 PERM. FY2026 contributes 553,859 LCA rows (82,477 Q1; 121,912 Q2; 230,263 Q3; 119,207 Q4) and 171,079 PERM rows. Decision dates cover October 1, 2025 through September 30, 2026. The LCA quarter files are disjoint; the PERM Q4 file is cumulative.

The FY2015–FY2025 typed values were retained and checked by counts and per-column multiplicity-preserving hash aggregates; `is_latest` was recomputed across the combined history. The existing crosswalk and 110/73-column schemas are retained, including the documented omission of 100 non-crosswalk PERM source fields. All builder validation checks passed. The artifact is 3,929,288,704 bytes, SHA-256 `ccab6347bfa183e013906ce56fc384afe9052d020b514aa31f15ab5ca870d723`.

The exact source hashes, baseline identity, incoming counts and validation record are in [sources-2026-11-16.json](https://huggingface.co/datasets/Nason/dol-visas-database/resolve/main/sources-2026-11-16.json). The GitHub repository includes the immutable baseline pin and the release-specific rebuild scripts. To replay in a fresh checkout with the pinned dependencies:

```sh
python download_20261116.py
# Download the immutable URL in baseline-2026-11-16.json to baseline.duckdb.
python refresh_20261116.py --baseline baseline.duckdb
```

The rebuild verifies the complete baseline hash and each source hash before use and refuses to overwrite its release output directory. It uses one DuckDB thread, a 1 GiB engine memory limit and at most 2 GiB spill. Disk space is additionally required for the baseline, current source files and output. Engine limits do not cap total process memory. General full-history builds remain available through `build_database.py`; that path may ingest later mutable publisher revisions and does not promise identical release bytes.

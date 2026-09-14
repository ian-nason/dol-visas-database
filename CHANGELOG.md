# Changelog

## 2026-09-14 — Data refresh (FY2026 Q3)

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

## 2026-07-07 — Initial release

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

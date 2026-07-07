# Changelog

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

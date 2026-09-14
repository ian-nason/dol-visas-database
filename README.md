# DOL Visas Database (H-1B LCA + PERM)

A clean, queryable DuckDB database of every **H-1B/H-1B1/E-3 Labor Condition
Application** and **PERM permanent labor certification** application disclosed
by the DOL Office of Foreign Labor Certification, FY2015 through the current
fiscal year.

**~8.8M rows** across 2 tables: `lca` (~7.48M) and `perm` (~1.33M).

## Quick Start (Remote Query)

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/dol-visas-database/resolve/main/dol_visas.duckdb' AS visas (READ_ONLY);

-- Top H-1B employers by certified LCAs, FY2025
SELECT employer_name, COUNT(*) AS certified
FROM visas.lca
WHERE fiscal_year = 2025 AND case_status = 'CERTIFIED' AND is_latest
GROUP BY 1 ORDER BY 2 DESC LIMIT 10;

-- Median offered wage by SOC title, FY2025 (annual salaries only)
SELECT soc_title, MEDIAN(wage_rate_of_pay_from) AS median_wage, COUNT(*) AS n
FROM visas.lca
WHERE fiscal_year = 2025 AND wage_unit_of_pay = 'Year' AND is_latest
GROUP BY 1 HAVING n >= 500 ORDER BY median_wage DESC LIMIT 20;

-- PERM approval rate by fiscal year
SELECT fiscal_year,
       ROUND(100.0 * COUNT(*) FILTER (WHERE case_status LIKE 'CERTIFIED%')
             / COUNT(*), 1) AS pct_certified
FROM visas.perm WHERE is_latest
GROUP BY 1 ORDER BY 1;
```

Or with the [datapond](https://pypi.org/project/datapond/) package:

```python
import datapond
visas = datapond.connect('dol-visas')
```

## Tables

| Table | Rows | Description |
|-------|------|-------------|
| `lca` | ~7.25M | One row per LCA per disclosure file, FY2015+ (H-1B, H-1B1, E-3) |
| `perm` | ~1.28M | One row per PERM application per disclosure file, FY2015+ |

## Researcher caveats — read before publishing numbers

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
   `wage_unit_of_pay`. FY2015-16 published a single wage value that is
   split into from/to at build time.
6. **The current fiscal year is partial** (cumulative through the latest
   quarterly release; see `quarter` and `source_file`). Pre-FY2020 LCA
   files are end-of-year snapshots; FY2020+ are per-quarter files.
7. **Categorical values are normalized at build time** (casing/punctuation
   unified: `case_status` is always UPPER like `CERTIFIED-WITHDRAWN`;
   `pw_wage_level` is `I`-`IV`; Y/N flags are `Y`/`N`).
8. **Not included in v1:** H-2A, H-2B, CW-1, prevailing wage determination
   files, pre-FY2015 files (formats differ substantially; candidates for a
   future version), and the FY2026+ LCA worksites addendum.

## Provenance

Every row carries `fiscal_year`, `quarter` (FY2020+ LCA files only), and
`source_file`. Source: [OFLC Performance Data](https://www.dol.gov/agencies/eta/foreign-labor/performance)
(file inventory pinned in `sources.yaml`).

## Build from Source

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

## License

Build code: MIT. Underlying data: public domain (U.S. government records).

"""Publish dol_visas.duckdb to the Nason/dol-visas-database HF dataset."""
import argparse
import sys
from pathlib import Path

import duckdb
from huggingface_hub import HfApi, create_repo


def generate_dataset_card(db_path: str) -> str:
    con = duckdb.connect(db_path, read_only=True)
    metadata = con.sql(
        "SELECT table_name, description, row_count, column_count, "
        "data_sources, date_range FROM _metadata ORDER BY row_count DESC"
    ).fetchdf()
    con.close()

    table_rows = "\n".join(
        f"| `{r['table_name']}` | {r['description']} | {r['row_count']:,} "
        f"| {r['column_count']} | {r['date_range']} |"
        for _, r in metadata.iterrows()
    )
    total_rows = int(metadata["row_count"].sum())

    return f"""---
license: mit
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

Every H-1B/H-1B1/E-3 Labor Condition Application and PERM permanent labor
certification application disclosed by the DOL Office of Foreign Labor
Certification, FY2015 to present, as a single queryable DuckDB database.
**{total_rows:,} rows.**

| Table | Description | Rows | Cols | Coverage |
|-------|-------------|------|------|----------|
{table_rows}

## Query it remotely

```sql
INSTALL httpfs; LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/dol-visas-database/resolve/main/dol_visas.duckdb'
    AS visas (READ_ONLY);

SELECT employer_name, COUNT(*) AS certified_lcas
FROM visas.lca
WHERE fiscal_year = 2025 AND case_status = 'CERTIFIED' AND is_latest
GROUP BY 1 ORDER BY 2 DESC LIMIT 10;
```

Or with the datapond package: `pip install datapond`, then
`datapond.connect('dol-visas')`.

Build pipeline, per-era column crosswalks, and full documentation:
https://github.com/ian-nason/dol-visas-database
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=Path("dol_visas.duckdb"))
    parser.add_argument("--repo", default="Nason/dol-visas-database")
    parser.add_argument("--token", help="HF token (or set HF_TOKEN env var)")
    args = parser.parse_args()

    if not args.db.exists():
        print(f"Error: {args.db} not found")
        sys.exit(1)

    api = HfApi(token=args.token)
    create_repo(args.repo, repo_type="dataset", exist_ok=True, token=args.token)

    card = generate_dataset_card(str(args.db))
    changelog = Path(__file__).parent / "CHANGELOG.md"
    if changelog.exists():
        card += "\n\n" + changelog.read_text()

    api.upload_file(path_or_fileobj=card.encode(), path_in_repo="README.md",
                    repo_id=args.repo, repo_type="dataset")
    size_gb = args.db.stat().st_size / (1024 ** 3)
    print(f"Uploading {args.db} ({size_gb:.1f} GB)...")
    api.upload_file(path_or_fileobj=str(args.db), path_in_repo="dol_visas.duckdb",
                    repo_id=args.repo, repo_type="dataset")
    print(f"\nUploaded to https://huggingface.co/datasets/{args.repo}")
    print("\nUsers can now query remotely:\n"
          f"  ATTACH 'https://huggingface.co/datasets/{args.repo}/resolve/main/dol_visas.duckdb'"
          " AS visas (READ_ONLY);")


if __name__ == "__main__":
    main()

"""Publish dol_visas.duckdb to Hugging Face.

The card text lives in card.yaml; the upload/verify logic in datapond-build.

    uv run python publish_to_hf.py --token hf_xxx [--card-only] [--verify]
"""
import sys

from datapond_build.publish import main

if __name__ == "__main__":
    sys.exit(main(["--db", "dol_visas.duckdb"] + sys.argv[1:]))

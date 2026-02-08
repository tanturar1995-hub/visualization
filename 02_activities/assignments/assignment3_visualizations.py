"""
Assignment 3 - Data Visualizations from Open Data (Python portion)

This script produces:
1) viz1_python_region_counts.png  (Python/matplotlib)
2) CSV tables used to build the Excel visualization:
   - crosstab_region_programtype_counts.csv
   - crosstab_region_programtype_percent.csv

Reproducibility notes:
- No manual editing is required to regenerate the outputs.
- If you change the dataset path, everything updates automatically.

Run:
  python3 code/assignment3_visualizations.py

Inputs:
  data/dataset.csv

Outputs:
  images/viz1_python_region_counts.png
  data/crosstab_region_programtype_counts.csv
  data/crosstab_region_programtype_percent.csv
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "dataset.csv"
IMG_DIR = ROOT / "images"
DATA_DIR = ROOT / "data"

def main() -> None:
    df = pd.read_csv(DATA_PATH)

    # Minimal cleaning: strip whitespace in key categorical columns
    for col in ["Region", "Program Type", "School Level", "City"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # ---- Visualization 1 (Python): counts by Region ----
    region_counts = df["Region"].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(7, 4))
    region_counts.plot(kind="bar", ax=ax)
    ax.set_title("Number of Schools by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(IMG_DIR / "viz1_python_region_counts.png", dpi=200)
    plt.close(fig)

    # ---- Tables for Visualization 2 (Excel): Program Type composition by Region ----
    ct = pd.crosstab(df["Region"], df["Program Type"])
    ct_pct = ct.div(ct.sum(axis=1), axis=0) * 100

    ct.to_csv(DATA_DIR / "crosstab_region_programtype_counts.csv")
    ct_pct.to_csv(DATA_DIR / "crosstab_region_programtype_percent.csv")

if __name__ == "__main__":
    main()

# # Class 3 — Reproducible Visualizations — Activities & Questions (answers)

# ### Slide 4 — Reproducibility and why it matters
# - A result is reproducible if someone else (or future-you) can re-run the workflow and obtain the same outputs from the same inputs.
# - It reduces errors, improves trust, and makes collaboration possible.

# ### Slide 6 — Can you spot duplications in the original images?
# - Yes: there are repeated background “speckle” patches and repeated clusters of purple shapes across panels (the same texture appears more than once).

# ### Slide 7 — If images were manipulated, can we trust conclusions?
# - It’s a serious red flag: the safest stance is **no**, until raw data + methods are provided and the analysis is independently re-verified.
# - Even if the main conclusion might still be true, manipulation undermines credibility and raises concern about other parts of the work.

# ### Slide 10 — How do we improve trust and transparency?
# - Keep raw data immutable; store analysis as scripts/notebooks; track versions with Git; document environment (requirements); use seeds for randomness; and generate figures from code (not manual edits).

# ### Slide 11 — How can we keep data visualizations honest?
# - Use correct encodings and scales; label axes/units; avoid truncated axes unless justified; show uncertainty (error bars/CI); and provide data sources + processing steps.

# ### Slide 13 — What is reproducibility? (working definition)
# - The ability for an independent person to obtain the same result using the same data + the documented analysis pipeline (code, parameters, environment).

# ### Slide 17 — What is version control for (in plain language)?
# - It’s a history system for files: you can see what changed, why, and when; collaborate without overwriting each other; and roll back to earlier working states.

# ### Slide 21 — Activity: Add comments to code
# - Good comments explain **why** something is done, assumptions, parameter meaning, and any non-obvious choices.
# - Example comment style is included in the Class 3 notes.

"""
Reproducible data visualization in-class activities

From the slides, reproducibility means someone else can re-create your result because
the **data, code, and methods** are available.

This script demonstrates a simple reproducible pattern:
1) Load or generate data
2) Make plot in code (not manual editing)
3) Save plot and any derived data
4) Keep parameters at the top; add comments
"""

from __future__ import annotations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OUTDIR = "outputs"
SEED = 613

def make_data(n: int = 50) -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    x = np.arange(n)
    y = rng.integers(0, 100, size=n)
    return pd.DataFrame({"x": x, "y": y})

def main() -> None:
    df = make_data(50)
    df.to_csv(f"{OUTDIR}/03_data.csv", index=False)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.scatter(df["x"], df["y"])
    ax.set_title("Reproducible scatter (data + code saved)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/03_reproducible_scatter.png", dpi=250)
    plt.close(fig)

    # Example “method” step: compute and save summary stats
    summary = df["y"].describe()
    summary.to_csv(f"{OUTDIR}/03_y_summary.csv")

if __name__ == "__main__":
    main()
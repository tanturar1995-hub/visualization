# Visualization 1 (Python): Number of Schools by Region

**Dataset link:** <https://data.ontario.ca/dataset/private-school-contact-information/resource/d16de265-35e9-4277-9381-0c311e802e39>  

**Date accessed:** 2026-02-08

![Bar chart of number of schools by region](images/viz1_python_region_counts.png)

## Software
Created in **Python** using `pandas` + `matplotlib`.

## Intended audience
General public (families/guardians), education analysts, and policymakers who want a quick overview of where schools are concentrated.

## Message
This visualization shows how the number of schools varies across regions, making it easy to compare regions at a glance.

## Design choices (and where applied)
- **Bar chart** for clear magnitude comparison across categories.
- **Sorted counts** (largest to smallest) to reduce cognitive load.
- **Clear title and axis labels** to make the chart self-explanatory.
- **No 3D / no decorative effects** so comparisons aren’t distorted.

## Reproducibility
- Fully reproducible: the script `code/assignment3_visualizations.py` loads the raw CSV, cleans key fields, and saves the figure automatically.
- The exact steps and outputs are determined by code, not manual edits.

## Accessibility
- Simple chart type with readable labels.
- Doesn’t rely on color to encode meaning (single-series bars).
- Includes descriptive text here (alt text in the image caption).

## Impacted communities
Families, school communities, and regional stakeholders could interpret the concentration/distribution as reflecting access and availability.

## Feature selection
Included: `Region` (most relevant for the geographic summary).  
Excluded: personal/contact fields and identifiers (not needed for the message and can distract).

## Underwater labour
Finding the dataset, checking column meanings, cleaning category labels (trimming spaces), choosing an appropriate comparison chart, and documenting the process.

## Code appendix
See: `code/assignment3_visualizations.py`

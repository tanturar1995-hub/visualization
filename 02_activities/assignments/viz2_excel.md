# Visualization 2 (Excel/LibreOffice): Program Type Composition by Region (100% Stacked)

**Dataset link:** <https://data.ontario.ca/dataset/private-school-contact-information/resource/d16de265-35e9-4277-9381-0c311e802e39>  
**Date accessed:** 2026-02-08

## Software
Created in an **Excel-compatible workbook** (`.xlsx`)

File: `viz2_excel_programtype_by_region.xlsx`

## Intended audience
Education analysts and the public who want to compare **the mix** of program types across regions (not just totals).

## Message
This visualization shows whether regions differ in the **composition** of program types (e.g., site-based vs online/hybrid).

## Design choices (and where applied)
- **100% stacked column chart**: emphasizes composition (percent) rather than raw counts.
- **Legend** identifies program types.
- **Percent scale** makes regions comparable even if they have different total numbers of schools.
- **Table next to chart** (in workbook) supports transparency.

## How to view / export (if you need an image)
1. Open `viz2_excel_programtype_by_region.xlsx`.
2. Click the chart.
3. Export as PNG/PDF (Excel: right-click chart → “Save as Picture…”).

If your instructor requires an image file, export and include:
`images/viz2_excel_programtype_by_region.png`

## Reproducibility
- The percent table is generated from the dataset by Python and saved as CSV:
  - `data/crosstab_region_programtype_percent.csv`
- The workbook contains the chart built from that table.
- Optional: run `code/make_excel_viz2.py` to regenerate the workbook/chart (useful if data changes).

## Accessibility
- Composition chart includes legend and percent scale.
- Provide the underlying percent table for screen readers / alternative access.
- When exporting, ensure readable font size and sufficient contrast.
- Add alt text in your report/submission (example):
  “100% stacked bar chart showing the percent of each program type within each region.”

## Impacted communities
Families and school communities might interpret differences in online/hybrid availability as affecting access, flexibility, or regional options.

## Feature selection
Included: `Region` and `Program Type` (directly supports composition question).  
Excluded: detailed identifiers (names/emails) because they don’t support the message and may introduce privacy concerns.

## Underwater labour
Creating the crosstab, deciding to normalize to percent, checking missing categories, and documenting how the chart should be interpreted.

## Code appendix
- Python data prep: `code/assignment3_visualizations.py`
- Workbook regeneration (optional): `code/make_excel_viz2.py`

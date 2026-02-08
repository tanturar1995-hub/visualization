# # Data Visualization — Participation Workbook

# # Class 1 — Course Intro — Activities & Questions (answers)

# ### Slide 5 — Why care about data visualization?

# - Because plots are often the fastest way to spot patterns, anomalies, and context that are hard to see in raw tables (e.g., spatial clustering, trends over time).
# - Because visuals are persuasive: the *design choices* can change decisions (good or bad), so we need to read and create charts critically.


# ### Slide 10 — Why visualize information (historical examples)?

# - **Context**: a map or spatial view can link outcomes to place (e.g., disease cases near a water pump).
# - **Argument/advocacy**: visuals can support a claim (e.g., comparing causes of death, resource allocation).
# - **Storytelling**: visuals can summarize multiple variables in one narrative (e.g., location + time + losses).


# ### Slide 15 — Another case of data viz saving lives?
# - Examples include: early COVID dashboards that guided public policy; hospital triage/bed-capacity dashboards; and risk/forecast maps for disasters (hurricanes, wildfires) that support evacuations and resource deployment.
# - The key is that the visualization makes the *right decision-relevant variables* clear (time, location, uncertainty, magnitude).

# ### Slide 18 — Activity: What is “good” data visualization?
# # - **Aesthetic**: readable, not cluttered, layout supports the story, typography and colors work.
# # - **Substantive (honest)**: scales and encodings don’t mislead; uncertainty and denominators are clear; data are not cherry-picked.
# # - **Perceptual**: what the viewer *sees first* matches what the data mean; comparisons are easy; labels/legends are clear.

# # ### Slide 19–24 — Activity: Evaluate the examples (Aesthetic / Substantive / Perceptual)
# # **Example 1 (Slide 20: 3D-style bars + textured background)**
# # - Aesthetic: busy background and pseudo‑3D hurt readability.
# # - Substantive: 3D effect can distort perceived heights and differences.
# # - Perceptual: difficult to compare categories accurately; low data-ink ratio. **Overall: not “good.”**

# # **Example 2 (Slide 21: “Monstrous costs” with monster mouth imagery)**
# # - Aesthetic: visually attention-grabbing, but decorative illustration dominates.
# # - Substantive: the shape/illustration may exaggerate change if axis/scales aren’t prominent.
# # - Perceptual: viewer may remember the “monster” more than values; encourages emotional framing. **Overall: risky / likely misleading.**

# # **Example 3 (Slide 22: same data, different aspect ratios)**
# # - Aesthetic: both are clean.
# # - Substantive: shows how *aspect ratio* can visually amplify or flatten trends without changing data.
# # - Perceptual: steepness perception changes; this is a great teaching example of why layout choices matter. **Overall: good as a demonstration, but can be misused.**

# # **Example 4 (Slide 23: distorted pie chart)**
# # - Aesthetic: flashy but confusing.
# # - Substantive: geometry is wrong (slices don’t match percentages).
# # - Perceptual: impossible to make correct comparisons. **Overall: very bad.**

# # **Example 5 (Slide 24: wind map / flow visualization)**
# # - Aesthetic: strong—beautiful and engaging.
# # - Substantive: good for showing *direction and motion*, but may not be best for precise numeric comparison.
# # - Perceptual: excellent for pattern discovery (fronts, vortices), weaker for exact values. **Overall: good for exploration; add legends/scales for rigor.**

# # ### Slide 26 — What data visualization *is* dependent on
# # - **Context** (where it will be used), **Audience** (who will read it), and **Data structure** (what variables and relationships exist).
# # - Practical rule: choose the simplest chart that answers the question for your audience, then refine for readability and honesty.


# # ### Slide 28 — What tools are used for data visualization?
# # - Common options: spreadsheets (Excel/Sheets), Python (matplotlib, seaborn, plotly), R (ggplot2), Tableau/PowerBI, and web tools (D3.js).
# # - Choice depends on required interactivity, reproducibility, and audience.
# Class 2 — Getting Started with Matplotlib

# This notebook recreates the main in-class code patterns (scatter, histogram, labels, limits, grid) and completes the required activities (including a Python Graph Gallery example).
# Getting Started with Matplotlib — Activities & In-class notes

# ### Slide 5 — What is matplotlib?
# - A Python plotting library for making static (and some interactive) figures; it’s low-level/flexible and sits underneath libraries like seaborn.

# ### Slide 6 — How matplotlib is structured (figure vs axes)?
# - **Figure** = whole canvas (can contain multiple plots).
# - **Axes** = the actual plotting area (one plot). You call methods like `ax.scatter`, `ax.plot`, etc. to add “artists” (lines, text, legend…).

# ### Slide 15 — Activity: modify code to make a histogram
# - Replace `ax.scatter(x, y)` with `ax.hist(y, bins=10)` (bins optional). You usually histogram *one variable* (the values), not x vs y.

# ### Slide 27–28 — Activity: customize grid lines
# - Use `ax.grid(axis='y', color='blue', linewidth=2, linestyle='-.')` (and tweak to your taste).

# ### Slide 31 — Python Graph Gallery activity (example + feedback)
# - I chose a **lollipop chart** (category vs value) and replicated it using Matplotlib’s `stem()` approach.
# - **Aesthetic**: usually clean because it reduces heavy bars; good spacing/labels are still required.
# - **Substantive**: honest if the baseline is clear and categories are sorted sensibly; don’t hide the axis or truncate without disclosure.
# - **Perceptual**: makes rank/comparison easy (dots are quick to compare) but can be harder if too many categories; labeling becomes critical.

# ### Slide 33 — Preview question: what does ‘objective’ mean in data viz?
# - ‘Objective’ usually means being transparent about choices (scales, filters, encodings), showing uncertainty, and minimizing misleading framing—*not* that the visualization is free of choices.

# import numpy as np
import matplotlib.pyplot as plt

np.random.seed(613)

# sample data (matches the slide structure)
x = np.arange(50)
y = np.random.randint(0, 100, 50)

## Basic scatter (figure + axes)
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
ax.set_title("Basic scatter")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
## Small customizations (marker size, transparency)
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y, s=40, alpha=0.8)
ax.set_title("Scatter with simple styling")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
plt.show()
## Axis limits
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
ax.set_xlim(0, 60)      # extend beyond data to show effect
ax.set_ylim(0, 110)
ax.set_title("Scatter with x/y limits")
plt.show()
## Activity (Slide 15): Make a histogram of `y`
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(y, bins=10)  # bins optional
ax.set_title("Histogram of y")
ax.set_xlabel("y value")
ax.set_ylabel("count")
plt.show()
## Activity (Slides 27–28): Customize grid lines
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
ax.set_title("Grid line customization")
ax.grid(axis="y", color="blue", linewidth=2, linestyle="-.")
plt.show()
## Activity (Slide 31): Python Graph Gallery example — Lollipop chart

# This is an original re-implementation inspired by typical lollipop charts (category vs numeric).
categories = np.array(["A", "B", "C", "D", "E", "F"])
values = np.array([12, 7, 19, 4, 15, 10])

fig, ax = plt.subplots(figsize=(6, 3))
(markerline, stemlines, baseline) = ax.stem(categories, values, basefmt=" ")
# Make it look like a classic "lollipop": thinner stems + larger markers
plt.setp(stemlines, linewidth=2)
plt.setp(markerline, markersize=8)

ax.set_title("Lollipop chart (Matplotlib stem)")
ax.set_xlabel("Category")
ax.set_ylabel("Value")
ax.grid(axis="y", linestyle=":", linewidth=1)
plt.show()
### Quick feedback (required in the slide)
# - **Aesthetic:** clean and less ‘heavy’ than bars; works best with sorted categories.
# - **Substantive:** honest when baseline is clear and axis is labeled; avoid truncating axes.
# - **Perceptual:** dot position makes comparisons quick; too many categories can become crowded.
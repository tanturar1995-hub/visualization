# # Class 4 — Choosing the Right Visualization — Activities & Questions (answers)

# ### Slide 9 — How do we decide what type of visualization to use? Does it matter?
# - Yes: chart type controls what comparisons are easy. Pick based on your question: trends over time → line; category comparison → bar/lollipop; distributions → histogram/box; relationships → scatter; composition → stacked/area (carefully).

# ### Slide 10 — Choosing the right visualization (rule of thumb)
# - Start with the analytical task (compare, rank, show change, show distribution, show relationship), then pick the simplest encoding that supports it.

# ### Slide 11–16 — Activity: analyze the two gun-violence visualizations
# **Viz #1 (Slides 12–14: many arcs/markers by state)**
# - What it helps you learn: relative magnitude by state/region; where events cluster.
# - Not neutral: the style is emotive/advocacy-driven (dark background, dramatic arcs) and encourages a moral/political reading.


# **Viz #2 (Slide 13 + 15): bar chart of incidents by year**
# - What it helps you learn: trend over time and year-to-year comparison.
# - More neutral *in tone*, but choices still matter (definition of ‘incident’, time window, data source).

# **Slide 16: qualities that make Viz #2 effective**
# - Clear axis labels, simple encoding (length), easy comparison, consistent scale, minimal decoration, and the message matches what you see first (rising counts).

# ### Slide 18 — Jobs report: same data, different story?
# - When a figure changes scale, baseline, annotations, or what time window is shown, it can shift perception from “recovery is strong” to “recovery is weak/uneven.”
# - The lesson: *framing choices* (what’s highlighted, what’s omitted) change the narrative even if the numbers are real.

# ### Slide 21–22 — Can data visualization be ‘neutral’?
# - Not fully: every visualization involves choices (what to include, scale, color, annotations).
# - But you *can* aim for fairness by being transparent, showing context/uncertainty, and avoiding manipulative design.

# ### Slide 27 — Recall the three qualities
# - Aesthetic, Substantive (honest), and Perceptual (easy to interpret correctly).

# ### Slide 29 — What do we want our visualization to do?
# - Typical goals: help people **discover** patterns, **compare** values, **communicate** a key message, and **support decisions**. The goal should drive design.

# ### Slide 37 — How do people perceive data visualizations?
# - People use pre-attentive cues (position, length, angle, color) first; good charts map important data to strong cues (position/length) and reduce cognitive load with labeling and grouping.

# Tiny “review” code (matplotlib figure/axes):

''' python code in class 4 review '''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.random.randint(0, 10, 10)

fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x, y)
ax.set_title("Review scatter")
fig.tight_layout()
fig.savefig("outputs/04_review_scatter.png", dpi=200)
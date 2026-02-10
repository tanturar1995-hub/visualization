# # Class 5 — Customizing Our Plots — Activities & Questions (answers)

# ### Slide 5–7 — Activity: line plot with two y variables + legend
# - Yes: plot both series on the same axes and label them; then call `ax.legend()` with a location.

# ### Slide 23–24 — Activity: modify x-axis title font (fontdict)
# - Use `plt.xlabel('Shiny New X Axis!', fontsize=18, fontdict={'family':'serif','color':'indigo'})`.


# Class 5 — Customizing Our Plots

# This notebook recreates the in-class examples: legends, annotations, axis labels, and styles. It also completes the listed activities.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

## Activity (Slides 5–6): line plot with both y variables on the same axes
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y1, label="Series 1")
ax.plot(x, y2, label="Series 2")
ax.set_title("Two line series on one axes")
ax.set_xlabel("x")
ax.set_ylabel("value")
ax.legend(loc="lower right")
plt.show()
## Annotations: text + arrows
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y1, label="Series 1")
ax.plot(x, y2, label="Series 2")
ax.legend(loc="lower right")

# annotate the max of y1
imax = int(np.argmax(y1))
ax.scatter([x[imax]], [y1[imax]])
ax.annotate("max of Series 1",
            xy=(x[imax], y1[imax]),
            xytext=(x[imax]+5, y1[imax]+10),
            arrowprops=dict(arrowstyle="->"))
ax.set_title("Example annotation")
plt.show()
## Shapes: vertical line + shaded region
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y1)
ax.set_title("Guides and regions")

# vertical reference line
ax.axvline(25, linestyle="--", linewidth=2)

# highlight a region
ax.axvspan(10, 20, alpha=0.2)

ax.set_xlabel("x")
ax.set_ylabel("value")
plt.show()
## Styles (global and per-axes)
# Check available styles
plt.style.available[:10]

plt.style.use("default")  # keep it predictable

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y1, label="Series 1")
ax.plot(x, y2, label="Series 2")
ax.set_title("Default style")
ax.legend()
plt.show()
## Activity (Slides 23–24): change x-axis label font using fontdict
font1 = {'family': 'serif', 'color': 'indigo'}

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y1)
ax.set_title("Fontdict example")
plt.xlabel("Shiny New X Axis!", fontsize=18, fontdict=font1)
plt.ylabel("y value")
plt.show()
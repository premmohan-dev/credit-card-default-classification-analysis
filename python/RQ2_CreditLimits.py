# Purpose:
# Visualize average credit limits for customers who defaulted and customers who did not.

# Research Question 2
# How do credit limits differ between customers who default and customers who do not?

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Default Status Groups
status_groups = [
    "No Default",
    "Default"
]

# Average Credit Limits
average_credit_limits = [
    178099.73,
    130109.66
]

# Create Chart
fig, ax = plt.subplots(figsize=(8, 6))

bars = ax.bar(
    status_groups,
    average_credit_limits,
    color=["seagreen", "firebrick"]
)

ax.set_title("Average Credit Limit by Default Status")
ax.set_xlabel("Default Status")
ax.set_ylabel("Average Credit Limit")

# Start y-axis at 0
ax.set_ylim(0, 200000)

# Add Data Labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height:,.0f}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

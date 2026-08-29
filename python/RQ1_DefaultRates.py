# Purpose:
# Visualize default rates across education groups.

# Research Question 1
# How do default rates vary across customer demographic groups?

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Education Groups
education_groups = [
    "Graduate School",
    "University",
    "High School"
]

# Default Rates (%)
default_rates = [
    19.23,
    23.73,
    25.16
]

# Create Chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    education_groups,
    default_rates,
    color="steelblue"
)

ax.set_title("Default Rate by Education Level")
ax.set_xlabel("Education Level")
ax.set_ylabel("Default Rate (%)")

# Start y-axis at 0 for a proportional comparison
ax.set_ylim(0, 30)

# Add Data Labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height:.2f}%",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

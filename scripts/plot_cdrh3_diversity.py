import pandas as pd
import matplotlib.pyplot as plt

#Load diversity summary
df = pd.read_csv("cdrh3_diversity_summary.csv")

#Plot
plt.figure(figsize=(8,5))

plt.bar(
    df["h3_length"].astype(str),
    df["unique_rate_percent"],
)

plt.xlabel("CDRH3 Length")
plt.ylabel("Unique Sequences (%)")
plt.title("Sequence Diversity of ESM3-Generated CDRH3 Libraries")

plt.ylim(0, 105)

for i, value in enumerate(df["unique_rate_percent"]):
    plt.text(i, value + 1, f"{value:.1f}%", ha="center", fontsize=10)

plt.tight_layout()

plt.savefig(
    "cdrh3_diversity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
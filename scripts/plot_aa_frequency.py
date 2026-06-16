import pandas as pd
import matplotlib.pyplot as plt

#Load data
df = pd.read_csv("aa_frequency.csv")

#Sort by frequency
df = df.sort_values("frequency", ascending=False)

#Plot
plt.figure(figsize=(10,5))
plt.bar(
    df["amino_acid"],
    df["frequency"]*100
)

plt.xlabel("Amino Acid")
plt.ylabel("Frequency (%)")
plt.title("ESM3-generated CDRH3 Amino Acid Composition")

plt.tight_layout()

plt.savefig(
    "aa_frequency.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
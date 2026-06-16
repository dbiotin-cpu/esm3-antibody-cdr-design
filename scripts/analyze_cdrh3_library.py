import pandas as pd
from collections import Counter

df = pd.read_csv("esm3_cdrh3_library.csv")

print("Total sequences:", len(df))
print("\nCounts by length:")
print(df["h3_length"].value_counts().sort_index())

print("\nUnique sequences by length:")
print(df.groupby("h3_length")["generated_cdrh3"].nunique())

all_sequences = "".join(df["generated_cdrh3"])
aa_counts = Counter(all_sequences)

aa_df = pd.DataFrame(
    aa_counts.items(),
    columns=["amino_acid", "count"]
).sort_values("count", ascending=False)

aa_df["frequency"] = aa_df["count"] / aa_df["count"].sum()

aa_df.to_csv("aa_frequency.csv", index=False)

print("\nAmino acid frequency:")
print(aa_df)
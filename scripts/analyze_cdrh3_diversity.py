import pandas as pd

#Load generated CDRH3 library
df = pd.read_csv("esm3_cdrh3_library.csv")

#Basic diversity summary
summary = (
    df.groupby("h3_length")
    .agg(
        total_sequences=("generated_cdrh3", "count"),
        unique_sequences=("generated_cdrh3", "nunique")
    )
    .reset_index()
)

summary["duplicate_sequences"] = (
    summary["total_sequences"] - summary["unique_sequences"]
)

summary["unique_rate_percent"] = (
    summary["unique_sequences"] / summary["total_sequences"] * 100
).round(1)

#Save result
summary.to_csv("cdrh3_diversity_summary.csv", index=False)

print(summary)
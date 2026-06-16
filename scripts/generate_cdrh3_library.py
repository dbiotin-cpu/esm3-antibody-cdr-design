import os
import csv
import time
from esm.sdk.forge import ESM3ForgeInferenceClient
from esm.sdk.api import ESMProtein, GenerationConfig

client = ESM3ForgeInferenceClient(
    model="esm3-open-2024-03",
    url="https://biohub.ai",
    token=os.environ["BIOHUB_API_KEY"],
)

prefix = "TAVYYC"
suffix = "WGQGTLVTVSS"

h3_lengths = [6, 8, 10, 12]
n_per_length = 50

output_file = "esm3_cdrh3_library.csv"

rows = []

for h3_length in h3_lengths:
    masked_sequence = prefix + ("_" * h3_length) + suffix

    print(f"\nGenerating CDRH3 length {h3_length}")

    for i in range(n_per_length):
        protein = ESMProtein(sequence=masked_sequence)

        result = client.generate(
            protein,
            GenerationConfig(
                track="sequence",
                num_steps=8,
                temperature=0.9,
            ),
        )

        if hasattr(result, "sequence") and result.sequence:
            full_sequence = result.sequence
            cdrh3 = full_sequence[len(prefix):len(prefix) + h3_length]

            rows.append({
                "h3_length": h3_length,
                "sample_id": i + 1,
                "input_sequence": masked_sequence,
                "generated_cdrh3": cdrh3,
                "full_generated_sequence": full_sequence,
            })

            print(f"{i + 1:03d}: {cdrh3}")
        else:
            print(f"{i + 1:03d}: failed")

        time.sleep(0.3)

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "h3_length",
            "sample_id",
            "input_sequence",
            "generated_cdrh3",
            "full_generated_sequence",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"\nSaved {len(rows)} sequences to {output_file}")
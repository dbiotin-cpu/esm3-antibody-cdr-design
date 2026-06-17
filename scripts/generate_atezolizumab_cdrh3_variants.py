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

heavy_chain = "EVQLVESGGGLVQPGGSLRLSCAASGFTFSDSWIHWVRQAPGKGLEWVAWISPYGGSTYYADSVKGRFTISADTSKNTAYLQMNSLRAEDTAVYYCARRHWPGGFDYWGQGTLVTVSSASTKGPSVFPLAPSGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEP"
original_cdrh3 = "RHWPGGFDY"
masked_cdrh3 = "_"*len(original_cdrh3)

masked_heavy_chain = heavy_chain.replace(original_cdrh3, masked_cdrh3)

print("Original CDRH3", original_cdrh3)
print("Masked heavy chain: ")
print(masked_heavy_chain)

n_variants = 50
output_file = "atezolizumab_cdrh3_variants.csv"

rows = []

for i in range(n_variants):
        protein = ESMProtein(sequence=masked_heavy_chain)

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

            cdrh3_start = heavy_chain.index(original_cdrh3)
            cdrh3_end = cdrh3_start + len(original_cdrh3)

            generated_cdrh3 = full_sequence[cdrh3_start:cdrh3_end]

            rows.append({
                "sample_id": i + 1,
                "original_cdrh3": original_cdrh3,
                "generated_cdrh3": generated_cdrh3,
                "masked_heavy_chain": masked_heavy_chain,
                "full_generated_heavy_chain": full_sequence,
            })

            print(f"{i + 1:03d}: {generated_cdrh3}")
        else:
            print(f"{i + 1:03d}: failed")

        time.sleep(0.3)

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "sample_id",
            "original_cdrh3",
            "generated_cdrh3",
            "masked_heavy_chain",
            "full_generated_heavy_chain",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"\nSaved {len(rows)} sequences to {output_file}")
import os
from esm.sdk.forge import ESM3ForgeInferenceClient
from esm.sdk.api import ESMProtein, GenerationConfig
client = ESM3ForgeInferenceClient(
    model="esm3-open-2024-03",
    url="https://biohub.ai",
    token=os.environ["BIOHUB_API_KEY"],
)

# using residues near CDRH3: YYC + masked CDRH3 + WGQGTLVTVSS
prefix = "TAVYYC"
suffix = "WGQGTLVTVSS"

for h3_length in [6, 8, 10, 12]:
    sequence = prefix + ("_" * h3_length) + suffix

    print("\n" + "=" * 60)
    print(f"Masked length = {h3_length}")
    print("Input:", sequence)

    protein = ESMProtein(sequence=sequence)

    result = client.generate(
        protein,
        GenerationConfig(
            track="sequence",
            num_steps=8,
            temperature=0.7,
        ),
    )

    print("Result:", result)

    if hasattr(result, "sequence") and result.sequence:
        generated = result.sequence
        cdrh3 = generated[len(prefix):len(prefix) + h3_length]
        print("Generated CDRH3:", cdrh3)
        print("Full generated:", generated)
    else:
        print("Failed.")
# Evaluating ESM3 for Antibody CDRH3 Sequence Generation

## Project Overview

This project explores the ability of ESM3, a multimodal protein foundation model, to generate antibody CDRH3 sequences within a fixed antibody framework.

Using masked sequence generation, I investigated how ESM3 completes missing CDRH3 regions of varying lengths and evaluated the diversity of generated sequences.

This work was performed as part of my hands-on exploration of AI-driven protein engineering tools and their potential applications in antibody discovery.

---

## Motivation

Antibody specificity is largely determined by the complementarity-determining regions (CDRs), particularly CDRH3, which often plays a dominant role in antigen recognition.

Recent protein language models have demonstrated the ability to generate biologically meaningful protein sequences. This project aims to evaluate whether ESM3 can generate plausible CDRH3 sequences when provided with a fixed antibody framework.

As a protein engineer with 10 years of experience in antibody discovery and engineering, I was interested in understanding how foundation models might contribute to future antibody design workflows.

---

## Workflow

```text
Antibody Framework

TAVYYC ______ WGQGTLVTVSS

↓

Mask CDRH3 Region

↓

ESM3 Sequence Generation

↓

Extract Generated CDRH3

↓

Sequence Analysis
```

---

## Experimental Design

### Antibody Framework

Prefix:

```text
TAVYYC
```

Suffix:

```text
WGQGTLVTVSS
```

### Tested CDRH3 Lengths

* 6 amino acids
* 8 amino acids
* 10 amino acids
* 12 amino acids

For each experiment, the CDRH3 region was masked and generated using ESM3.

---

## Example Results

| Mask Length | Generated CDRH3 |
| ----------- | --------------- |
| 6           | AAGTSI          |
| 8           | ARWDDTWY        |
| 10          | AARSGSGSWV      |
| 12          | ARRDGGGGGFDV    |

Example generated sequence:

```text
Input:
TAVYYC______WGQGTLVTVSS

Output:
TAVYYCAAGTSIWGQGTLVTVSS

```
## Amino Acid Composition

![AA Frequency](images/aa_frequency.png)

Analysis of 200 generated CDRH3 sequences revealed a strong enrichment of glycine (25.7%), followed by alanine (12.2%) and serine (11.7%). Aromatic residues such as tyrosine and tryptophan were also observed, while no cysteine residues were generated.

---

## CDRH3 Diversity Analysis

![CDRH3 Diversity](images/cdrh3_diversity.png)

Across all tested loop lengths, ESM3 generated highly diverse CDRH3 libraries with unique sequence rates ranging from 90% to 100%.

The highest diversity was observed for 8-amino-acid loops, while all longer loop lengths maintained greater than 97% uniqueness. These results suggest that ESM3 explores a broad sequence space even when constrained within a fixed antibody framework.

---

## Antibody Scaffold-Based CDRH3 Redesign

To explore a more biologically relevant application, I extended the workflow from antigen-free CDRH3 generation to scaffold-constrained antibody redesign.

The heavy-chain framework of atezolizumab, a clinically approved anti-PD-L1 antibody, was used as a fixed scaffold. The native CDRH3 sequence:

```text
RHWPGGFDY
```

was masked and regenerated using ESM3 while preserving the surrounding antibody framework.

### Example Generated Variants

| Original CDRH3 | ESM3-Generated CDRH3 |
| -------------- | -------------------- |
| RHWPGGFDY      | GDGYGYFDY            |
| RHWPGGFDY      | GGYYYSMDY            |
| RHWPGGFDY      | GGYGFALDY            |
| RHWPGGFDY      | GGYYYGFDY            |
| RHWPGGFDY      | DDYYYGMDY            |

### Observations

Several notable sequence patterns emerged from the generated variants:

* Glycine (G) and tyrosine (Y) were strongly enriched across the redesigned CDRH3 sequences.
* Most generated variants preserved the original loop length of 9 amino acids.
* Multiple candidates retained the C-terminal `DY` motif, suggesting that ESM3 recognized local sequence context within the antibody framework.
* The original `RHWP` motif was not preserved, indicating that ESM3 explored alternative sequence solutions while maintaining overall antibody-like characteristics.

This experiment demonstrates how a protein foundation model can be applied to therapeutic antibody scaffolds to generate diverse CDRH3 candidates. Antigen-specific binding cannot be inferred directly from sequence generation and would require downstream structural modeling and experimental validation.


---

## Repository Structure

```text
README.md

scripts/
├── cdrh3_generation.py
├── generate_cdrh3_library.py
├── analyze_cdrh3_library.py
├── analyze_cdrh3_diversity.py
├── plot_aa_frequency.py
└── plot_cdrh3_diversity.py

results/
├── esm3_cdrh3_library.csv
├── aa_frequency.csv
└── cdrh3_diversity_summary.csv

images/
├── aa_frequency.png
└── cdrh3_diversity.png

```

---

## Key Observations

A library of 200 CDRH3 sequences was generated using ESM3 across four loop lengths (6, 8, 10, and 12 amino acids).

Analysis of the generated sequences revealed several notable trends:

* Glycine was the most abundant residue (25.7%), suggesting a strong preference for flexible loop conformations.
* Aromatic residues (Y, W, and F) accounted for approximately 10% of all generated residues, consistent with their frequent involvement in antibody-antigen recognition.
* Charged residues such as Arg (7.5%) and Asp (8.7%) were also enriched, indicating the potential for electrostatic interactions.
* No cysteine residues were generated within the designed CDRH3 regions, reducing the risk of unintended disulfide bond formation.

Overall, the generated sequences displayed several characteristics commonly observed in natural antibody repertoires, suggesting that ESM3 captures biologically relevant patterns within antibody sequence space.


---

## Future Work

- Structural filtering of ESM3-generated CDRH3 variants
- Antibody-antigen complex prediction using Boltz-1 or AlphaFold-based workflows
- Interface scoring and ranking of redesigned antibodies
- Developability assessment (aggregation, stability, and liability prediction)
- Expansion from scaffold-constrained redesign to antigen-aware antibody engineering

---

## Author

Protein engineer with 10 years of industry experience in antibody discovery, protein engineering, and biologics development.

This project was conducted as part of a broader effort to evaluate modern AI-based protein design technologies for therapeutic antibody engineering.

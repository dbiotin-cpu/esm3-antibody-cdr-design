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

---

## Repository Structure

```text
README.md

scripts/
└── cdrh3_generation.py

results/

images/
```

---

## Key Observations

Several generated CDRH3 sequences contained features commonly observed in natural antibody repertoires, including:

* Aromatic residues (Y, W)
* Glycine-rich motifs
* Charged residues (R, D)
* Variable loop lengths

These preliminary results suggest that ESM3 captures biologically relevant sequence patterns that may be useful for antibody engineering applications.

---

## Future Work

* Generate larger CDRH3 libraries (100+ sequences per length)
* Analyze amino acid composition
* Compare generated sequences with natural antibody repertoires
* Evaluate developability-related properties
* Integrate ESM3-generated CDRs into downstream structure prediction workflows

---

## Author

Protein engineer with 10 years of industry experience in antibody discovery, protein engineering, and biologics development.

This project was conducted as part of a broader effort to evaluate modern AI-based protein design technologies for therapeutic antibody engineering.

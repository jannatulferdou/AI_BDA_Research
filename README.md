<div align="center">

# AI BDA Research

### Research repository for the conference paper
### Big Data and Artificial Intelligence in Sustainable Entrepreneurship: Economic Performance Analysis and Market Entry Strategies

</div>

## Overview

This repository contains the working dataset, Python analysis pipeline, generated tables, and figures for a quantitative research project examining how **artificial intelligence (AI)** and **big data analytics (BDA)** relate to **sustainable entrepreneurship**, **employment-linked outcomes**, and **broader economic performance** in emerging economies, with a primary empirical focus on **South Asia**.

The repository supports a reproducible research workflow for conference presentation, academic review, and future extension. It combines **country-year panel analysis**, **fixed-effects modeling**, and **Random Forest-based variable importance** to study whether stronger AI-related ecosystem conditions are associated with more resilient and growth-oriented entrepreneurial environments.

---

## Paper Information

**Conference:** 13th International Conference on Responsible Management in the Age of AI\
**Institution:** IILM University\
**Date:** March 2026

### Paper Title

**Big Data and Artificial Intelligence in Sustainable Entrepreneurship: Economic Performance Analysis and Market Entry Strategies**

### Authors

1. **Md Emon Chowdhury** — Independent Researcher in Economics, South Keraniganj, Dhaka, Bangladesh
2. **Jannatul Ferdous** — Independent Researcher in Machine Learning, Khulna, Bangladesh
3. **Fahmida Faiza** — Milestone College, Mohammadpur, Dhaka, Bangladesh
4. **Rafia Antara** — RDA Lab. School and College, Bogura, Bangladesh
5. **Addayan Barman** — Independent Researcher in Computer Science, South Jatrabari, Dhaka, Bangladesh

### Corresponding Author

**Md Emon Chowdhury**\
Email: [**mdemonchawdhury72@gmail.com**](mailto\:mdemonchawdhury72@gmail.com)\
ORCID: **0009-0009-8757-275X**

---

## Abstract Snapshot

Sustainable entrepreneurship is increasingly framed as a development pathway in emerging economies, but the economic value of integrating AI and big data into such ventures remains under-tested in empirical work. This study addresses that gap through a mixed-method, quantitatively weighted design using a ten-year unbalanced panel for seven South Asian economies. The analysis draws on data synthesized from **Global Entrepreneurship Monitor (GEM)**, **World Bank Development Indicators**, **Crunchbase**, and selected supporting secondary sources. Fixed-effects panel models and a machine-learning component are used to evaluate how AI-related ecosystem indicators relate to entrepreneurial resilience, investment intensity, employment-linked outcomes, and macroeconomic performance. The study argues that digital capability matters not merely as a productivity tool, but as a strategic resource for market entry, adaptation, and growth under institutional and informational constraints.

---

## Research Focus

### Central Research Question

How are AI- and data-related ecosystem conditions associated with the economic performance of sustainable entrepreneurship in emerging economies?

### Core Objectives

- Examine whether stronger AI-related indicators are associated with improved economic performance.
- Explore how AI adoption relates to employment-linked entrepreneurial outcomes.
- evaluate whether digital capability supports resilience, investment intensity, and market-entry positioning under uncertainty.
- Compare cross-country trends across South Asia.
- Complement econometric interpretation with machine-learning-based variable importance.

### Keywords

**Artificial Intelligence, Big Data Analytics, Sustainable Entrepreneurship, Economic Performance, Market Entry Strategy, Emerging Economies**

---

## Study Design at a Glance

| Component                 | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| **Research design**       | Mixed-method, quantitatively weighted                           |
| **Geographic scope**      | Bangladesh, India, Pakistan, Sri Lanka, Nepal, Bhutan, Maldives |
| **Time span**             | 2015–2025                                                       |
| **Panel structure**       | Unbalanced country-year panel                                   |
| **Observations**          | 77                                                              |
| **Main inference window** | 2020–2025                                                       |
| **Quantitative sources**  | GEM, World Bank Development Indicators, Crunchbase              |
| **Supplementary sources** | Oxford Insights, Statista, regional market and policy reports   |
| **Econometric approach**  | Country fixed effects with year fixed effects                   |
| **ML component**          | Random Forest feature importance                                |
| **Contextual anchor**     | Qualitative evidence from Bangladesh                            |

---

## Repository Structure

```text
AI_BDA_Research/
├── data/
│   └── south_asia_ai.csv
├── output/
│   ├── figure2_ai_market_trend.png
│   ├── figure3_bangladesh_trend.png
│   ├── figure4_adoption_employment.png
│   ├── figure5_rf_importance.png
│   ├── table2_descriptive_statistics.csv
│   ├── table3_correlation_matrix.csv
│   ├── table4_fe_ai_employment.csv
│   ├── table5_fe_economic_performance.csv
│   └── table6_rf_importance.csv
└── analysis.py
```

---

## Repository Contents

### `data/`

Contains the analytical dataset used for the study.

- `` — country-year dataset covering macroeconomic indicators, AI ecosystem measures, entrepreneurship-related outcomes, and derived normalized variables.

### `output/`

Stores exported tables and generated visual outputs from the analysis pipeline.

#### Figures

- `` — trend visualization for AI market development across the study context.
- `` — Bangladesh-focused trend analysis.
- `` — visual representation of the relationship between AI adoption and employment-linked outcomes.
- `` — Random Forest variable-importance plot.

#### Tables

- `` — descriptive summary of core variables.
- `` — pairwise correlation matrix for preliminary diagnostics.
- `` — fixed-effects estimation output for employment-related outcomes.
- `` — fixed-effects estimation output for economic performance.
- `` — numerical feature-importance values from the Random Forest model.

### `analysis.py`

Main Python script for the full analytical workflow, including:

- data import and cleaning,
- variable harmonization,
- descriptive statistics,
- correlation analysis,
- panel regression estimation,
- Random Forest modeling,
- figure generation, and
- export of final outputs.

---

## Data and Variables

The dataset is organized around three analytical layers:

### 1. Macroeconomic Context

- GDP (current US\$ billions)
- R&D expenditure as a percentage of GDP

### 2. Digital and AI Ecosystem

- AI market size
- AI-specific startup investment
- Government AI readiness
- Internet penetration
- AI adoption rate

### 3. Labour and Entrepreneurship Outcomes

- AI-related employment share
- AI investment as a share of total startup funding

### Constructed Cross-Country Indicators

- **AI\_Market\_Pct\_GDP** — AI market size as a percentage of GDP
- **AI\_Inv\_Pct\_Total\_Startup** — AI-specific investment as a percentage of total startup funding

These derived variables are used to improve cross-country comparability and capture the relative depth of digital entrepreneurship and AI-based market-entry intensity.

---

## Methodological Pipeline

### 1. Data Assembly

The dataset was synthesized from multiple international and regional secondary sources and harmonized by country and year.

### 2. Data Preparation

- monetary values were converted into consistent units,
- variable names were standardized,
- missing values were preserved where reliable estimates did not exist,
- continuous predictors used in the machine-learning stage were standardized with z-scores.

### 3. Descriptive and Diagnostic Analysis

- descriptive statistics were generated,
- correlation matrices were produced,
- variable relationships were explored before model estimation.

### 4. Econometric Modeling

The main quantitative strategy uses **country fixed effects with year fixed effects** to estimate associations between AI-related indicators and key outcomes such as employment-linked performance and broader economic performance.

### 5. Machine Learning Layer

A **Random Forest** model was used to assess variable importance and provide an additional non-linear perspective on predictor relevance.

### 6. Contextual Interpretation

Quantitative findings were interpreted alongside qualitative context from **Bangladesh**, especially around algorithmic pricing, targeted decision-making, and market adaptation in information-constrained environments.

---

## Main Analytical Takeaways

This repository is built around a measured, evidence-based interpretation of the paper's findings.

### Key takeaways

- Stronger AI- and data-related ecosystem conditions are positively associated with **entrepreneurial resilience**, **investment intensity**, and **broader economic performance**.
- The most consistent relationships appear around **AI adoption**, **internet penetration**, and **AI readiness**, rather than the mere existence of digital markets.
- Bangladesh serves as a grounded contextual case showing how AI-assisted pricing, targeting, and decision processes can function as practical responses to persistent information frictions.
- The paper treats AI not simply as a productivity aid, but as a **strategic capability** for entry, adaptation, and competitive positioning.

### Important interpretive boundary

The dataset is structured at the **country-year ecosystem level**, not at the startup level. Accordingly, this repository is better suited to discussions of **ecosystem resilience**, **capital acquisition efficiency**, **employment-linked outcomes**, and **macroeconomic association** than literal startup survival probabilities.

---

## How to Run the Project

### Requirements

Install Python and the core scientific libraries used in the workflow.

```bash
pip install pandas numpy matplotlib statsmodels scikit-learn
```

### Run the analysis

From the repository root:

```bash
python analysis.py
```

The script reads the dataset from `data/` and writes generated tables and figures to `output/`.

---

## Expected Outputs

Running the full workflow should generate:

- descriptive statistics tables,
- correlation diagnostics,
- fixed-effects regression outputs,
- Random Forest feature-importance outputs,
- publication-ready research figures.

---

## Reproducibility Notes

To preserve consistency across replications:

- keep the existing repository structure unchanged,
- ensure `south_asia_ai.csv` remains in the `data/` directory,
- preserve original variable names unless the analysis script is updated accordingly,
- verify Python package compatibility if using a newer environment,
- treat missing values carefully rather than forcing artificial completion.

---

## Research Contribution

This repository contributes to the growing literature on:

- AI and sustainable entrepreneurship,
- digital capability in emerging economies,
- market entry strategy under informational and institutional uncertainty,
- macro–meso empirical analysis of entrepreneurship ecosystems,
- mixed quantitative research workflows in applied economics.

It is particularly relevant for scholars and practitioners interested in how technological capability can shape **resilience**, **investment efficiency**, and **growth-oriented entrepreneurship** in the Global South.

---

## Limitations

This repository should be interpreted in line with the underlying study design.

### Main limitations

- The dataset is an **unbalanced panel** with **77 observations** across **seven South Asian economies**.
- AI-specific variables are densest mainly from **2020 onward**, which limits long-horizon inference.
- Several measures are **ecosystem-level proxies**, not direct startup-level observations.
- Data coverage is uneven across smaller economies, especially for earlier years.
- The Random Forest component complements interpretation, but does **not** resolve endogeneity.

In other words: useful evidence, yes; magical omniscience, no.

---

## Suggested Use Cases

This repository may be useful for:

- conference paper replication,
- academic presentation support,
- undergraduate and graduate research reference,
- AI policy and entrepreneurship analysis,
- research-methods teaching using Python,
- extension into future firm-level or cross-regional studies.

---

## Recommended Next Improvements

Potential enhancements for future versions of the repository include:

- adding a `` file,
- adding a `` file,
- adding a `` file for GitHub citation support,
- adding a short **project summary in the README header**,
- adding figure previews directly into the README,
- providing a notebook-based replication version,
- including robustness checks and extended model specifications,
- documenting variable definitions in a dedicated data dictionary.

---

## Citation

If you use this repository, please cite the associated paper.

```bibtex
@misc{chowdhury2026aibda,
  title        = {Big Data and Artificial Intelligence in Sustainable Entrepreneurship: Economic Performance Analysis and Market Entry Strategies},
  author       = {Chowdhury, Md Emon and Ferdous, Jannatul and Faiza, Fahmida and Antara, Rafia and Barman, Addayan},
  year         = {2026},
  note         = {Research repository for the 13th International Conference on Responsible Management in the Age of AI, IILM University},
  howpublished = {GitHub repository}
}
```

---

## Licensing Recommendation

Because this repository includes **code**, **research documentation**, **generated outputs**, and a **compiled dataset**, licensing should be handled clearly and deliberately.

### Recommended structure

- **MIT License** for code components such as `analysis.py`
- **CC BY 4.0** for documentation and research presentation materials
- **Dataset reuse note** clarifying whether `south_asia_ai.csv` can be redistributed under the same terms, depending on the original source permissions

### Suggested repository note

> Unless otherwise stated, the code in this repository may be released under the MIT License. Documentation and research presentation materials may be shared under CC BY 4.0. Dataset reuse remains subject to the terms of the original data sources and compilation permissions.

---

## Contact

**Corresponding Author:** Md Emon Chowdhury\
**Email:** [mdemonchawdhury72@gmail.com](mailto\:mdemonchawdhury72@gmail.com)\
**ORCID:** 0009-0009-8757-275X

For academic collaboration, replication requests, conference communication, or repository-related questions, please contact the corresponding author.


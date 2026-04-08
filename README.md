# Mittelstand M&A Landscape Analyser 🇩🇪

> An end-to-end analysis of M&A deal activity in Germany's Mittelstand (SME) sector, covering deal volume, sector concentration, acquirer types, and EV/EBITDA valuation trends.

**Author:** Shardul Pundir
**Background:** MSc Finance, WHU Otto Beisheim School of Management (2026 intake) | CFA Level I
**LinkedIn:** [linkedin.com/in/shardulpundir](https://linkedin.com/in/shardulpundir)

> ⚠️ **Data Disclaimer:** This project is built entirely on **hypothesised, sample data** generated to simulate realistic Mittelstand M&A deal activity. It does not use any proprietary database (Mergermarket, Bloomberg, Refinitiv, etc.) and no real transaction data has been sourced or included. The project is designed as a **technical and analytical framework** — demonstrating pipeline architecture, valuation methodology, and financial reasoning — not as a factual study of actual deal flows. All figures, multiples, and trends are illustrative only.

---

## Project Overview

Germany's Mittelstand — the backbone of its economy — generates significant M&A activity that is often overlooked in favour of large-cap deal coverage. This project maps and analyses that deal landscape over a 5-year period (2019–2024), producing:

- Sector-level deal frequency and concentration analysis
- Acquirer type breakdown (strategic vs. financial/PE)
- EV/EBITDA multiple trends by sector and year
- Impact of rising interest rates (post-2022) on deal multiples
- An interactive dashboard for visual exploration
- A written 2-page investment memo on the most active sector

---

## Repository Structure

```
mittelstand-ma-analyser/
│
├── data/
│   ├── raw/              # Raw deal data (CSV exports from Mergermarket / manual)
│   └── processed/        # Cleaned, enriched datasets ready for analysis
│
├── notebooks/
│   ├── 01_data_exploration.ipynb     # First look at the data, distributions
│   ├── 02_sector_analysis.ipynb      # Sector concentration + deal frequency
│   ├── 03_valuation_trends.ipynb     # EV/EBITDA by sector and year
│   └── 04_acquirer_analysis.ipynb    # Strategic vs. PE breakdown
│
├── src/
│   ├── data_loader.py        # Load, validate, and standardise deal data
│   ├── sector_classifier.py  # Tag and clean sector labels
│   ├── valuation_metrics.py  # Compute EV/EBITDA, deal multiples
│   └── visualiser.py         # Reusable chart functions (matplotlib / plotly)
│
├── outputs/
│   ├── charts/           # Exported chart images
│   └── commentary/       # Written deal memos (PDF)
│
├── dashboard/            # Tableau / Power BI export files
├── requirements.txt
└── README.md
```

---

## Data Sources

| Source | What It Provides | Status in This Project |
|--------|-----------------|------------------------|
| Mergermarket | Comprehensive M&A deal database | Not accessed — institutional subscription required |
| Refinitiv / LSEG Workspace | Deal data + financials | Not accessed — institutional subscription required |
| Bloomberg Terminal | Company financials, multiples | Not accessed — institutional subscription required |
| Manual research | Deal press releases, company IRs | Referenced for structural design only |
| **Hypothesised sample data** | Simulated deal records modelled on public Mittelstand M&A patterns | **This is the actual data used in this project** |

**Note on data:** This project uses a fully hypothesised dataset (`data/raw/sample_deals.csv`) generated to reflect realistic Mittelstand M&A characteristics (sector mix, deal size ranges, acquirer types, EV/EBITDA multiples). No proprietary or licensed data sources have been accessed. The pipeline is designed so that real data — from Mergermarket, Refinitiv, or similar — can be dropped in once access is available, with no changes to the codebase.

---

## Setup

### Prerequisites
- Python 3.9+ (Anaconda recommended)
- Jupyter Notebook / JupyterLab

### Create environment
```bash
conda create -n mittelstand python=3.11
conda activate mittelstand
pip install -r requirements.txt
```

### Run the pipeline
```bash
# Start with data exploration
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## Key Findings *(updated as analysis progresses)*

> This section will be populated as each analysis notebook is completed.

- **Deal volume:** TBD
- **Most active sector:** TBD
- **EV/EBITDA trend (2019–2024):** TBD
- **Rate impact on multiples (post-2022):** TBD

---

## Investment Memo

A written 2-page commentary on the most active Mittelstand sector will be published in `outputs/commentary/` and posted on LinkedIn.

---

## Skills Demonstrated

`Python` `pandas` `matplotlib` `Plotly` `Tableau` `M&A Analysis` `EV/EBITDA` `Sector Research` `Data Pipeline` `Financial Commentary`

---

*This project is part of a finance portfolio built in preparation for a career in Investment Banking and Asset Management in Europe.*

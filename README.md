# Mittelstand M&A Landscape Analyser 🇩🇪

> An end-to-end analysis of M&A deal activity in Germany's Mittelstand (SME) sector, covering deal volume, sector concentration, acquirer types, and EV/EBITDA valuation trends.

**Author:** Shardul Pundir
**Background:** MSc Finance, WHU Otto Beisheim School of Management (2026) | CFA Level I
**LinkedIn:** [linkedin.com/in/shardulpundir](https://linkedin.com/in/shardulpundir)

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

| Source | What It Provides | Access |
|--------|-----------------|--------|
| Mergermarket | Comprehensive M&A deal database | Free trial (14 days) |
| Refinitiv / LSEG Workspace | Deal data + financials | WHU library access (from Sep 2026) |
| Bloomberg Terminal | Company financials, multiples | WHU library access |
| Manual research | Deal press releases, company IRs | Public |

**Note on data:** Raw data files are not included in this repository due to licensing restrictions. A sample anonymised dataset is provided in `data/raw/sample_deals.csv` to allow the pipeline to run end-to-end.

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

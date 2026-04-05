"""
data_loader.py
--------------
Load, validate, and standardise M&A deal data for the Mittelstand analyser.

Expected columns in raw CSV:
    deal_id, date, target_name, target_sector, target_country,
    acquirer_name, acquirer_type, deal_value_eur_m, ev_ebitda,
    deal_status, deal_type

Usage:
    from src.data_loader import load_deals
    df = load_deals("data/raw/sample_deals.csv")
"""

import pandas as pd
import numpy as np
from pathlib import Path


REQUIRED_COLUMNS = [
    "deal_id", "date", "target_name", "target_sector",
    "target_country", "acquirer_name", "acquirer_type",
    "deal_value_eur_m", "ev_ebitda", "deal_status", "deal_type"
]

ACQUIRER_TYPE_MAP = {
    "strategic": "Strategic",
    "corporate": "Strategic",
    "financial": "Financial (PE/VC)",
    "pe": "Financial (PE/VC)",
    "private equity": "Financial (PE/VC)",
    "vc": "Financial (PE/VC)",
    "venture": "Financial (PE/VC)",
    "management": "Management Buyout",
    "mbo": "Management Buyout",
}


def load_deals(filepath: str, filter_germany: bool = True) -> pd.DataFrame:
    """
    Load and clean deal data from a CSV file.

    Parameters
    ----------
    filepath : str
        Path to the raw deals CSV file.
    filter_germany : bool
        If True, keep only deals where the target is in Germany.

    Returns
    -------
    pd.DataFrame
        Cleaned and validated deal dataframe.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")

    df = pd.read_csv(filepath, parse_dates=["date"])

    # Validate required columns
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Filter to Germany targets
    if filter_germany:
        df = df[df["target_country"].str.lower().isin(["germany", "deutschland", "de"])]

    # Standardise acquirer type
    df["acquirer_type_clean"] = (
        df["acquirer_type"].str.lower().str.strip()
        .map(ACQUIRER_TYPE_MAP)
        .fillna("Other")
    )

    # Standardise sector labels
    df["target_sector"] = df["target_sector"].str.strip().str.title()

    # Parse numeric columns — some sources use commas or 'N/A'
    df["deal_value_eur_m"] = pd.to_numeric(
        df["deal_value_eur_m"].astype(str).str.replace(",", "").str.strip(),
        errors="coerce"
    )
    df["ev_ebitda"] = pd.to_numeric(
        df["ev_ebitda"].astype(str).str.replace("x", "").str.strip(),
        errors="coerce"
    )

    # Add year and half-year columns for time series analysis
    df["year"] = df["date"].dt.year
    df["half"] = df["date"].dt.month.apply(lambda m: "H1" if m <= 6 else "H2")
    df["year_half"] = df["year"].astype(str) + " " + df["half"]

    # Add rate regime flag (pre/post ECB rate hikes)
    df["rate_regime"] = df["year"].apply(
        lambda y: "Pre-Hike (2019–2021)" if y <= 2021 else "Post-Hike (2022–2024)"
    )

    print(f"Loaded {len(df)} deals | {df['year'].min()}–{df['year'].max()} | "
          f"{df['target_sector'].nunique()} sectors")

    return df.reset_index(drop=True)


def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a high-level summary of the deal dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned deal dataframe from load_deals().

    Returns
    -------
    pd.DataFrame
        Summary statistics table.
    """
    summary = {
        "Total deals": len(df),
        "Total deal value (EUR bn)": round(df["deal_value_eur_m"].sum() / 1000, 1),
        "Median deal size (EUR m)": round(df["deal_value_eur_m"].median(), 1),
        "Median EV/EBITDA (x)": round(df["ev_ebitda"].median(), 1),
        "Years covered": f"{df['year'].min()}–{df['year'].max()}",
        "Unique sectors": df["target_sector"].nunique(),
        "Strategic acquirers (%)": round(
            (df["acquirer_type_clean"] == "Strategic").mean() * 100, 1
        ),
        "PE/Financial acquirers (%)": round(
            (df["acquirer_type_clean"] == "Financial (PE/VC)").mean() * 100, 1
        ),
    }

    return pd.DataFrame.from_dict(summary, orient="index", columns=["Value"])

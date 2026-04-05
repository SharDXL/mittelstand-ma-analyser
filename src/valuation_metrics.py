"""
valuation_metrics.py
--------------------
Compute EV/EBITDA multiples, deal size distributions, and rate-regime
comparisons for the Mittelstand M&A analyser.
"""

import pandas as pd
import numpy as np


def ev_ebitda_by_sector(df: pd.DataFrame, min_deals: int = 3) -> pd.DataFrame:
    """
    Compute median EV/EBITDA multiple by sector.
    Only include sectors with at least `min_deals` observations.

    Returns
    -------
    pd.DataFrame sorted by median multiple descending.
    """
    result = (
        df.dropna(subset=["ev_ebitda"])
        .groupby("target_sector")["ev_ebitda"]
        .agg(
            deal_count="count",
            median_ev_ebitda="median",
            mean_ev_ebitda="mean",
            min_ev_ebitda="min",
            max_ev_ebitda="max",
        )
        .reset_index()
        .query(f"deal_count >= {min_deals}")
        .sort_values("median_ev_ebitda", ascending=False)
        .round(1)
    )
    return result


def ev_ebitda_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute median EV/EBITDA multiple by year.
    Useful for tracking the compression in multiples post-rate hikes.
    """
    return (
        df.dropna(subset=["ev_ebitda"])
        .groupby("year")["ev_ebitda"]
        .agg(deal_count="count", median_ev_ebitda="median")
        .reset_index()
        .round(1)
    )


def rate_regime_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare deal activity and multiples between pre- and post-hike periods.
    Pre-hike: 2019–2021 | Post-hike: 2022–2024
    """
    return (
        df.groupby("rate_regime").agg(
            deal_count=("deal_id", "count"),
            total_value_eur_bn=("deal_value_eur_m", lambda x: round(x.sum() / 1000, 1)),
            median_deal_size_eur_m=("deal_value_eur_m", "median"),
            median_ev_ebitda=("ev_ebitda", "median"),
            pct_pe=("acquirer_type_clean",
                    lambda x: round((x == "Financial (PE/VC)").mean() * 100, 1)),
        )
        .reset_index()
        .round(1)
    )


def deal_volume_by_year_sector(df: pd.DataFrame, top_n_sectors: int = 8) -> pd.DataFrame:
    """
    Return deal counts by year and top N sectors.
    Suitable for a stacked bar or heatmap chart.
    """
    top_sectors = (
        df["target_sector"].value_counts().head(top_n_sectors).index.tolist()
    )
    filtered = df[df["target_sector"].isin(top_sectors)]
    return (
        filtered.groupby(["year", "target_sector"])
        .size()
        .reset_index(name="deal_count")
    )

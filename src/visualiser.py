"""
visualiser.py
-------------
Reusable chart functions for the Mittelstand M&A analyser.
Uses matplotlib/seaborn for static exports and plotly for interactive views.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

# ── Style config ──────────────────────────────────────────────────────────────
NAVY   = "#1B3A6B"
ACCENT = "#2E75B6"
GOLD   = "#C4942A"
GRAY   = "#6B7280"
PALETTE = [NAVY, ACCENT, GOLD, "#1B6B4A", "#7C3AED", GRAY, "#DC2626", "#059669"]

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUTPUT_DIR = Path("outputs/charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def bar_ev_ebitda_by_sector(df_metrics: pd.DataFrame, save: bool = True):
    """
    Horizontal bar chart: Median EV/EBITDA by sector.

    Parameters
    ----------
    df_metrics : output of valuation_metrics.ev_ebitda_by_sector()
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(
        df_metrics["target_sector"],
        df_metrics["median_ev_ebitda"],
        color=ACCENT, edgecolor="white", height=0.6
    )
    ax.bar_label(bars, fmt="%.1fx", padding=4, fontsize=9, color=NAVY)
    ax.set_xlabel("Median EV/EBITDA (x)", labelpad=8)
    ax.set_title("Mittelstand M&A: Median EV/EBITDA Multiple by Sector", pad=14,
                 fontweight="bold", color=NAVY)
    ax.axvline(df_metrics["median_ev_ebitda"].median(), color=GOLD, linestyle="--",
               linewidth=1.2, label=f"Overall median: {df_metrics['median_ev_ebitda'].median():.1f}x")
    ax.legend(fontsize=9)
    ax.invert_yaxis()
    plt.tight_layout()
    if save:
        fig.savefig(OUTPUT_DIR / "ev_ebitda_by_sector.png", bbox_inches="tight")
        print("Saved: ev_ebitda_by_sector.png")
    return fig


def line_ev_ebitda_trend(df_yearly: pd.DataFrame, save: bool = True):
    """
    Line chart: Median EV/EBITDA over time — shows rate-regime impact.

    Parameters
    ----------
    df_yearly : output of valuation_metrics.ev_ebitda_by_year()
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_yearly["year"], df_yearly["median_ev_ebitda"],
            marker="o", color=ACCENT, linewidth=2.5, markersize=7)
    ax.fill_between(df_yearly["year"], df_yearly["median_ev_ebitda"],
                    alpha=0.1, color=ACCENT)

    # Shade the post-hike period
    ax.axvspan(2022, df_yearly["year"].max() + 0.5, alpha=0.07, color=GOLD,
               label="ECB rate hike cycle (2022+)")
    ax.axvline(2022, color=GOLD, linestyle="--", linewidth=1.2)

    for _, row in df_yearly.iterrows():
        ax.annotate(f"{row['median_ev_ebitda']:.1f}x",
                    (row["year"], row["median_ev_ebitda"]),
                    textcoords="offset points", xytext=(0, 10), ha="center",
                    fontsize=9, color=NAVY)

    ax.set_xlabel("Year"); ax.set_ylabel("Median EV/EBITDA (x)")
    ax.set_title("Mittelstand M&A: EV/EBITDA Multiple Trend (2019–2024)",
                 fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=9)
    ax.set_xticks(df_yearly["year"])
    plt.tight_layout()
    if save:
        fig.savefig(OUTPUT_DIR / "ev_ebitda_trend.png", bbox_inches="tight")
        print("Saved: ev_ebitda_trend.png")
    return fig


def stacked_bar_deal_volume(df_vol: pd.DataFrame, save: bool = True):
    """
    Stacked bar chart: Deal volume by year and sector.

    Parameters
    ----------
    df_vol : output of valuation_metrics.deal_volume_by_year_sector()
    """
    pivot = df_vol.pivot(index="year", columns="target_sector", values="deal_count").fillna(0)
    fig, ax = plt.subplots(figsize=(11, 6))
    pivot.plot(kind="bar", stacked=True, ax=ax, color=PALETTE[:len(pivot.columns)],
               edgecolor="white", linewidth=0.5)
    ax.set_xlabel("Year"); ax.set_ylabel("Number of Deals")
    ax.set_title("Mittelstand M&A Deal Volume by Sector (2019–2024)",
                 fontweight="bold", color=NAVY, pad=14)
    ax.legend(title="Sector", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=8)
    ax.tick_params(axis="x", rotation=0)
    plt.tight_layout()
    if save:
        fig.savefig(OUTPUT_DIR / "deal_volume_by_sector.png", bbox_inches="tight")
        print("Saved: deal_volume_by_sector.png")
    return fig


def pie_acquirer_type(df: pd.DataFrame, save: bool = True):
    """
    Pie chart: Strategic vs. PE/Financial acquirer split.
    """
    counts = df["acquirer_type_clean"].value_counts()
    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        counts, labels=counts.index, autopct="%1.1f%%",
        colors=PALETTE[:len(counts)], startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )
    for t in autotexts:
        t.set_fontsize(10); t.set_color("white"); t.set_fontweight("bold")
    ax.set_title("Mittelstand M&A: Acquirer Type Breakdown",
                 fontweight="bold", color=NAVY, pad=16)
    plt.tight_layout()
    if save:
        fig.savefig(OUTPUT_DIR / "acquirer_type_split.png", bbox_inches="tight")
        print("Saved: acquirer_type_split.png")
    return fig

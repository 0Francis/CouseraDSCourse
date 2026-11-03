"""Plotting for the stock-data project."""
import matplotlib.pyplot as plt
import pandas as pd


def make_graph(
    stock_data,
    revenue_data,
    title,
    stock_cutoff="2021-06-14",
    revenue_cutoff="2021-04-30",
):
    """Plot share price and revenue on two time-aligned subplots.

    ``stock_data`` and ``revenue_data`` must each have a ``Date`` column.
    """
    stock = stock_data[stock_data["Date"] <= pd.Timestamp(stock_cutoff)]
    revenue = revenue_data[revenue_data["Date"] <= pd.Timestamp(revenue_cutoff)]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    axes[0].plot(stock["Date"], stock["Close"], label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{title} - Historical Share Price")
    axes[0].legend()

    axes[1].plot(revenue["Date"], revenue["Revenue"], label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{title} - Historical Revenue")
    axes[1].legend()

    plt.tight_layout()
    plt.show()

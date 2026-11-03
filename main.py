"""Entry point: fetching Tesla and GameStop data, then plot it.

Run with:  python main.py
"""
import data_fetcher
from plotting import make_graph


def main():
    # Tesla
    tesla_stock = data_fetcher.get_stock_data("TSLA")
    tesla_revenue = data_fetcher.get_revenue_data(data_fetcher.TESLA_REVENUE_URL)
    make_graph(tesla_stock, tesla_revenue, "Tesla")

    # GameStop
    gme_stock = data_fetcher.get_stock_data("GME")
    gme_revenue = data_fetcher.get_revenue_data(data_fetcher.GAMESTOP_REVENUE_URL)
    make_graph(gme_stock, gme_revenue, "GameStop")


if __name__ == "__main__":
    main()

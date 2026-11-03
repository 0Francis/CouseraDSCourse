"""Data fetching for the Tesla / GameStop stock-data project.

This module replaces the old notebook cells that scraped revenue tables by
hand. It uses pandas' ``read_html``, which reads the table directly and is
simpler and more robust than a manual BeautifulSoup loop.
"""
import pandas as pd
import yfinance as yf

TESLA_REVENUE_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
)
GAMESTOP_REVENUE_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
)


def get_stock_data(ticker: str) -> pd.DataFrame:
    """Download full daily price history for a ticker.

    Returns a DataFrame with a timezone-naive ``Date`` column plus the usual
    Open/High/Low/Close/Volume columns.
    """
    stock = yf.Ticker(ticker).history(period="max").reset_index()
    stock["Date"] = pd.to_datetime(stock["Date"]).dt.tz_localize(None)
    return stock


def get_revenue_data(url: str) -> pd.DataFrame:
    """Read the *annual* revenue table from a MacroTrends page.

    Returns a DataFrame with ``Date`` and ``Revenue`` columns, sorted
    oldest-first, with ``Revenue`` as a float (millions of USD).
    """
    tables = pd.read_html(url)
    annual = next(
        t for t in tables if len(t.columns) and "Annual Revenue" in str(t.columns[0])
    )
    annual.columns = ["Date", "Revenue"]
    annual["Revenue"] = annual["Revenue"].str.replace(r"[$,]", "", regex=True).astype(float)
    annual["Date"] = pd.to_datetime(annual["Date"].astype(str), format="%Y")
    return annual.sort_values("Date").reset_index(drop=True)

from datetime import date
from pathlib import Path
import sys
from typing import List, Tuple

import yfinance
import pandas as pd


def fetch_stocks(symbols: List[str], start_date: date, end_date: date) -> List[pd.DataFrame]:
    return [
        yfinance.download(symbol, start=start_date, end=end_date)
        for symbol in symbols
    ]


def stock_history_path(symbol: str) -> Path:
    return Path(f"stock_history/{symbol}_history.csv")


def save_stock(symbol: str, df: pd.DataFrame):
    df.to_csv(stock_history_path(symbol), index=True)


def load_stock(symbol: str) -> pd.DataFrame:
    return pd.read_csv(stock_history_path(symbol))


def parse_dates(dates_arg: str) -> Tuple[date, date]:
    """Accepts two ISO dates separated by a hyphen.
    e.g. 20250701-20250801
    """
    try:
        start_str, end_str = dates_arg.split("-")
    except IndexError:
        raise RuntimeError("dates must be separated by a '-'")

    try:
        start = date.fromisoformat(start_str)
        end = date.fromisoformat(end_str)
    except Exception:
        raise RuntimeError("dates must be in ISO format")

    assert start < end, "start date must precede end date"
    return start, end


if __name__ == "__main__":
    # symbols = ["AAPL", "META", "AMZN", "NFLX", "GOOGL"]
    # start = date(2025, 7, 1)
    # end = date(2025, 8, 1)

    start, end = parse_dates(sys.argv[1])
    symbols = sys.argv[2:]

    stocks = fetch_stocks(symbols, start, end)
    for symbol, stock in zip(symbols, stocks):
        save_stock(symbol, stock)


import yfinance as yf
import datetime 


''' List of 5 stocks tickers
    Meta = META
    Apple = AAPL
    Amazon = AMZN
    Netflix = NFLX
    Google = GOOGL '''

stock_tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

for ticker in stock_tickers:
    tick = yf.Ticker(ticker)
    print("Company Website :", tick.info['website'])

def period():
    start_date = datetime.datetime(2025, 7, 1)
    end_date = datetime.datetime(2025, 7, 31)
    

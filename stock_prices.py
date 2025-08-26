import yfinance as yf
import pandas as pd

import datetime 


''' List of 5 stocks tickers
    Meta = META
    Apple = AAPL
    Amazon = AMZN
    Netflix = NFLX
    Google = GOOGL '''


def stock():
    stock_tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

    for ticker in stock_tickers:
        tick = yf.Ticker(ticker)
    
    #Time period
        start_date = datetime.datetime(2025, 7, 1)
        end_date = datetime.datetime(2025, 8, 1)

    # print data
    #data = tick.history(start = start_date, end = end_date)
    #print(f"Company Name : {ticker}")
    #print(data.to_string())

    #download data and export to a csv file
        stock_data = yf.download(ticker,start = start_date, end = end_date)
        output_file = f"C:/Users/User/Desktop/python_projects/stock_tracker/{ticker}_stock_data.csv"
        stock_data.to_csv(output_file, index = True)

if __name__ == "__main__":
    stock()


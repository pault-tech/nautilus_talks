import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker = "NVDA"

# Download the stock data at the second granularity
data = yf.download(ticker, interval="1s")

# Convert the data to a Parquet dataset
data.to_parquet("nvda_stock_data.parquet")

msft = yf.Ticker("MSFT")

# get all stock info
msft.info
print("yf.py:6 msft.info=%+v\n", msft.info)

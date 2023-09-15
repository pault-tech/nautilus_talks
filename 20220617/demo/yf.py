import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info
print("yf.py:6 msft.info=%+v\n", msft.info)

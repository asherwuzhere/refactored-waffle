import pandas as pd
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)
import yfinance as yf

msft = yf.Ticker("AAPL")

# get stock info
msft.info
print(msft.cashflow)

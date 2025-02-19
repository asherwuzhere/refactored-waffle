import yfinance as yf
import pandas as pd

# Ensure all rows and columns are visible
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 0)

# Define the stock ticker symbol
ticker = "AAPL"  # Change this to any stock symbol
stock = yf.Ticker(ticker)

# Print raw financial statements
print(stock.balance_sheet)
print(stock.cashflow)
print(stock.financials)

# Print raw stock info
print(stock.info)


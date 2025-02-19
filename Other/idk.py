import yfinance as yf
import pandas as pd

# Define parameters
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "NFLX"]  # Example stock list
lookback_period = 252  # 1-year lookback period (252 trading days)
top_n = 5  # Number of top momentum stocks to select
start_date = "2020-01-01"
end_date = "2024-02-01"

# Fetch historical stock data
data = yf.download(tickers, start=start_date, end=end_date)

# Debug: Check data structure
print("Downloaded data columns:", data.columns)

# Fix: Select 'Close' instead of 'Adj Close' using MultiIndex approach
if isinstance(data.columns, pd.MultiIndex):
    data = data.xs("Close", level=0, axis=1)  # Use 'Close' prices instead

# Check if data is empty
if data.empty:
    raise ValueError("No data retrieved. Check the tickers and date range.")

# Calculate momentum as percentage price change over the lookback period
momentum = data.pct_change(lookback_period)

# Select the latest momentum values (most recent date)
latest_momentum = momentum.iloc[-1].dropna()

# Rank stocks based on momentum
top_momentum_stocks = latest_momentum.nlargest(top_n)
print("\nTop Momentum Stocks:")
print(top_momentum_stocks)

# Backtest: Calculate equal-weighted portfolio returns
selected_stocks = top_momentum_stocks.index.tolist()
portfolio_returns = data[selected_stocks].pct_change().mean(axis=1)

# Compute cumulative returns
cumulative_returns = (1 + portfolio_returns).cumprod()

# Display cumulative returns as a DataFrame
cumulative_returns_df = pd.DataFrame(cumulative_returns, columns=["Cumulative Return"])
print("\nCumulative Returns of the Momentum Portfolio:")
print(cumulative_returns_df.tail())

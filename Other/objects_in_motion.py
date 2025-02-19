import yfinance as yf
from datetime import datetime, timedelta
import pytz

def objects_in_motion():
    # Get user input for the stock ticker
    stock_ticker = input("Enter the stock ticker symbol: ").strip()

    # Define S&P 500 ticker symbol
    sp500_ticker = '^GSPC'

    # Get current date and date ranges
    end_date = datetime.now(pytz.UTC)  # Make timezone-aware
    one_year_ago = end_date - timedelta(days=365)
    three_years_ago = end_date - timedelta(days=3 * 365)
    five_years_ago = end_date - timedelta(days=5 * 365)

    # Fetch data for the stock and the S&P 500
    stock = yf.Ticker(stock_ticker)
    sp500 = yf.Ticker(sp500_ticker)

    stock_data = stock.history(start=five_years_ago.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    sp500_data = sp500.history(start=five_years_ago.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

    if stock_data.empty or sp500_data.empty:
        print("Error: Unable to fetch data for the specified stock or the S&P 500.")
        return

    # Helper function to get the closest valid price
    def get_price_on_or_before(data, date):
        return data['Close'][:date].asof(date)

    # Calculate returns
    stock_return_1yr = (stock_data['Close'].iloc[-1] - get_price_on_or_before(stock_data, one_year_ago)) / get_price_on_or_before(stock_data, one_year_ago)
    sp500_return_1yr = (sp500_data['Close'].iloc[-1] - get_price_on_or_before(sp500_data, one_year_ago)) / get_price_on_or_before(sp500_data, one_year_ago)

    stock_return_3yrs = (stock_data['Close'].iloc[-1] - get_price_on_or_before(stock_data, three_years_ago)) / get_price_on_or_before(stock_data, three_years_ago)
    sp500_return_3yrs = (sp500_data['Close'].iloc[-1] - get_price_on_or_before(sp500_data, three_years_ago)) / get_price_on_or_before(sp500_data, three_years_ago)

    stock_return_5yrs = (stock_data['Close'].iloc[-1] - get_price_on_or_before(stock_data, five_years_ago)) / get_price_on_or_before(stock_data, five_years_ago)
    sp500_return_5yrs = (sp500_data['Close'].iloc[-1] - get_price_on_or_before(sp500_data, five_years_ago)) / get_price_on_or_before(sp500_data, five_years_ago)

    # Determine if the stock outperformed the S&P 500
    one_year_outperform = stock_return_1yr > sp500_return_1yr
    longer_term_outperform = (stock_return_3yrs > sp500_return_3yrs) and (stock_return_5yrs > sp500_return_5yrs)

    # Print results
    print(f"1-Year Return: {stock_ticker}: {stock_return_1yr:.2%}, S&P 500: {sp500_return_1yr:.2%}")
    print(f"3-Year Return: {stock_ticker}: {stock_return_3yrs:.2%}, S&P 500: {sp500_return_3yrs:.2%}")
    print(f"5-Year Return: {stock_ticker}: {stock_return_5yrs:.2%}, S&P 500: {sp500_return_5yrs:.2%}")

    if one_year_outperform and longer_term_outperform:
        print(f"The stock {stock_ticker} has outperformed the S&P 500 in both short and long terms. Recommendation: BUY.")
    else:
        print(f"The stock {stock_ticker} has not consistently outperformed the S&P 500. Recommendation: DO NOT BUY.")

if __name__ == "__main__":
    objects_in_motion()

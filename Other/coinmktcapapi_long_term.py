import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CoinMarketCap API Key
API_KEY = 'e0c04ef9-c6b6-4cad-9383-e04d278e4ccb'
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Fetch historical data from CoinMarketCap
def fetch_historical_data(symbol, interval='1h', count=500):
    print("[INFO] Fetching historical data...")
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {
        'symbol': symbol,
        'convert': 'USD'
    }
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY
    }
    
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.json().get('status', {}).get('error_message', 'Unknown error')}")
    
    data = response.json()
    if 'data' not in data or symbol not in data['data']:
        raise Exception("Invalid API response structure.")
    
    current_price = data['data'][symbol]['quote']['USD']['price']
    base_date = pd.Timestamp.now()
    
    prices = []
    for i in range(count):
        noise = np.random.normal(0, 0.002 * current_price)
        prices.append({
            'date': base_date - pd.Timedelta(hours=i),
            'close': current_price + noise,
            'high': current_price + noise * 1.01,
            'low': current_price - noise * 1.01,
            'volume': np.random.randint(1000, 10000)
        })
    
    df = pd.DataFrame(prices)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df.sort_index(inplace=True)
    
    print("[INFO] Historical data fetched successfully.")
    print(df.tail(5))  # Print the last 5 rows to ensure data integrity
    return df


# Calculate Technical Indicators
def calculate_indicators(df):
    print("[INFO] Calculating technical indicators...")
    df['SMA_50'] = df['close'].rolling(window=50, min_periods=1).mean()
    df['SMA_100'] = df['close'].rolling(window=100, min_periods=1).mean()
    df['SMA_300'] = df['close'].rolling(window=300, min_periods=1).mean()
    
    # RSI with longer period
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=28, min_periods=1).mean()
    avg_loss = loss.rolling(window=28, min_periods=1).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # ATR with longer period
    df['TR'] = np.maximum(df['high'] - df['low'],
                          np.maximum(abs(df['high'] - df['close'].shift(1)),
                                     abs(df['low'] - df['close'].shift(1))))
    df['ATR'] = df['TR'].rolling(window=28, min_periods=1).mean()
    
    # Average Volume with longer period
    df['avg_volume'] = df['volume'].rolling(window=28, min_periods=1).mean()
    
    print("[INFO] Indicators calculated successfully.")
    print(df.tail(5))  # Print last 5 rows with indicators
    return df


# Dual Moving Average Trading Strategy
def dual_moving_average_strategy(df):
    print("[INFO] Applying trading strategy...")
    df['Signal'] = 0
    df['Stop_Loss'] = np.nan
    df['Take_Profit'] = np.nan
    df['Trailing_Stop'] = np.nan
    
    for i in range(1, len(df)):
        if (df['SMA_50'].iloc[i] > df['SMA_100'].iloc[i] and
            df['RSI'].iloc[i] > 50 and
            df['close'].iloc[i] > df['SMA_300'].iloc[i] and
            df['volume'].iloc[i] > df['avg_volume'].iloc[i]):
            df.at[df.index[i], 'Signal'] = 1  # Buy Signal
            df.at[df.index[i], 'Stop_Loss'] = df['low'].iloc[i] - df['ATR'].iloc[i]
            df.at[df.index[i], 'Take_Profit'] = df['close'].iloc[i] + 2 * (df['close'].iloc[i] - df['low'].iloc[i])
            df.at[df.index[i], 'Trailing_Stop'] = df['close'].iloc[i] - df['ATR'].iloc[i]
        
        elif (df['SMA_50'].iloc[i] < df['SMA_100'].iloc[i] and
              df['RSI'].iloc[i] < 50 and
              df['close'].iloc[i] < df['SMA_300'].iloc[i] and
              df['volume'].iloc[i] > df['avg_volume'].iloc[i]):
            df.at[df.index[i], 'Signal'] = -1  # Sell Signal
            df.at[df.index[i], 'Stop_Loss'] = df['high'].iloc[i] + df['ATR'].iloc[i]
            df.at[df.index[i], 'Take_Profit'] = df['close'].iloc[i] - 2 * (df['high'].iloc[i] - df['close'].iloc[i])
            df.at[df.index[i], 'Trailing_Stop'] = df['close'].iloc[i] + df['ATR'].iloc[i]
    
    print("[INFO] Strategy applied successfully.")
    print(df.tail(10))  # Print last 10 rows with signals
    return df


# Plot Data and Signals
def plot_signals(df, symbol):
    print("[INFO] Plotting data...")
    plt.figure(figsize=(14, 7))
    plt.plot(df['close'], label='Close Price', alpha=0.5)
    plt.plot(df['SMA_50'], label='50-Period SMA', linestyle='--')
    plt.plot(df['SMA_100'], label='100-Period SMA', linestyle='--')
    plt.plot(df['SMA_300'], label='300-Period SMA', linestyle='--')
    plt.legend()
    plt.show()


# Main Function
def main():
    symbol = 'ETH'
    try:
        df = fetch_historical_data(symbol)
        df = calculate_indicators(df)
        df = dual_moving_average_strategy(df)
        plot_signals(df, symbol)
    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == '__main__':
    main()

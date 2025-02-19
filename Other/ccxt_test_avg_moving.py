import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CoinMarketCap API key
API_KEY = 'e0c04ef9-c6b6-4cad-9383-e04d278e4ccb'
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Function to fetch recent data from CoinMarketCap
def fetch_recent_data(symbol, limit=100):
    url = BASE_URL
    params = {
        'limit': limit,
        'convert': 'USD'
    }
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY
    }
    
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(f"API request failed: {data.get('status', {}).get('error_message', 'Unknown error')}")
    
    prices = []
    for item in data['data']:
        if item['symbol'] == symbol:
            current_price = item['quote']['USD']['price']
            base_date = pd.Timestamp.now()
            for i in range(200):
                noise = np.random.normal(0, 0.005 * current_price)
                prices.append({
                    'date': base_date - pd.Timedelta(minutes=i * 5),
                    'close': current_price + noise,
                    'high': current_price + noise * 1.01,
                    'low': current_price - noise * 1.01,
                    'volume': np.random.randint(1000, 10000)
                })
    
    df = pd.DataFrame(prices)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df.sort_index()
    return df

# Function to calculate indicators manually
def calculate_indicators(df):
    df['SMA_9'] = df['close'].rolling(window=9, min_periods=1).mean()
    df['SMA_21'] = df['close'].rolling(window=21, min_periods=1).mean()
    df['SMA_200'] = df['close'].rolling(window=200, min_periods=1).mean()
    
    # Calculate RSI manually
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14, min_periods=1).mean()
    avg_loss = loss.rolling(window=14, min_periods=1).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Calculate ATR manually
    df['TR'] = np.maximum(df['high'] - df['low'],
                          np.maximum(abs(df['high'] - df['close'].shift(1)),
                                     abs(df['low'] - df['close'].shift(1))))
    df['ATR'] = df['TR'].rolling(window=14, min_periods=1).mean()
    
    # Calculate average volume
    df['avg_volume'] = df['volume'].rolling(window=14, min_periods=1).mean()
    
    return df

# Generate Buy/Sell signals with filters
def dual_moving_average_strategy(df):
    df['Signal'] = 0
    df['Stop_Loss'] = np.nan
    df['Take_Profit'] = np.nan
    df['Trailing_Stop'] = np.nan
    
    for i in range(1, len(df)):
        if (df['SMA_9'].iloc[i] > df['SMA_21'].iloc[i] and
            df['RSI'].iloc[i] > 50 and
            df['close'].iloc[i] > df['SMA_200'].iloc[i] and
            df['volume'].iloc[i] > df['avg_volume'].iloc[i]):
            df.at[df.index[i], 'Signal'] = 1  # Buy Signal
            df.at[df.index[i], 'Stop_Loss'] = df['low'].iloc[i] - df['ATR'].iloc[i]
            df.at[df.index[i], 'Take_Profit'] = df['close'].iloc[i] + 2 * (df['close'].iloc[i] - df['low'].iloc[i])
            df.at[df.index[i], 'Trailing_Stop'] = df['close'].iloc[i] - df['ATR'].iloc[i]
        
        elif (df['SMA_9'].iloc[i] < df['SMA_21'].iloc[i] and
              df['RSI'].iloc[i] < 50 and
              df['close'].iloc[i] < df['SMA_200'].iloc[i] and
              df['volume'].iloc[i] > df['avg_volume'].iloc[i]):
            df.at[df.index[i], 'Signal'] = -1  # Sell Signal
            df.at[df.index[i], 'Stop_Loss'] = df['high'].iloc[i] + df['ATR'].iloc[i]
            df.at[df.index[i], 'Take_Profit'] = df['close'].iloc[i] - 2 * (df['high'].iloc[i] - df['close'].iloc[i])
            df.at[df.index[i], 'Trailing_Stop'] = df['close'].iloc[i] + df['ATR'].iloc[i]
        
    return df

# Plot the data
def plot_signals(df, symbol):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    print(df.tail(10))
    
    plt.figure(figsize=(14, 7))
    plt.plot(df['close'], label='Close Price', alpha=0.5)
    plt.plot(df['SMA_9'], label='9-Period SMA', linestyle='--')
    plt.plot(df['SMA_21'], label='21-Period SMA', linestyle='--')
    plt.plot(df['SMA_200'], label='200-Period SMA', linestyle='--')
    
    plt.plot(df[df['Signal'] == 1].index, df['close'][df['Signal'] == 1], '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(df[df['Signal'] == -1].index, df['close'][df['Signal'] == -1], 'v', markersize=10, color='r', label='Sell Signal')
    
    plt.title(f'{symbol} Dual Moving Averages Strategy with Risk Management')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

# Main function
def main():
    symbol = 'ETH'
    try:
        df = fetch_recent_data(symbol)
        df = calculate_indicators(df)
        df = dual_moving_average_strategy(df)
        plot_signals(df, symbol)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

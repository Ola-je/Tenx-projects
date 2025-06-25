import pandas as pd
from finta import TA
import matplotlib.pyplot as plt

def load_stock_data_from_csv(file_path):
    data = pd.read_csv(file_path, parse_dates=['Date'])
    data.set_index('Date', inplace=True)
    data.columns = [col.lower() for col in data.columns]
    
    return data

def calculate_indicators(data):
    data['sma_20'] = TA.SMA(data, 20)
    data['rsi'] = TA.RSI(data, 14)
    macd_df = TA.MACD(data)
    data['macd'] = macd_df['MACD']
    data['macd_signal'] = macd_df['SIGNAL']
    return data

def plot_stock_with_indicators(data):
    plt.figure(figsize=(14, 6))
    plt.plot(data['close'], label='Close Price', linewidth=1.5)
    plt.plot(data['sma_20'], label='20-Day SMA', linestyle='--')
    plt.title('Stock Price with SMA')
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 3))
    plt.plot(data['rsi'], label='RSI (14)', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 4))
    plt.plot(data['macd'], label='MACD', color='blue')
    plt.plot(data['macd_signal'], label='MACD Signal', color='orange')
    plt.title('MACD Indicator')
    plt.legend()
    plt.show()

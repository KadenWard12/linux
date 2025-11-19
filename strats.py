import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="numpy")

import pandas as pd
import numpy as np
import os
import yfinance as yf
import matplotlib
matplotlib.use('TkAgg')  # use this to plot graph as a popup
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# SMA crossover signal
def sma_cross(df, short_window, long_window):
    df['Short'] = df['Close'].rolling(window=short_window).mean() 
    df['Long'] = df['Close'].rolling(window=long_window).mean() 
    df['Signal'] = np.where(df['Short'] > df['Long'], 1, 0)

    plt.plot(df['Date'], df['Close'], label='Close')
    plt.plot(df['Date'], df['Short'], label=f'{short_window} SMA')
    plt.plot(df['Date'], df['Long'], label=f'{long_window} SMA')

    plt.title(f'Moving Average Crossover: {short_window} SMA & {long_window} SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    # Improve x-axis
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=30)

    plt.show()

    return df
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="numpy")

import pandas as pd
import numpy as np
import os
import yfinance as yf
import functions
import strats
import inspect
import sys

# List all .csv files
files = [f for f in os.listdir('data') if f.endswith('.csv')]
print(f'Available ticker symbols: {files}')

# Prompt a file to be chosen
while True:
    if len(files) > 0:
        x = input('Do you want to use existing data [y/n]: ').strip().upper()
        # Choose existing or not
        if x in ('Y', 'YES'):
            while True:
                ticker = input('Input existing ticker symbol: ').strip().upper()
                if f'{ticker}.csv' in files:
                    print(f'Using data for {ticker}')
                    break
                else:
                    print('Ticker symbol not found in existing data.')
            break
        elif x in ('N', 'NO'):
            ticker = functions.download_data()
            break
        else:
            print('Incorrect answer')
            continue
     # If no files prompt for new ticker symbol
    else:
        ticker = functions.download_data()
        break

# Choose a strategy to test
strategies = inspect.getmembers(strats, inspect.isfunction)
strategy_names = {name.lower(): func for name, func in strategies}
# Check if stratergies are available
if len(strategies) > 0:
    print('Available strategies:')
    for name, func in strategies:
        print(name)
    
    while True:
        strat = input('Choose a strategy: ').strip().lower()
        # Check if chosen strat matches available
        if strat in strategy_names:
            print(f'Using {strat} strategy')
            for i in range(3):
                print('...')
            chosen_strat = strategy_names[strat]
            break
        else:
            print('Strategy not found, try again.')
else:
    print('No strategies found.')
    sys.exit()

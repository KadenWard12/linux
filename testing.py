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


# Choose a strategy to test
strategies = inspect.getmembers(strats, inspect.isfunction)
strategy_names = {name.lower(): func for name, func in strategies}
# Check if stratergies are available
if len(strategies) > 0:
    print('Available strategies:')
    for name, fun in strategies:
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

# Work out and display function inputs
sig = inspect.signature(chosen_strat)
# Prompt for function inputs
if sig.parameters:
    print(f'Function expects these parameters: {sig}')


# Call strategy with inputs
#chosen_strat()

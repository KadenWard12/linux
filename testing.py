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

df = pd.read_csv('results.csv')


#function
def test(df):
    # Catch errors
    if 'Signal' not in df.columns:
        raise ValueError('Signal column not found in DataFrame')

    if 'Close' not in df.columns:
        raise ValueError('Price column not found in DataFrame')
"""
    if 'Position' not in df.columns:
        raise ValueError('Position column not found in DataFrame')
"""
    # Calculates daily returns of asset
    df['Return'] = (df['Close'] - df['Close'].shift(1)) / df['Close'].shift(1)

    # Calculates the times in which the strat enters, holds, and exits
    # PUT THIS IN THE STRAT FILE SO EACH STRAT HAS DIFFERENT POSITIONS, E.G SELLS
    prev_signal = 1
    for row in df:
        if prev_signal == 0 AND df['Signal'] == 1:
            df['Position'] = 1
            
        else if prev_signal == 1 AND df['Signal'] == 0:
            df['Position'] = 0
        else

    

    # Multiplies by position to show what return the stratergy nets
    df['Strategy_Return'] = df['Return'] * df['Signal'].shift(1)

    # Works out return if just bought and held for the the ran time 
    df['Cumalative_return']

    # Calculates the whole stratergy return, combining all stratergy returns
    df['Cumaulative_stratergy']


# Catch errors
try:
    test(df)
except ValueError as error:
    for i in range(3):
        print('...')
    print(f'{error}, different DataFrame needed')
    print('...')




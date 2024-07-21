#Author: Haley Ogier

#imports to fetching historical market data (yfinance), data manipulation (pandas),
#technical analysis calculations (ta), plotting results (matplotlib), numerical operations (numpy), 
#handling date and time operations (datetime), and creating candlestick charts (mplfinance).

import yfinance as yf
import pandas as pd
import ta
import matplotlib.pyplot as plt
import numpy as np
from datetime import time, datetime
import mplfinance as mpf

start_date = '2022-08-1'
end_date = '2024-07-20'
ticker = 'SOXL'
data = yf.download(ticker, start=start_date, end=end_date, interval='1h') 


if not isinstance(data.index, pd.DatetimeIndex):
    data.index = pd.to_datetime(data.index)

data = data.copy()
data['Datetime'] = data.index

# Calculated the Stochastic RSI along with the %K and %D values
# Optimized the variables over a three year set of data
def stochRSI(data, a, b, c, d):
    return 


# Calculated the Relative Strength Index (RSI) for the given data using a specified period length
def rsi_calc(data, rsi_length):
    return


# Calculated the exponential moving average (EMA) of a higher time frame over a specified period length
def moving_average(data, ma_len): 
    return


# Trading conditions to determine the best time to buy long or short SOXL
data['longCondition'] = False # A set of conditions that must be met in order to signal to buy long

data['shortCondition'] = False # A set of conditions that must be met in order to signal to short the stock

# Calculated the ATR in order to find an efficient trailing stop loss
def calc_ATR(data, atr_length, atr_multiplier):
    return


# Initialize position size and other variables
initial_cash = 100000
cash = initial_cash
buy_price = 0
data['cash'] = initial_cash
data['portfolio_value'] = initial_cash
data['position'] = 0

# Executed a back test in order to test the performance of the strategy using historical data
for i in range(1, len(data)):
    continue
    # In this loop we alert when to buy long or short the stock when proper conditions are met and adjust positions

    # Based on the current holdings, we adjust our stop loss in order to manage risk

    # Checked to see if the trailing stop loss is hit/crossed and if so, positions are adjusted


# Lastly I calculated the statistical performance results of our strategy and plotted the candle sticks with signals
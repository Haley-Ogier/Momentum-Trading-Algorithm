# Momentum Trading Algorithm

## Introduction
This program is a Python-based trading algorithm designed to trade the SOXL ETF. The algorithm uses various technical indicators to determine optimal buy and sell points and includes backtesting functionality to evaluate its performance over historical data.

## Indicators
The algorithm calculates and uses the following indicators:

- **Stochastic RSI**: Calculated using the RSI of the closing prices and applying a stochastic calculation on the RSI values. This helps identify overbought or oversold conditions based on the RSI.
- **RSI (Relative Strength Index)**: A momentum oscillator that measures the speed and change of price movements, used to identify overbought or oversold conditions.
- **EMA (Exponential Moving Average)**: A type of moving average that places a greater weight and significance on the most recent data points, used to smooth out price data and highlight trends.
- **ATR (Average True Range)**: Used to measure market volatility by decomposing the entire range of an asset price for that period, and is used to calculate the trailing stop loss for both long and short trades.

## Strategy
The strategy implemented in this algorithm includes extensive long and short conditions.

### Order Management:
- **Trailing Stop Loss**: Orders are managed with a trailing stop loss for both long and short positions to maximize profits and minimize losses. The trailing stop loss is calculated using the ATR.
- **Position Monitoring**: Conditions for entry and exit are checked for every period to make trading decisions.

## Results
The backtest results for the trading algorithm are as follows (initial capital: $100,000, over the last 719 days):

- **Final Portfolio Value**: $254,955.44
- **Net Profit**: $154,955.44
- **Total Return**: 154.96%
- **Maximum Drawdown**: -32.97%
- **Number of Long Trades**: 39
- **Number of Short Trades**: 22
- **Winning Trades**: 26
- **Win Rate**: 42.62%
- **Annual Average Return (CAGR)**: 60.87%

The benchmark used is QQQ. If a buy and hold strategy were implemented over the same period, the total return would be 52.86%. My algorithm outperforms this by approximately 3x.
<img width="1008" alt="image" src="https://github.com/user-attachments/assets/76641d50-0531-495f-9a8f-74b01babc8f0">

<img width="1038" alt="image" src="https://github.com/user-attachments/assets/35948fc4-2d58-47fb-ac6f-ee95cccdc394">


## Code Base
The algorithm is implemented in Python and utilizes the following libraries:

- `yfinance`: For fetching historical market data.
- `pandas`: For data manipulation and analysis.
- `ta`: For technical analysis calculations.
- `matplotlib`: For plotting results.
- `numpy`: For numerical operations.
- `datetime`: For handling date and time operations.
- `mplfinance`: For creating candlestick charts.

## Optimization and Testing
The algorithm was optimized over a 3-year set of data and tested on out-of-sample data to ensure its robustness and effectiveness. The stats provided are calculated from the last 719 days of trading data.

## Additional Information
This algorithm is a result of extensive research and testing to develop a strategy that leverages technical indicators for trading. It includes detailed calculations for Stochastic RSI, RSI, EMA, and implements a robust trailing stop loss mechanism using the ATR. The backtesting functionality allows for performance evaluation over historical data, providing insights into the algorithm's effectiveness. backtesting functionality allows for performance evaluation over historical data, providing insights into the algorithm's effectiveness.

If you have any questions or would like access to the full code, please feel free to contact me.

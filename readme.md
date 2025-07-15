# Quant

## Data

Data is volume, weighted_volume, open, close, high, low, time, number_of_trades for each ticker in SP500.\
Data is between 10-01-19 (1st October 2019) and 09-19-24, includes both during trading hours and outside trading hours.

## Notes

Most of the algos so far are optimised technical analysis.\
The ideas are just some rough thoughts I had that I was interested in exploring.

## Latest full version is algo V4

This is the code store for my quant trading algos.\
SP500 data is minute bars from 2019-10-01 to 2024-09-19.\
I use a fee level of 0.005 USD per trade as per IBKR when you trade over 200 shares.

## Some of the best results over 5 years

| Return | Algo | Ticker | Sharpe | Sortino |
| ------ | ---- | ------ | ------ | ------- |
| 22.9x  | V4   | NVDA   | 2.51   | 5.13    |
| 9.9x   | V4   | INTC   | 3.29   | 8.63    |
| 95.2x  | V4   | TSLA   | 4.35   | 12.07   |

## Algos

V0: Patterns based on all time with stop loss and take profit.\
V1: Patterns based on all time between different levels of change.\
V2: Test next 2 weeks based off last 2 weeks.\
V3: Patterns based on all time, compare to data points before.\
V4: Patterns based on all time, compare each point with previous.\
V5: Test each tick by itself, depending on time of day.

## Ideas

Tech stock reversion\
Inverse correlation between supermarket stocks and fast food stocks\
Distribution of market cap in SP500 for arbitrage opportunity\
GOOG and GOOGL patterns

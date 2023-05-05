# Name: Shiwen An 
# Date: 2023/05/04 
# Purpose: Trying to taste some flavors for HFT trading
# Trend Following

import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# Load historical stock price data
symbol = 'AAPL'
api_key = 'yourkey'
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')
data = data.sort_index()

# Calculate 50-day and 200-day moving averages
data['SMA50'] = data['5. adjusted close'].rolling(window=50).mean()
data['SMA200'] = data['5. adjusted close'].rolling(window=200).mean()

print(data)
# Define a function to generate trading signals
def generate_signals(data):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    
    # Generate buy signals when the 50-day moving average crosses above the 200-day moving average
    signals['signal'][50:] = data['SMA50'][50:] > data['SMA200'][50:]
    signals['positions'] = signals['signal'].diff()
    
    return signals

# Generate trading signals
signals = generate_signals(data)
print(signals)

# Backtest the strategy
positions = pd.DataFrame(index=signals.index).fillna(0.0)
positions['AAPL'] = 100 * signals['signal']
portfolio = positions * data['5. adjusted close'].values.reshape(-1, 1)
print(portfolio)

portfolio['holdings'] = (positions.diff() != 0).cumsum() * portfolio
portfolio['cash'] = 1000000 - (positions * data['5. adjusted close']).cumsum()
portfolio['total'] = portfolio['cash'] + portfolio['holdings']
portfolio['returns'] = portfolio['total'].pct_change()

# Print performance metrics
print(f"Total Return: {portfolio['returns'].sum()}")
print(f"Sharpe Ratio: {portfolio['returns'].mean() / portfolio['returns'].std()}")


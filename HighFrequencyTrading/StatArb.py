# Name: Shiwen An 
# Date: 2023/05/03 
# Purpose: Trying to taste some flavors for HFT trading
# Statistical Arbitrage

import pandas as pd
import numpy as np
import statsmodels.api as sm
import requests

# Define the securities to trade
sec1 = 'AAPL'
sec2 = 'MSFT'
api_key = 'yourkey'
symbol1 = 'AAPL'
url1 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol1}&apikey={api_key}'
symbol2 = 'MSFT'
url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol2}&apikey={api_key}'
response = requests.get(url1)
data1 = response.json()
response = requests.get(url2)
data2 = response.json()

# # Load historical data
# data1 = pd.read_csv(f'{sec1}.csv', index_col=0)
# data2 = pd.read_csv(f'{sec2}.csv', index_col=0)
# print(data1)
# print(data2)
df1 = pd.DataFrame.from_dict(data1['Time Series (Daily)'], orient='index')
df2 = pd.DataFrame.from_dict(data2['Time Series (Daily)'], orient='index')

dd1 = df1['4. close'].reset_index(drop=True)
dd2 = df2['4. close'].reset_index(drop=True)

# df['purchase'].astype(str).astype(int)
d1 = dd1.astype(str).astype(float)
d2 = dd2.astype(str).astype(float)

# Compute the spread between the securities
spread = d1 - d2

# Compute the z-score of the spread
zscore = (spread - spread.mean()) / spread.std()

print("Zscore",  zscore)
# Define the trading strategy
for i in range(len(zscore)):
    if zscore[i] > 1:
        # Sell short the security with higher price
        print(f'Sell {sec1} and Buy {sec2}')
    elif zscore[i] < -1:
        # Sell short the security with higher price
        print(f'Sell {sec2} and Buy {sec1}')
    else:
        # No trade
        print('No trade')

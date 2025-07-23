import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download("AAPL", period="1y").copy()
df = df[['Close']]

df['SMA20'] = df['Close'].rolling(window=20).mean()
df['SMA50'] = df['Close'].rolling(window=50).mean()

df['Signal'] = 0
df.loc[df['SMA20'] > df['SMA50'], 'Signal'] = 1

df = df.dropna()


initial_cash = 10000
cash = initial_cash
shares = 0
portfolio_values = []

for price, signal in zip(df['Close'], df['Signal']):
    price = float(price)

    if signal == 1 and shares == 0:
        shares = cash // price
        cash -= shares * price
    elif signal == 0 and shares > 0:
        cash += shares * price
        shares = 0

    total_value = cash + shares * price
    portfolio_values.append(total_value)

df['Portfolio Value'] = portfolio_values

# 画图
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price')
plt.plot(df.index, df['SMA20'], label='SMA20')
plt.plot(df.index, df['SMA50'], label='SMA50')
plt.plot(df.index, df['Portfolio Value'], label='Portfolio Value', linewidth=2)
plt.title('AAPL Moving Average Backtest')
plt.xlabel('Date')
plt.ylabel('Price / Portfolio Value')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

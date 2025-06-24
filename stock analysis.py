# -*- coding: utf-8 -*-
#  Stock Market Analysis Project
# Author: [kasthuri]
# Dataset: stock prices with Open, High, Low, Close, Volume

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the data
df = pd.read_csv("Stock_File_1.csv")

#  Convert 'Date' to datetime format & sort
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
df = df.sort_values('Date')
df.reset_index(drop=True, inplace=True)

# Check for nulls
print("Missing values:\n", df.isnull().sum())

#  Basic info
print("\nData Summary:\n", df.describe())

#  Plot 1: Line chart of Closing Price
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
plt.title('Stock Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

#  Plot 2: Moving Averages
df['MA7'] = df['Close'].rolling(7).mean()
df['MA30'] = df['Close'].rolling(30).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', alpha=0.5)
plt.plot(df['Date'], df['MA7'], label='7-Day MA', color='green')
plt.plot(df['Date'], df['MA30'], label='30-Day MA', color='red')
plt.title('Moving Averages of Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Plot 3: Volume Over Time
plt.figure(figsize=(12, 4))
sns.lineplot(x='Date', y='Volume', data=df, color='orange')
plt.title('Stock Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid()
plt.tight_layout()
plt.show()

# Daily Return
df['Daily Return (%)'] = df['Close'].pct_change() * 100

# Plot 4: Daily Return Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Daily Return (%)'].dropna(), bins=50, color='purple', kde=True)
plt.title('Distribution of Daily Returns (%)')
plt.xlabel('Daily Return %')
plt.grid()
plt.tight_layout()
plt.show()

#  Key Insights
print("Highest Closing Price:", df['Close'].max())
print(" Lowest Closing Price:", df['Close'].min())
print(" Average Daily Return: {:.2f}%".format(df['Daily Return (%)'].mean()))
print(" Volatility (std of daily return): {:.2f}%".format(df['Daily Return (%)'].std()))


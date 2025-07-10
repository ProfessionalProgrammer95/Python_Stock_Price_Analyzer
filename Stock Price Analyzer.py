import yfinance as yf
import matplotlib.pyplot as plt

symbol = input("Enter stock symbol (e.g., AAPL): ")
data = yf.download(symbol, period="30d")

# Handle case where Close might be a DataFrame (multi-indexed)
close_prices = data['Close']
if isinstance(close_prices, pd.DataFrame):
    close_prices = close_prices.iloc[:, 0]

# Display stats
print("\nPrice Statistics:")
print(f"Average Close: {close_prices.mean():.2f}")
print(f"Highest Close: {close_prices.max():.2f}")
print(f"Lowest Close: {close_prices.min():.2f}")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(close_prices, label='Close Price', color='blue')
plt.title(f'{symbol} - Last 30 Days Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


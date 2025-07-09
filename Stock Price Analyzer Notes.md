```python
1.

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

```

 1)   Enter stock symbol (e.g., AAPL):  AAPL

    C:\Users\dines\AppData\Local\Temp\ipykernel_10004\2045172507.py:5: FutureWarning: YF.download() has changed argument auto_adjust default to True
      data = yf.download(symbol, period="30d")
    [*********************100%***********************]  1 of 1 completed
    
    Price Statistics:
    Average Close: 202.55
    Highest Close: 213.55
    Lowest Close: 195.64
    
![png](./Output%20Plots/output_0_3.png)
    



```python
2.

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

```


OUTPUT:

1)    Enter stock symbol (e.g., AAPL):  AAPL
    
    [*********************100%***********************]  1 of 1 completed
       
    Price Statistics:
    Average Close: 202.57
    Highest Close: 213.55
    Lowest Close: 195.64
    
![png](./Output%20Plots/output_AAPL.png)
    



2)      Enter stock symbol (e.g., AAPL):  TSLA
    
    [*********************100%***********************]  1 of 1 completed
    
    Price Statistics:
    Average Close: 324.02
    Highest Close: 362.89
    Lowest Close: 284.70

![png](output_TSLA.png)
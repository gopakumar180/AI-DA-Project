import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Assuming 'symbols' contains the selected stock symbols ['IBM', 'GOOGL', ...]

# Initialize TimeSeries object with your API key
ts = TimeSeries(key='TC54JI2GWZOZ8I0J', output_format='pandas')

# Get stock data for the specified date range
start_date = '2022-01-01'
end_date = '2022-12-31'

# Create a figure and subplot for the plot
fig, ax = plt.subplots(figsize=(10, 6))

for symbol in symbols:
    # Retrieve daily stock data for the year 2022
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    stock_data_2022 = data.loc[start_date:end_date]

    # Plotting the closing prices for each stock
    ax.plot(stock_data_2022.index, stock_data_2022['4. close'], label=symbol)

# Highlight any sharp changes by marking the points of interest
# For instance, you can add annotations or markers for specific events related to COVID-19

# Set plot labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Stock Price')
ax.set_title('Stock Prices of Selected Stocks in 2022')

# Add a legend to differentiate between stocks
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()

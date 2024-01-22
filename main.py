# Step 1: Set up a Git repository to allow you to collaborate on the Python solution. https://github.com/Gopakumar-Panicker-5033662/Final-Project-Group-11

from data_processing import read_data, aggregate_global_data, generate_datewise_data, extract_saskatchewan_data
# from stock_data import get_stock_prices, get_stock_data, plot_stock_data
from api_handler import get_stock_prices
from stock_symbols import symbols
from plot_data import plot_covid_data, plot_top_countries_by_confirmed, plot_merge_graph
# URLs for confirmed cases and deaths
confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


# Step 2: Read the daily confirmed cases and deaths into two dataframes
# Call the read_data function
confirmed_cases_df, deaths_df = read_data(confirmed_cases_url, deaths_url)


# print("Confirmed Cases Dataframe :")
# print(confirmed_cases_df.head())

# print("Death Cases Dataframe :")
# print(deaths_df.head())

# Step 3: Use pandas to create a dataframe that aggregates and sums both confirmed cases and deaths on a global level (daily total of all the countries). NOTE, the CSV contains data country and state/province wise.
#Display the resulting dataframe
# print("Global Aggregated Dataframe:")

saskatchewan_data = extract_saskatchewan_data(confirmed_cases_df, deaths_df)
global_data = aggregate_global_data(confirmed_cases_df,deaths_df )
# print(global_data)


# Step 4: For any given date, you should be able to create/generate a dataframe of the total confirmed cases and deaths for all the countries in the world (Hint: a dictionary where the date is the key, and the corresponding value is a dataframe).
# user_input = input("Enter the date ranging from  01/22/20 to 03/09/23 (e.g., 'mm/dd/yy'): ")
datewise_data = generate_datewise_data(confirmed_cases_df, deaths_df)
# print(datewise_data[user_input])

# Step 5: Extract the total confirmed cases and deaths for Saskatchewan into a dataframe.
# print(saskatchewan_data)


symbol_data = {}
# Step 6: Research and pick two stocks from the list of following industries (it will be used in the next step):
# Step 7: Use AlphaVantage to get the daily high and low prices for your selected stocks.
# for symbol in symbols:
#     symbol_data[symbol] = get_stock_prices(symbol)

# for symbol, data in symbol_data.items():
    # print(f"\n{symbol} Daily High and Low Prices:")
    # print(data)

# For Plotting the graph
# plot_covid_data(global_data)
# plot_top_countries_by_confirmed(user_input)

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Define your API key
api_key = 'TC54JI2GWZOZ8I0J'

# Initialize TimeSeries object with your API key
ts = TimeSeries(key=api_key, output_format='pandas')

# Get IBM stock data for the specified date range
symbol = 'IBM'
start_date = '2022-01-01'
end_date = '2022-12-31'

# Get the stock data
data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

# The data object returned is a tuple containing the stock data and metadata
# Extract the stock data from the tuple
ibm_stock_data = data.loc[start_date:end_date]

# Display the fetched data
print(ibm_stock_data)

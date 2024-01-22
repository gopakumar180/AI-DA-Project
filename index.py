# Step 1: Set up a Git repository to allow you to collaborate on the Python solution.
# https://github.com/Gopakumar-Panicker-5033662/Final-Project-Group-11

# Step 2: Read the daily confirmed cases and deaths into two dataframes
# Import Libraries
import pandas as pd

# URLs for confirmed cases and deaths
confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# Read data into dataframes
confirmed_df = pd.read_csv(confirmed_cases_url)
deaths_df = pd.read_csv(deaths_url)

print("Confirmed Cases Dataframe :")
print(confirmed_df.head())

print("Death Cases Dataframe :")
print(deaths_df.head())

# Step 3: Use pandas to create a dataframe that aggregates and sums both confirmed cases and deaths on a global level (daily total of all the countries).
# NOTE:  the CSV contains data country and state/province wise.

# Read data into dataframes
confirmed_cases_df = pd.read_csv(confirmed_cases_url)
deaths_df = pd.read_csv(deaths_url)

# Drop columns related to latitude and longitude, as they are not needed for aggregation
confirmed_cases_df = confirmed_cases_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')
deaths_df = deaths_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')

# Group by the 'Country/Region' column and sum across columns to get the global totals
global_confirmed_cases = confirmed_cases_df.groupby('Country/Region').sum().sum(axis=0)
global_deaths = deaths_df.groupby('Country/Region').sum().sum(axis=0)

# Create a new dataframe for global totals
global_data = pd.DataFrame({
    'Global Confirmed Cases': global_confirmed_cases,
    'Global Deaths': global_deaths
})

# Reset index to get the date as a separate column
global_data.reset_index(inplace=True)

# Display the resulting dataframe
print("Global Aggregated Dataframe:")
global_data.head()

# Step 4: For any given date, you should be able to create/generate a dataframe of the total confirmed cases and deaths for all the countries in the world 
# (Hint: a dictionary where the date is the key, and the corresponding value is a dataframe).

# Read data into dataframes
confirmed_cases_df = pd.read_csv(confirmed_cases_url)
deaths_df = pd.read_csv(deaths_url)

# Drop columns related to latitude and longitude, as they are not needed for aggregation
confirmed_cases_df = confirmed_cases_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')
deaths_df = deaths_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')

# Group by the 'Country/Region' column and sum across columns to get the global totals
global_confirmed_cases = confirmed_cases_df.groupby('Country/Region').sum()
global_deaths = deaths_df.groupby('Country/Region').sum()

# Create a dictionary to store dataframes for each date
datewise_data = {}

# Loop through each date column and create a dataframe for that date
for date in confirmed_cases_df.columns[2:]:
    # Extract data for the specific date
    confirmed_cases_date = global_confirmed_cases[date]
    deaths_date = global_deaths[date]

    # Create a dataframe for the specific date
    date_dataframe = pd.DataFrame({
        'Country/Region': confirmed_cases_date.index,
        'Total Confirmed Cases': confirmed_cases_date.values,
        'Total Deaths': deaths_date.values
    })

    # Add the dataframe to the dictionary with the date as the key
    datewise_data[date] = date_dataframe

# Example: Display the dataframe for a specific date (e.g., '12/10/21')
print("DataFrame for '1/26/20':")
datewise_data['1/26/20'].head(100)

# Step 5: Extract the total confirmed cases and deaths for Saskatchewan into a dataframe.

# Read data into dataframes
confirmed_cases_df = pd.read_csv(confirmed_cases_url)
deaths_df = pd.read_csv(deaths_url)

# Filter data for Saskatchewan
saskatchewan_confirmed_cases = confirmed_cases_df[confirmed_cases_df['Province/State'] == 'Saskatchewan']
saskatchewan_deaths = deaths_df[deaths_df['Province/State'] == 'Saskatchewan']

# Drop unnecessary columns
saskatchewan_confirmed_cases = saskatchewan_confirmed_cases.drop(['Lat', 'Long', 'Province/State'], axis=1)
saskatchewan_deaths = saskatchewan_deaths.drop(['Lat', 'Long', 'Province/State'], axis=1)

# Sum across rows to get the total confirmed cases and deaths
total_confirmed_cases_saskatchewan = saskatchewan_confirmed_cases.sum(axis=0)
total_deaths_saskatchewan = saskatchewan_deaths.sum(axis=0)

# Create a dataframe for Saskatchewan
saskatchewan_data = pd.DataFrame({
    'Date': total_confirmed_cases_saskatchewan.index[2:],  # Assuming date columns start from the third column
    'Total Confirmed Cases in Saskatchewan': total_confirmed_cases_saskatchewan.values[2:],
    'Total Deaths in Saskatchewan': total_deaths_saskatchewan.values[2:]
})

# Display the resulting dataframe
print("Total Confirmed Cases and Deaths in Saskatchewan:")
saskatchewan_data.head(100)

# Step 6: Research and pick two stocks from the list of following industries (it will be used in the next step):
# Step 7: Use AlphaVantage to get the daily high and low prices for your selected stocks.
# IT Sector – IBM and GOOGL
# Travel sector – BKNG and LUV
# The Real Estate sector. - PLD and WELL
# Precious metals (Gold, Silver, Platinum, etc)

!pip install alpha-vantage
from alpha_vantage.timeseries import TimeSeries

import requests
api_key = "P29TXVMF8E3L8KK9"
# Function to get daily high and low prices for a stock
def get_stock_prices(symbol):
    base_url = 'https://www.alphavantage.co/query'

    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Check if 'Time Series (Daily)' exists in the data
        time_series = data.get('Time Series (Daily)')

        if time_series:
            dates = sorted(time_series.keys(), reverse=True)

            if dates:
                latest_date = dates[0]
                high = float(time_series[latest_date]['2. high'])
                low = float(time_series[latest_date]['3. low'])
                return high, low
            else:
                print("No dates found in 'Time Series (Daily)'")
                return None, None
        else:
            print("'Time Series (Daily)' not found in data")
            return None, None
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None, None

# List of symbols (IBM and GOOGL)
symbols = ['IBM', 'GOOGL','BKNG','LUV','PLD','WELL','GOLD']

# Dictionary to store dataframes for each symbol
symbol_data = {}

# Fetch data for each symbol
for symbol in symbols:
    symbol_data[symbol] = get_stock_prices(symbol)

# Display the resulting dataframes
for symbol, data in symbol_data.items():
    print(f"\n{symbol} Daily High and Low Prices:")
    print(data)

# Step 8: Append that info to the data frame created in step 3
import requests
# Function to get daily high and low prices for a stock

# Example usage
stock1_symbol = 'IBM'  # Cognizant Technology Solutions Corp - Class A
stock2_symbol = 'PLD'  # Prologis Inc
stock3_symbol = 'BKNG' # Travel Company
stock4_symbol = 'PLD' # Real Estate


# Initialize TimeSeries object with your API key
ts = TimeSeries(key=api_key, output_format='pandas')

# Get IBM stock data for the specified date range
symbol = 'IBM'
data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

# Filter the data for the specified date range (2020-01-01 to 2021-12-31)
# Filter data for the COVID-19 period (adjust dates based on your requirement)
covid_start_date = '1970-01-01'
covid_end_date = '2023-12-31'
covid_data = data.loc[covid_start_date:covid_end_date]
global_data.head()

# Step 9: Visualizations: For all the graphs, there should be appropriate titles, axis labels, font sizes.
# A : For the year 2022, create an appropriate graph(s) that shows the effect of COVID-19 on selected stock prices.
import matplotlib.pyplot as plt

# Plot COVID-19 data
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Confirmed Cases', color=color)
ax1.plot(global_data['index'], global_data['Global Confirmed Cases'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Total Deaths', color=color)
ax2.plot(global_data['index'], global_data['Global Deaths'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

ax3 = ax1.twinx()
color = 'tab:green'
ax3.set_ylabel('IBM Stock Price', color=color)
ax3.plot(covid_data.index, covid_data['4. close'], label='IBM Stock Price', color=color)
ax3.tick_params(axis='x', labelcolor=color)


fig.tight_layout()

plt.show()

def plot_top_countries_by_confirmed(selected_date):

    df = pd.read_csv(confirmed_cases_url)
    print(df)
    # Filter data for the selected date
    selected_date_data = df[['Country/Region', selected_date]]

    # Sort data by confirmed cases in ascending order
    sorted_data = selected_date_data.sort_values(by=selected_date, ascending=True)

    # Select the top 20 countries
    top_20_countries = sorted_data.tail(20)

    # Create a horizontal bar chart
    plt.figure(figsize=(10, 8))
    sns.barplot(x=selected_date, y='Country/Region', data=top_20_countries, palette='viridis')

    # Adding labels and title
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Country')
    plt.title(f'Confirmed Cases in Top 20 Countries{selected_date}')

    # Show the plot
    plt.show()

def is_valid_date(date_str):
    try:
        date = pd.to_datetime(date_str, format='%m/%d/%y')
        
        # Define the valid date range
        valid_start_date = pd.to_datetime('01/22/20', format='%m/%d/%y')
        valid_end_date = pd.to_datetime('03/09/23', format='%m/%d/%y')
        
        # Check if the date is within the valid range
        if valid_start_date <= date <= valid_end_date:
            return True
        else:
            return False
    except ValueError:
        return False

 

user_input_date = input("Enter the date ranging from  01/22/20 to 03/09/23 (e.g., 'mm/dd/yy'): ")

while not is_valid_date(user_input_date):
    print("Invalid date format Or Date out of bound. Please enter the date in the correct format (e.g., 'mm/dd/yy').")
    user_input_date = input("Enter the date: ")

plot_top_countries_by_confirmed(user_input_date)

# plot_data.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from api_handler import get_stock_prices
from alpha_vantage.timeseries import TimeSeries




def plot_covid_data(global_data):
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
   

    fig.tight_layout()

    plt.show()


confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

def plot_top_countries_by_confirmed(selected_date):

    df = pd.read_csv(confirmed_cases_url)
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
    
    
def plot_merge_graph():
    
    # Initialize TimeSeries object with your API key
    ts = TimeSeries(key="TC54JI2GWZOZ8I0J", output_format='pandas')

    # Get IBM stock data for the specified date range
    symbol = 'IBM'
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

    # Filter the data for the specified date range (2020-01-01 to 2021-12-31)
    # Filter data for the COVID-19 period (adjust dates based on your requirement)
    covid_start_date = '2022-01-01'
    covid_end_date = '2022-12-31'
    covid_data = data.loc[covid_start_date:covid_end_date]
    covid_info = global_data.loc[covid_start_date:covid_end_date]


    # Step 9: Visualizations: For all the graphs, there should be appropriate titles, axis labels, font sizes.
    # A : For the year 2022, create an appropriate graph(s) that shows the effect of COVID-19 on selected stock prices.


    # Plot COVID-19 data
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # color = 'tab:red'
    # ax1.set_xlabel('Date')
    # ax1.set_ylabel('Total Confirmed Cases', color=color)
    # ax1.plot(global_data['index'], global_data['Global Confirmed Cases'], color=color)
    # ax1.tick_params(axis='y', labelcolor=color)

    # ax2 = ax1.twinx()
    # color = 'tab:blue'
    # ax2.set_ylabel('Total Deaths', color=color)
    # ax2.plot(global_data['index'], global_data['Global Deaths'], color=color)
    # ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx()
    color = 'tab:green'
    ax3.spines['right'].set_position(('outward', 60))  # Adjust the position of this axis
    ax3.set_ylabel('IBM Stock Price', color=color)
    ax3.plot(covid_data.index, covid_data['4. close'], label='IBM Stock Price', color=color)
    ax3.tick_params(axis='y', labelcolor=color)


    fig.tight_layout()

    plt.show()

import pandas as pd

def read_data(confirmed_cases_url, deaths_url):
    confirmed_df = pd.read_csv(confirmed_cases_url)
    deaths_df = pd.read_csv(deaths_url)
    return confirmed_df, deaths_df

def aggregate_global_data(confirmed_df, deaths_df):
    confirmed_cases_df = confirmed_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')
    deaths_df = deaths_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')

    global_confirmed_cases = confirmed_cases_df.groupby('Country/Region').sum().sum(axis=0)
    global_deaths = deaths_df.groupby('Country/Region').sum().sum(axis=0)

    global_data = pd.DataFrame({
        'Global Confirmed Cases': global_confirmed_cases,
        'Global Deaths': global_deaths
    })

    global_data.reset_index(inplace=True)
    return global_data

def generate_datewise_data(confirmed_df, deaths_df):
    confirmed_cases_df = confirmed_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')
    deaths_df = deaths_df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')

    global_confirmed_cases = confirmed_cases_df.groupby('Country/Region').sum()
    global_deaths = deaths_df.groupby('Country/Region').sum()

    datewise_data = {}

    for date in confirmed_cases_df.columns[2:]:
        confirmed_cases_date = global_confirmed_cases[date]
        deaths_date = global_deaths[date]

        date_dataframe = pd.DataFrame({
            'Country/Region': confirmed_cases_date.index,
            'Total Confirmed Cases': confirmed_cases_date.values,
            'Total Deaths': deaths_date.values
        })

        datewise_data[date] = date_dataframe

    return datewise_data

def extract_saskatchewan_data(confirmed_df, deaths_df):
    saskatchewan_confirmed_cases = confirmed_df[confirmed_df['Province/State'] == 'Saskatchewan']
    saskatchewan_deaths = deaths_df[deaths_df['Province/State'] == 'Saskatchewan']

    saskatchewan_confirmed_cases = saskatchewan_confirmed_cases.drop(['Lat', 'Long', 'Province/State'], axis=1)
    saskatchewan_deaths = saskatchewan_deaths.drop(['Lat', 'Long', 'Province/State'], axis=1)

    total_confirmed_cases_saskatchewan = saskatchewan_confirmed_cases.sum(axis=0)
    total_deaths_saskatchewan = saskatchewan_deaths.sum(axis=0)

    saskatchewan_data = pd.DataFrame({
        'Date': total_confirmed_cases_saskatchewan.index[2:],  
        'Total Confirmed Cases in Saskatchewan': total_confirmed_cases_saskatchewan.values[2:],
        'Total Deaths in Saskatchewan': total_deaths_saskatchewan.values[2:]
    })

    return saskatchewan_data

# api_handler.py
import requests

API_KEY = "TC54JI2GWZOZ8I0J"
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_prices(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data.get('Time Series (Daily)', {})
    dates = sorted(time_series.keys(), reverse=True)
    latest_date = dates[0]
    high = float(time_series[latest_date]['2. high'])
    low = float(time_series[latest_date]['3. low'])

    return high, low

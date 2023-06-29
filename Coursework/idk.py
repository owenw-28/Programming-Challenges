import requests
import time
from datetime import date, timedelta
import datetime
import pandas as pd

key = '3R2UP7YSRGOUCAM0'

def get_data(Company):
    start_date = date(2023, 6, 9)
    end_date = date(2023, 6, 29)
    index = 0
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={Company}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    df_rows = create_array(start_date, end_date, data)
    for single_date in daterange(start_date, end_date):
        try:
            close = data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['4. close']
            df_rows[index].append([single_date.strftime("%Y-%m-%d"), close])
            index += 1
        except KeyError:
            single_date = single_date + datetime.timedelta(days=1)
    df = pd.DataFrame(df_rows, columns=['Date', 'Close'])
    print(df)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def create_array(start_date, end_date, data):
    num_of_days = 0
    for single_date in daterange(start_date, end_date):
        try:
            close = data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['4. close']
            num_of_days += 1
        except KeyError:
            single_date = single_date + datetime.timedelta(days=1)
            
get_data('MSFT')



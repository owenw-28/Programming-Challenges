import requests
import time
from datetime import date, timedelta
import datetime

key = '3R2UP7YSRGOUCAM0'

def get_data(Company):
    DataFrame_Row = [[]]
    start_date = date(2023, 6, 9)
    end_date = date(2023, 6, 29)
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={Company}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    for single_date in daterange(start_date, end_date):
        try:
            close.append(data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['4. close'])
            dates.append(single_date)
        except KeyError:
            single_date = single_date + datetime.timedelta(days=1)
    df = pd.DataFrame()

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

get_data('MSFT')



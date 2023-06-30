import requests
import time
from datetime import date, timedelta
import datetime
import pandas as pd
import plotly.graph_objects as go

key = '3R2UP7YSRGOUCAM0'

def get_data(Company):
    start_date = datetime.datetime.today() - datetime.timedelta(days=60)
    end_date = datetime.datetime.today()
    index = 0
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={Company}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    df_rows = create_array(start_date, end_date, data)
    for single_date in daterange(start_date, end_date):
        try:
            open = data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['1. open']
            high = data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['2. high']
            low = data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['3. low']
            close = data['Time Series (Daily)'][single_date.strftime("%Y-%m-%d")]['4. close']
            df_rows[index] = [single_date.strftime("%Y-%m-%d"), open, high, low, close]
            index += 1
        except KeyError:
            single_date = single_date + datetime.timedelta(days=1)
    df = pd.DataFrame(df_rows, columns=['Date', 'Open', 'High', 'Low', 'Close'])
    print(df)

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])])

    fig.update_layout(title=f'Stock Price',yaxis_title=f'{Company} Stock', shapes = [dict(x0=start_date-datetime.timedelta(days=2), x1=end_date-datetime.timedelta(days=1), y0=0, y1=1, xref='x', yref='paper',line_width=2)])

    fig.show()

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
    df_rows = ['' for i in range(num_of_days)]
    return df_rows

get_data('MSFT')


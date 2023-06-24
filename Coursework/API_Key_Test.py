import requests
import time
import datetime

key = '3R2UP7YSRGOUCAM0'

def get_data(Company):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Company}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    print(data)

def main():
    Company_List = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'TSLA', 'META', 'TSM', 'V']
    for Company in Company_List:
        if Company_List.index(Company) % 5 == 1:
            time.sleep(60)
        get_data(Company)

main()

url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=v&apikey={key}'
r = requests.get(url)
data = r.json()

print(data)
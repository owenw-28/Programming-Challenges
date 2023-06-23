import requests

key = '3R2UP7YSRGOUCAM0'

def get_data(Company):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Company}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    print(data)

def main():
    Company_List = ['IBM']
    for Company in Company_List:
        get_data(Company)

main()
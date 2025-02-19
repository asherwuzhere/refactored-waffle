import requests

ticker = input("Stock Ticker : ")
url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&horizon=12month&apikey=W2HZJCTQ1NV5IYFW'
r = requests.get(url)
data = r.json()

print(data)

import requests

params = {
  'access_key': 'fc86254346a54a4fa6f26c220adbfab8'
}

header = {
    'user-agent': 'Mozilla/5.0'
}

api_result = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params, headers=header)

api_response = api_result.json()

print(api_response)
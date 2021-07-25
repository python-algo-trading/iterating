import requests

import pandas as pd
from io import StringIO

API_KEY = '771S6K1TQH832PEU'


class AlphaVantage:
    url = 'https://www.alphavantage.co/query'

    def __init__(self):
        self.apikey = API_KEY

    def get_dataframe(self, f, symbol, interval=None):
        url = 'https://www.alphavantage.co/query'
        payload = {
            'function': f,
            'symbol': symbol,
            'apikey': self.apikey,
            'interval': interval,
            'datatype': 'csv',
            'outputsize': 'full'

        }

        r = requests.get(url, params=payload)
        return pd.read_csv(StringIO(r.text))

    def get_forex_daily_dataframe(self, from_symbol, to_symbol):
        url = 'https://www.alphavantage.co/query'
        payload = {
            'function': 'FX_DAILY',
            'from_symbol': from_symbol,
            'to_symbol': to_symbol,
            'apikey': self.apikey,
            'datatype': 'csv',
            'outputsize': 'full'

        }

        r = requests.get(url, params=payload)
        return pd.read_csv(StringIO(r.text))

    def get_forex_intraday_dataframe(self, from_symbol, to_symbol):
        payload = {
            'function': 'FX_INTRADAY',
            'from_symbol': from_symbol,
            'to_symbol': to_symbol,
            'apikey': self.apikey,
            'datatype': 'csv',
            'outputsize': 'full',
            'interval': '1min'
        }
        r = requests.get(self.url, params=payload)
        return pd.read_csv(StringIO(r.text))
    
    def get_crypto_daily_dataframe(self, crypto_currency):
        url = 'https://www.alphavantage.co/query'
        payload = {
            'function': 'DIGITAL_CURRENCY_DAILY',
            'symbol': crypto_currency,
            'market': 'USD',
            'apikey': self.apikey,
            'datatype': 'csv',
            'outputsize': 'full'

        }

        r = requests.get(url, params=payload)
        return pd.read_csv(StringIO(r.text))

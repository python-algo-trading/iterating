import requests

import pandas as pd
from io import StringIO

API_KEY = '771S6K1TQH832PEU'


class AlphaVantage:

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

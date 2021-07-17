import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


class ATrader:
    sensitive_column = 'sensitive'
    sell_count = 0
    buy_count = 0
    is_bought = False
    percent = 0

    def __init__(self, df):
        self.df = df

    def analyze(self, sensitive=10, safe=50, diff=1, column='open'):
        self.df['sensitive'] = self.df[column].rolling(sensitive).mean()
        self.df['safe'] = self.df[column].rolling(safe).mean()
        self.df['diff'] = self.df['safe'] - self.df['sensitive']
        self.df['action'] = np.where(self.df['diff'] > diff, 1, 0)
        self.df['action'] = np.where(self.df['diff'] < -diff, -1, self.df['action'])

    def trade(self, portfolio, lot, column='open', broker_percent=0.1):
        start_portfolio = portfolio
        for index, row in self.df.iterrows():
            if row['action'] < 0 and self.is_bought:
                value = row[column] * lot
                value = value - value * (broker_percent / 100)
                portfolio = portfolio + value
                self.sell_count += 1
                self.is_bought = False

            elif row['action'] > 0 and not self.is_bought:
                value = row[column] * lot
                value = value + value * (broker_percent / 100)
                portfolio = portfolio - value
                self.buy_count += 1
                self.is_bought = True

        self.percent = round((portfolio - start_portfolio)/portfolio, 2) * 100

        return portfolio

    def plot(self, columns=['open']):
        plt.style.use('ggplot')
        figure(figsize=(10, 10), dpi=80)
        self.df.plot(y=columns)

    def report(self):
        return f'SELLS:{self.sell_count}, BUYS: {self.buy_count}'

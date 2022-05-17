import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from AlgoTrader.core.trader.strategies.BaseStrategy import BaseStrategy

class AlgoTrader:
    strategy = None
    sensitive_column = 'sensitive'
    stocks_count = 0
    buy_count = 0
    percent = 0
    broker_percent = 0.03
    report_df = None
    report_dict = []
    report_df_index = 0
    commission = 0
    current_portfolio = 0
    is_bought = False
    trade_value = 0
    start_portfolio = 0
    price = 0
    volume = 0
    benefit = 0
    final_benefit = 0

    def __init__(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate_percent(self):
        return round((self.current_portfolio - self.start_portfolio) / self.start_portfolio, 3) * 100

    def apply_buy_commission(self, value):
        commission = value * (self.broker_percent / 100)
        self.commission += commission
        return value - commission

    def apply_sale_commission(self, value):
        commission = value * (self.broker_percent / 100)
        self.commission += commission
        return value + commission

    def fill_report_dict(self, datetime):
        row = {
            'datetime': str(datetime),
            'price': self.price,
            'stocks_count': self.stocks_count,
            'portfolio': self.current_portfolio,
            'volume': self.volume,
            'benefit': self.benefit,
            '%': self.calculate_percent()}
        if self.is_bought:
            row['action'] = 'sell'
        else:
            row['action'] = 'buy'

        self.report_dict.append(row)

    def sale(self, row):
        volume = self.apply_sale_commission(self.price * self.stocks_count)
        self.benefit = volume - self.volume
        self.volume = volume
        self.current_portfolio += self.volume
        self.fill_report_dict(row.name)
        self.is_bought = False

    def buy(self, row):
        self.stocks_count = ((self.trade_value / 100) * self.current_portfolio) / self.price
        self.volume = self.apply_buy_commission(self.price * self.stocks_count)
        self.benefit = 0
        self.current_portfolio -= self.volume
        self.fill_report_dict(row.name)
        self.is_bought = True

    def trade(self, portfolio, trade_value, column='open'):
        self.strategy.analyze()
        self.trade_value = trade_value
        self.start_portfolio = portfolio
        self.current_portfolio = portfolio

        df = self.strategy.df

        if 'action' in df.columns:
            i = 0
            for index, row in df.iterrows():
                i += 1
                self.price = row[column]
                if row['action'] < 0 and self.is_bought:
                    self.sale(row)

                elif row['action'] > 0 and not self.is_bought:
                    self.buy(row)

                if i == len(df) and self.is_bought:
                    # final sale
                    self.sale(row)

            self.percent = self.calculate_percent()
            self.final_benefit = self.current_portfolio - self.start_portfolio
        else:
            raise Exception('`action` column does not exist in the DataFrame')

    def plot(self, columns=None):
        if columns is None:
            columns = ['open']
        plt.style.use('ggplot')
        figure(figsize=(15, 15), dpi=80)
        self.strategy.df.plot(y=columns)

    def plot_with_sma(self, *args, **kwargs):
        from_datetime = kwargs.get('from_datetime', None)
        to_datetime = kwargs.get('to_datetime', None)
        if kwargs.get('columns') is None:
            columns = ['open', 'safe', 'sensitive']
        df = self.strategy.df.copy()
        if from_datetime:
            df = df[df.index > from_datetime]
        if to_datetime:
            df = df[df.index < to_datetime]
        plt.style.use('ggplot')
        figure(figsize=(10, 10), dpi=80)
        df.plot(y=columns)

    def report(self):
        return pd.DataFrame(self.report_dict)

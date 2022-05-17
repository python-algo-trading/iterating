import numpy as np

from AlgoTrader.core.trader.strategies.BaseStrategy import BaseStrategy


class MinTrendStrategy(BaseStrategy):
    def __init__(self, df, **kwargs):
        self.column = kwargs.get('column', 'open')
        self.sensitive = kwargs.get('sensitive', 50)
        self.safe = kwargs.get('safe', 200)
        self.diff = kwargs.get('diff', None)
        super(MinTrendStrategy, self).__init__(df)

    def analyze(self):
        column = self.column
        diff = self.diff
        sensitive = self.sensitive
        safe = self.safe
        self.df['sensitive'] = self.df[column].rolling(sensitive).mean()
        self.df['safe'] = self.df[column].rolling(safe).mean()
        self.df['diff'] = self.df['safe'] - self.df['sensitive']
        self.df['action'] = np.where(self.df['diff'] > diff, 1, 0)
        self.df['action'] = np.where(self.df['diff'] < -diff, -1, self.df['action'])

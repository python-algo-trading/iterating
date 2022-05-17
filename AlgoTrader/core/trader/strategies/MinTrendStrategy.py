import numpy as np

from AlgoTrader.core.trader.strategies.BaseStrategy import BaseStrategy


class MinTrendStrategy(BaseStrategy):
    def __init__(self, df, **kwargs):
        self.column = kwargs.get('column', 'open')
        self.delay = kwargs.get('delay', 1)
        self.diff = kwargs.get('diff', None)
        self.ma = kwargs.get('ma', None)
        super(MinTrendStrategy, self).__init__(df)

    def analyze(self):
        self.df['ma'] = self.df[self.column].rolling(self.ma).mean()
        self.df['trend'] = self.df['ma'].diff(self.delay)
        self.df['action'] = np.where(self.df['trend'] > self.diff, 1, 0)
        self.df['action'] = np.where(self.df['trend'] < -self.diff, -1, self.df['action'])


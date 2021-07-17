import numpy as np
import pandas as pd

from AlgoTrader.core.trader.ATrader import ATrader


class Iterator:
    delta = 0

    def __init__(self, df):
        self.df = df
        self.define_delta()

    def define_delta(self, column='open'):
        max_value = self.df[column].max()
        min_value = self.df[column].min()
        self.delta = ((max_value - min_value) / 50, (max_value - min_value) / 2)

    def get_delta_range(self):
        return np.linspace(self.delta[0], self.delta[1], 10)

    def compose_iterator_dataframe(self):
        deltas = self.get_delta_range()
        sensitives = range(8, 12)
        safes = range(18, 21)
        deltas_count = len(deltas)
        sensitive_count = len(sensitives)
        safe_count = len(safes)
        rows_count = deltas_count * safe_count * sensitive_count

        df = pd.DataFrame(
            index=range(1, rows_count + 10),
            columns=['sensitive', 'delta', 'safe', '%']
        )

        # df.info()
        i = 0
        for safe in safes:
            for delta in deltas:
                for sensitive in sensitives:
                    i += 1
                    df.loc[i]['sensitive'] = sensitive
                    df.loc[i]['delta'] = delta
                    df.loc[i]['safe'] = safe

        return df

    def calculate(self, df, portfolio=1000, lot=20):

        def trade(row):
            trader = ATrader(self.df.copy())
            try:
                if not np.isnan(row['safe']) and not np.isnan(row['sensitive']) and not np.isnan(row['delta']):
                    trader.analyze(row['sensitive'], row['safe'], row['delta'])
                    trader.trade(portfolio, lot)
            except ValueError:
                print(row['sensitive'])

            return trader.percent

        df['%'] = df.apply(trade, axis=1)
        df.where(df['%'] > 0, inplace=True)
        df.sort_values(by=['%'], inplace=True, ascending=False)

        return df

import numpy as np
import pandas as pd


class AlgoIterator:

    def __init__(self, df, dictionary, function):
        self.df = df
        self.dictionary = dictionary
        self.function = function

        # defining report_df
        keys = list(self.dictionary.keys())
        length = 1
        for key, value in self.dictionary.items():
            length = length * len(value)

        self.report_df = pd.DataFrame(
            index=range(0, length),
            columns=np.append(keys, ['%'])
        )
        self._fill_report_df()

    def _fill_report_df(self):
        keys = list(self.dictionary.keys())
        i = 0
        for first in self.dictionary[keys[0]]:
            if len(keys) > 1:
                for second in self.dictionary[keys[1]]:
                    if len(keys) > 2:
                        for third in self.dictionary[keys[2]]:
                            if len(keys) > 3:
                                for fourth in self.dictionary[keys[3]]:
                                    self.report_df.loc[i][keys[0]] = first
                                    self.report_df.loc[i][keys[1]] = second
                                    self.report_df.loc[i][keys[2]] = third
                                    self.report_df.loc[i][keys[3]] = fourth
                                    i += 1

                            else:
                                self.report_df.loc[i][keys[0]] = first
                                self.report_df.loc[i][keys[1]] = second
                                self.report_df.loc[i][keys[2]] = third
                                i += 1

                    else:
                        self.report_df.loc[i][keys[0]] = first
                        self.report_df.loc[i][keys[1]] = second
                        i += 1

            else:
                self.report_df.loc[i][keys[0]] = first
                i += 1

    def _prepare_report(self):
        self.report_df.where(self.report_df['%'] > 0, inplace=True)
        self.report_df.sort_values(by=['%'], inplace=True, ascending=False)

    def iterate_trading(self):
        self.report_df['%'] = self.report_df.apply(self.function, axis=1)

        self._prepare_report()

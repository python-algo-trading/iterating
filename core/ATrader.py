{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "pycharm": {
   "stem_cell": {
    "cell_type": "raw",
    "source": [
     "\n",
     "import pandas as pd\n",
     "import numpy as np\n",
     "\n",
     "import matplotlib.pyplot as plt\n",
     "from matplotlib.pyplot import figure\n",
     "\n",
     "\n",
     "class ATrader:\n",
     "    def __init__(self, df):\n",
     "        self.df = df\n",
     "        \n",
     "    def analyze(self, sence = 10, safe = 50, diff = 1, column = 'open'):\n",
     "        self.df['sence'] = self.df[column].rolling(sence).mean()\n",
     "        self.df['safe'] = self.df[column].rolling(safe).mean()\n",
     "        self.df['diff'] = self.df['safe'] - self.df['sence']\n",
     "        self.df['action'] = np.where(self.df['diff'] > diff, 1, 0)\n",
     "        self.df['action'] = np.where(self.df['diff'] < -diff, -1, self.df['action'])\n",
     "\n",
     "    def trade(self, portfolio, lot, column = 'open', broker_percent = 0.1):\n",
     "        value = 0\n",
     "        for index, row in self.df.iterrows():\n",
     "            if row['action'] < 0:\n",
     "                value = row[column]*lot\n",
     "                value = value - value * (broker_percent/100)\n",
     "                portfolio = portfolio + value\n",
     "            elif row['action'] > 0:\n",
     "                    value = row[column]*lot\n",
     "                    value = value + value * (broker_percent/100)\n",
     "                    portfolio = portfolio - value\n",
     "        return portfolio\n",
     "    \n",
     "    def plot(self, columns = ['open']):\n",
     "        plt.style.use('ggplot')\n",
     "        figure(figsize=(10, 10), dpi=80)\n",
     "        self.df.plot(y=columns)\n",
     "\n",
     "\n"
    ],
    "metadata": {
     "collapsed": false
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
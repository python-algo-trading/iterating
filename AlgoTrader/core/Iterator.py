{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "23cce632",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "import numpy.random as random\n",
    "\n",
    "\n",
    "class Iterator():\n",
    "    \n",
    "    delta = 0\n",
    "    \n",
    "    def __init__(self, df):\n",
    "        self.df = df\n",
    "        self.delta()\n",
    "    \n",
    "    def delta(self, column = 'open'):\n",
    "        max = self.df[column].max()\n",
    "        min = self.df[column].min()\n",
    "        self.delta = ((max - min) / 5000, (max - min)/ 10)\n",
    "    \n",
    "    def get_delta_range(self):\n",
    "        return np.linspace(self.delta[0],self.delta[1], 50)\n",
    "        \n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33508b8e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddbcde27",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5f47aae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65ac24c7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

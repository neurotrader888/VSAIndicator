import pandas as pd
import pandas_ta as ta
import numpy as np
import scipy
import matplotlib.pyplot as plt


data = pd.read_csv('BTCUSDT3600.csv')
data['date'] = data['date'].astype('datetime64[s]')
data = data.set_index('date')

plt.style.use('dark_background')

# Get relative range/volume
#  24 * 7 = 168
atr = ta.atr(data['high'], data['low'], data['close'], 168)
data['norm_range'] = (data['high'] - data['low']) / atr

volume_median = data['volume'].rolling(168).median()
data['norm_volume'] = data['volume'] / volume_median

# Random 1 week slice
data = data.iloc[1000:1168]
slope, intercept, _, _, std_err = scipy.stats.linregress(data['norm_volume'], data['norm_range'])

p1 = intercept + slope * data['norm_volume'].min()
p2 = intercept + slope * data['norm_volume'].max()

data.plot.scatter('norm_volume', 'norm_range')
plt.xlabel("Volume")
plt.ylabel("Range")
plt.plot([data['norm_volume'].min(), data['norm_volume'].max()], [p1, p2],color='orange')
plt.show()



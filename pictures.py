import pandas as pd
import pandas_ta as ta
import numpy as np
import scipy
import matplotlib.pyplot as plt


data = pd.read_csv('BTCUSDT3600.csv')
data['date'] = data['date'].astype('datetime64[s]')
data = data.set_index('date')

plt.style.use('dark_background')

# Plot raw volume and range
data['volume'].plot()
plt.ylabel("BTC Volume")
plt.show()

(data['high'] - data['low']).plot()
plt.ylabel("Candle Range (High - Low)")
plt.show()


# Get relative range/volume
#  24 * 7 = 168
atr = ta.atr(data['high'], data['low'], data['close'], 168)
data['norm_range'] = (data['high'] - data['low']) / atr

volume_median = data['volume'].rolling(168).median()
data['norm_volume'] = data['volume'] / volume_median

data['norm_range'].plot(label='Range')
data['norm_volume'].plot(label='Volume')
plt.legend()
plt.show()

print("Volume - Range Correlation", data['norm_range'].corr(data['norm_volume']))
data.plot.scatter('norm_volume', 'norm_range')
plt.xlabel("Volume")
plt.ylabel("Range")
plt.show()






import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import rfft

data = np.load("record.npy")
data_filtered = data[4700:]
data_spec = rfft(data_filtered)

fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

line, = ax1.plot(data_filtered, '.', lw=2)

line_fft, = ax2.semilogx(data_spec, '-', lw=2)

plt.show()
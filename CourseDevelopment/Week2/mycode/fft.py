import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import rfft

data = np.load("rawfile0.npy")
data_filtered = data[4700:]
RATE = 48000
seglen = 5000
seg1 = 18000+30000
seg2 = 32000+30000

fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

line, = ax1.plot(data_filtered, '.', lw=2)
chunk1 = data_filtered[seg1:seg1+seglen]
chunk2 = data_filtered[seg2:seg2+seglen]
line2, = ax1.plot(np.arange(seg1, seg1+seglen, dtype = int), chunk1)
line3, = ax1.plot(np.arange(seg2, seg2+seglen, dtype = int), chunk2)

chunk1_spec = np.abs(rfft(chunk1))
chunk2_spec = np.abs(rfft(chunk2))

line_fft1, = ax2.semilogx(chunk1_spec, '-', lw=2)
line_fft2, = ax2.semilogx(chunk2_spec, '-', lw=2)

plt.show()

peak1 = np.argmax(chunk1_spec)
peak2 = np.argmax(chunk2_spec)
f1 = peak1 * RATE / seglen / 2
f2 = peak2 * RATE / seglen / 2

print('shifted frequencies:',f1, f2)
print('doppler shift is: {} Hz'.format((f2-f1)))

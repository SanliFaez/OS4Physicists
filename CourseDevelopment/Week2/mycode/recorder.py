import matplotlib
matplotlib.use('TkAgg')

import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt


# ------------ Audio Setup ---------------
# constants
CHUNK = 1024 * 16  # samples per frame
FORMAT = pyaudio.paInt16  # audio format (bytes per sample?)
CHANNELS = 1  # single channel for microphone
RATE = 48000  # samples per second
# Signal range is -32k to 32k
# limiting amplitude to +/- 4k
# AMPLITUDE_LIMIT = 4096

# pyaudio class instance
p = pyaudio.PyAudio()

# stream object to get data from microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)


fig, (ax1) = plt.subplots(1, figsize=(15, 7))
x = np.arange(0, 2 * CHUNK, 2)  # samples (waveform)

# format waveform axes
ax1.set_title('AUDIO WAVEFORM')
ax1.set_xlabel('samples')
ax1.set_ylabel('volume')
ax1.set_xlim(0, 2 * CHUNK)

#start_time = time.time()

data = stream.read(CHUNK, exception_on_overflow=False)
data_np = np.frombuffer(data, dtype='h')
plt.plot(x, data_np)
plt.show()

np.save("record.npy", data_np)

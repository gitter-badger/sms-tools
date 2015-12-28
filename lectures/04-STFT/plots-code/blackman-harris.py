# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.fftpack import fft

M = 64
N = 512
hN = N / 2
hM = M / 2
fftbuffer = np.zeros(N)
mX1 = np.zeros(N)

plt.figure(1, figsize=(7.5, 4))
fftbuffer[hN - hM:hN + hM] = signal.blackmanharris(M)
plt.subplot(2, 1, 1)
plt.plot(np.arange(-hN, hN), fftbuffer, 'b', lw=1.5)
plt.axis([-hN, hN, 0, 1.1])

X = fft(fftbuffer)
mX = 20 * np.log10(abs(X))
mX1[:hN] = mX[hN:]
mX1[N - hN:] = mX[:hN]

plt.subplot(2, 1, 2)
plt.plot(np.arange(-hN, hN), mX1 - max(mX), 'r', lw=1.5)
plt.axis([-hN, hN, -110, 0])

plt.tight_layout()
plt.savefig('blackman-harris.png')

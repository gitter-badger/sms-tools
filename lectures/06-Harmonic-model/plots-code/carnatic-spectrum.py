import math
# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from smst.utils import audio
from smst.models import dft

(fs, x) = audio.read_wav('../../../sounds/carnatic.wav')
pin = 1.4 * fs
w = np.blackman(1601)
N = 4096
hM1 = int(math.floor((w.size + 1) / 2))
hM2 = int(math.floor(w.size / 2))
x1 = x[pin - hM1:pin + hM2]
mX, pX = dft.from_audio(x1, w, N)

plt.figure(1, figsize=(9, 7))
plt.subplot(311)
plt.plot(np.arange(-hM1, hM2) / float(fs), x1, lw=1.5)
plt.axis([-hM1 / float(fs), hM2 / float(fs), min(x1), max(x1)])
plt.title('x (carnatic.wav)')

plt.subplot(3, 1, 2)
plt.plot(fs * np.arange(mX.size) / float(N), mX, 'r', lw=1.5)
plt.axis([0, fs / 4, -100, max(mX)])
plt.title('mX')

plt.subplot(3, 1, 3)
plt.plot(fs * np.arange(pX.size) / float(N), pX, 'c', lw=1.5)
plt.axis([0, fs / 4, min(pX), 27])
plt.title('pX')

plt.tight_layout()
plt.savefig('carnatic-spectrum.png')

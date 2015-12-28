import math
# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from smst.utils import audio
from smst.models import dft

(fs, x) = audio.read_wav('../../../sounds/oboe-A4.wav')
w = np.hamming(511)
N = 512
pin = 5000
hM1 = int(math.floor((w.size + 1) / 2))
hM2 = int(math.floor(w.size / 2))
x1 = x[pin - hM1:pin + hM2]
mX, pX = dft.from_audio(x1, w, N)

plt.figure(1, figsize=(9.5, 7))

plt.subplot(311)
plt.plot(np.arange(-hM1, hM2), x1, lw=1.5)
plt.axis([-hM1, hM2, min(x1), max(x1)])
plt.ylabel('amplitude')
plt.title('x (oboe-A4.wav)')

plt.subplot(3, 1, 2)
plt.plot(np.arange(mX.size), mX, 'r', lw=1.5)
plt.axis([0, mX.size, min(mX), max(mX)])
plt.title('magnitude spectrum: mX = 20*log10(abs(X))')
plt.ylabel('amplitude (dB)')

plt.subplot(3, 1, 3)
plt.plot(np.arange(mX.size), pX, 'c', lw=1.5)
plt.axis([0, mX.size, min(pX), max(pX)])
plt.title('phase spectrum: pX=unwrap(angle(X))')
plt.ylabel('phase (radians)')

plt.tight_layout()
plt.savefig('spectrum-1.png')

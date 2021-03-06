import math
# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from smst.utils import audio
from smst.models import dft

(fs, x) = audio.read_wav('../../../sounds/oboe-A4.wav')
w = np.hanning(501)
N = 512
pin = 5000
hM1 = int(math.floor((w.size + 1) / 2))
hM2 = int(math.floor(w.size / 2))
x1 = x[pin - hM1:pin + hM2]
mX, pX = dft.from_audio(x1, w, N)
y = dft.to_audio(mX, pX, w.size) * sum(w)

plt.figure(1, figsize=(9.5, 5.5))
plt.subplot(4, 1, 1)
plt.plot(np.arange(-hM1, hM2), x1 * w, lw=1.5)
plt.axis([-hM1, hM2, min(x1), max(x1)])
plt.title('x (oboe-A4.wav)')

plt.subplot(4, 1, 2)
plt.plot(np.arange(mX.size), mX, 'r', lw=1.5)
plt.axis([0, mX.size, min(mX), max(mX)])
plt.title('mX')

plt.subplot(4, 1, 3)
plt.plot(np.arange(pX.size), pX, 'c', lw=1.5)
plt.axis([0, pX.size, min(pX), max(pX)])
plt.title('pX')

plt.subplot(4, 1, 4)
plt.plot(np.arange(-hM1, hM2), y, lw=1.5)
plt.axis([-hM1, hM2, min(y), max(y)])
plt.title('y')

plt.tight_layout()
plt.savefig('anal-synth.png')

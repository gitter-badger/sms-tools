import math
import numpy as np
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import hamming, triang, blackmanharris

from smst.utils import audio
from smst.models import dft

(fs, x) = audio.wavread('../../../sounds/oboe-A4.wav')
w = np.blackman(651)
N = 1024
pin = 5000
hM1 = int(math.floor((w.size+1)/2))
hM2 = int(math.floor(w.size/2))
x1 = x[pin-hM1:pin+hM2]
mX, pX = dft.fromAudio(x1, w, N)

plt.figure(1, figsize=(9, 7))
plt.subplot(311)
plt.plot(np.arange(-hM1, hM2)/float(fs), x1, lw=1.5)
plt.axis([-hM1/float(fs), hM2/float(fs), min(x1), max(x1)])
plt.title('x (oboe-A4.wav)')

plt.subplot(3,1,2)
plt.plot(fs*np.arange(mX.size)/float(N), mX, 'r', lw=1.5)
plt.axis([0,fs/3,-90,max(mX)])
plt.title ('mX')

plt.subplot(3,1,3)
plt.plot(fs*np.arange(pX.size)/float(N), pX, 'c', lw=1.5)
plt.axis([0,fs/3,min(pX),18])
plt.title ('pX')

plt.tight_layout()
plt.savefig('oboe-spectrum.png')

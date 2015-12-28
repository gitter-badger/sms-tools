import math
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from smst.utils import audio
from smst.models import dft

(fs, x) = audio.wavread('../../../sounds/piano.wav')
M = 1100
w = np.blackman(M)
N = 2048
pin = .3*fs
hM1 = int(math.floor((w.size+1)/2))
hM2 = int(math.floor(w.size/2))
x1 = x[pin-hM1:pin+hM2]
mX, pX = dft.fromAudio(x1, w, N)

plt.figure(1, figsize=(9, 7))
plt.subplot(311)
plt.plot(np.arange(-hM1, hM2)/float(fs), x1, lw=1.5)
plt.axis([-hM1/float(fs), hM2/float(fs), min(x1), max(x1)])
plt.title('x (piano.wav)')

plt.subplot(3,1,2)
plt.plot(fs*np.arange(mX.size)/float(N), mX, 'r', lw=1.5)
plt.axis([0,fs/4,-90,max(mX)])
plt.title ('mX')

plt.subplot(3,1,3)
plt.plot(fs*np.arange(pX.size)/float(N), pX, 'c', lw=1.5)
plt.axis([0,fs/4,-5,max(pX)])
plt.title ('pX')

plt.tight_layout()
plt.savefig('piano-spectrum.png')

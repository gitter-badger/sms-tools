import math
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


from smst import utils
from smst.models import dft

(fs, x) = utils.wavread('../../../sounds/oboe-A4.wav')
M = 512
N = 512
start = .8*fs
x1 = x[start:start+M]
xw = x1 * np.hamming(M)

plt.figure(1, figsize=(9.5, 6))
plt.subplot(311)
plt.plot(np.arange(start, (start+M), 1.0)/fs, xw, 'b', lw=1.5)
plt.axis([start/fs, (start+M)/fs, min(xw), max(xw)])
plt.title('x (oboe-A4.wav), M = 512')
mX, pX = dft.fromAudio(x1, np.hamming(N), N)

plt.subplot(312)
plt.plot((fs/2.0)*np.arange(mX.size)/float(mX.size), mX, 'r', lw=1.5)
plt.axis([0,fs/4.0,-85,max(mX)])
plt.title('mX, N = 512')

M = 512
N = 2048
start = .8*fs
x1 = x[start:start+M]
xw = x1 * np.hamming(M)
mX, pX = dft.fromAudio(x1, np.hamming(M), N)

plt.subplot(313)
plt.plot((fs/2.0)*np.arange(mX.size)/float(mX.size), mX, 'r', lw=1.5)
plt.axis([0,fs/4.0,-85,max(mX)])
plt.title('mX, N = 2048')

plt.tight_layout()
plt.savefig('fft-size.png')

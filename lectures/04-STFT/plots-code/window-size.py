import math
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import time

from smst.models import dft
import smst.utils as utils

(fs, x) = utils.wavread('../../../sounds/oboe-A4.wav')
N = 128
start = .81*fs
x1 = x[start:start+N]
plt.figure(1, figsize=(9.5, 6))
plt.subplot(321)
plt.plot(np.arange(start, (start+N), 1.0)/fs, x1*np.hamming(N), 'b', lw=1.5)
plt.axis([start/fs, (start+N)/fs, min(x1*np.hamming(N)), max(x1*np.hamming(N))])
plt.title('x1, M = 128')

mX, pX = dft.fromAudio(x1, np.hamming(N), N)
plt.subplot(323)
plt.plot((fs/2.0)*np.arange(mX.size)/float(mX.size), mX, 'r', lw=1.5)
plt.axis([0,fs/2.0,-90,max(mX)])
plt.title('mX1')

plt.subplot(325)
plt.plot((fs/2.0)*np.arange(mX.size)/float(mX.size), pX, 'c', lw=1.5)
plt.axis([0,fs/2.0,min(pX),max(pX)])
plt.title('pX1')

N = 1024
start = .81*fs
x2 = x[start:start+N]
mX, pX = dft.fromAudio(x2, np.hamming(N), N)

plt.subplot(322)
plt.plot(np.arange(start, (start+N), 1.0)/fs, x2*np.hamming(N), 'b', lw=1.5)
plt.axis([start/fs, (start+N)/fs, min(x2), max(x2)])
plt.title('x2, M = 1024')

plt.subplot(324)
plt.plot((fs/2.0)*np.arange(mX.size)/float(mX.size), mX, 'r', lw=1.5)
plt.axis([0,fs/2.0,-90,max(mX)])
plt.title('mX2')

plt.subplot(326)
plt.plot((fs/2.0)*np.arange(mX.size)/float(mX.size), pX, 'c', lw=1.5)
plt.axis([0,fs/2.0,min(pX),max(pX)])
plt.title('pX2')

plt.tight_layout()
plt.savefig('window-size.png')

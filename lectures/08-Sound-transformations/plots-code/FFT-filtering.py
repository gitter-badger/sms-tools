import math
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import time



from smst.models import dft
import smst.utils as utils


(fs, x) = utils.wavread('../../../sounds/orchestra.wav')
N = 2048
start = 1.0*fs
x1 = x[start:start+N]

plt.figure(1, figsize=(12, 9))
plt.subplot(321)
plt.plot(np.arange(N)/float(fs), x1*np.hamming(N), 'b', lw=1.5)
plt.axis([0, N/float(fs), min(x1*np.hamming(N)), max(x1*np.hamming(N))])
plt.title('x (orchestra.wav)')

mX, pX = dft.fromAudio(x1, np.hamming(N), N)
startBin = int(N*500.0/fs)
nBins = int(N*4000.0/fs)
bandpass = (np.hanning(nBins) * 60.0) - 60
filt = np.zeros(mX.size)-60
filt[startBin:startBin+nBins] = bandpass
mY = mX + filt

plt.subplot(323)
plt.plot(fs*np.arange(mX.size)/float(mX.size), mX, 'r', lw=1.5, label = 'mX')
plt.plot(fs*np.arange(mX.size)/float(mX.size), filt+max(mX), 'k', lw=1.5, label='filter')
plt.legend(prop={'size':10})
plt.axis([0,fs/4.0,-90,max(mX)+2])
plt.title('mX + filter')

plt.subplot(325)
plt.plot(fs*np.arange(pX.size)/float(pX.size), pX, 'c', lw=1.5)
plt.axis([0,fs/4.0,min(pX),8])
plt.title('pX')

y = dft.toAudio(mY, pX, N)*sum(np.hamming(N))
mY1, pY = dft.fromAudio(y, np.hamming(N), N)
plt.subplot(322)
plt.plot(np.arange(N)/float(fs), y, 'b')
plt.axis([0, float(N)/fs, min(y), max(y)])
plt.title('y')

plt.subplot(324)
plt.plot(fs*np.arange(mY1.size)/float(mY1.size), mY1, 'r', lw=1.5)
plt.axis([0,fs/4.0,-90,max(mY1)+2])
plt.title('mY')

plt.subplot(326)
plt.plot(fs*np.arange(pY.size)/float(pY.size), pY, 'c', lw=1.5)
plt.axis([0,fs/4.0,min(pY),8])
plt.title('pY')

plt.tight_layout()
plt.savefig('FFT-filtering.png')


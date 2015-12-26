import numpy as np
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import hamming, hanning, resample
from scipy.fftpack import fft, ifft
import time
import sys, os


import smst.utils as utils
import smst.models.stochasticModel as STM
import smst.models.stft as STFT

(fs, x) = utils.wavread('../../../sounds/ocean.wav')
w = np.hamming(512)
N = 512
H = 256
stocf = .1
mYst = STM.stochasticModelAnal(x, H, N, stocf)
y = STM.stochasticModelSynth(mYst, H, N)
mX, pX = STFT.stftAnal(x, w, N, H)

plt.figure(1, figsize=(9, 7))
plt.subplot(411)
plt.plot(np.arange(x.size)/float(fs), x,'b')
plt.title('x (ocean.wav)')
plt.axis([0,x.size/float(fs),min(x),max(x)])

plt.subplot(412)
numFrames = int(mX[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(mX[0,:].size)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX))
plt.title('mX; M=512, N=512, H=256')
plt.autoscale(tight=True)

plt.subplot(413)
numFrames = int(mYst[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(stocf*mX[0,:].size)*float(fs)/(stocf*N)
plt.pcolormesh(frmTime, binFreq, np.transpose(mYst))
plt.title('mY (stochastic approximation); stocf=.1')
plt.autoscale(tight=True)

plt.subplot(414)
plt.plot(np.arange(y.size)/float(fs), y,'b')
plt.title('y')
plt.axis([0,y.size/float(fs),min(y),max(y)])

plt.tight_layout()
plt.savefig('stochasticModelAnalSynth.png')
utils.wavwrite(y, fs, 'ocean-synthesis.wav')


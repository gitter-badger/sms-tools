import numpy as np
import time

from smst.models import stft
import smst.utils as utils
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import hamming
from scipy.fftpack import fft
import math

(fs, x) = utils.wavread('../../../sounds/piano.wav')

plt.figure(1, figsize=(9.5, 6))

w = np.hamming(256)
N = 256
H = 128
mX1, pX1 = stft.stftAnal(x, w, N, H)
plt.subplot(211)
numFrames = int(mX1[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(mX1[0,:].size)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX1))
plt.title('mX (piano.wav), M=256, N=256, H=128')
plt.autoscale(tight=True)

w = np.hamming(1024)
N = 1024
H = 128
mX2, pX2 = stft.stftAnal(x, w, N, H)

plt.subplot(212)
numFrames = int(mX2[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(mX2[0,:].size)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX2))
plt.title('mX (piano.wav), M=1024, N=1024, H=128')
plt.autoscale(tight=True)

plt.tight_layout()
plt.savefig('time-freq-compromise.png')

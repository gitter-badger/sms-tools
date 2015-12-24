import numpy as np
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import hamming, triang, blackmanharris
from scipy.fftpack import fft, ifft
import math
import sys, os, functools, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../'))

import smst.models.dftModel as DFT
import smst.models.utilFunctions as UF

(fs, x) = UF.wavread('../../../sounds/oboe-A4.wav')
N = 512
M = 511
t = -60
w = np.hamming(M)
start = .8*fs
hN = N/2
hM = (M+1)/2

x1 = x[start:start+M]
mX, pX = DFT.dftAnal(x1, w, N)
ploc = UF.peakDetection(mX, t)
pmag = mX[ploc]
freqaxis = fs*np.arange(mX.size)/float(N)

plt.figure(1, figsize=(9.5, 5.5))
plt.subplot (2,1,1)
plt.plot(freqaxis, mX, 'r', lw=1.5)
plt.axis([300,2500,-70,max(mX)])
plt.plot(fs * ploc / N, pmag, marker='x', color='b', linestyle='', markeredgewidth=1.5)
plt.title('mX + spectral peaks (oboe-A4.wav)')

plt.subplot (2,1,2)
plt.plot(freqaxis,pX,'c', lw=1.5)
plt.axis([300,2500,6,14])
plt.plot(fs * ploc / N, pX[ploc], marker='x', color='b', linestyle='', markeredgewidth=1.5)
plt.title('pX + spectral peaks')

plt.tight_layout()
plt.savefig('spectral-peaks.png')


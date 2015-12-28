import math
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hamming, triang, blackmanharris

from smst.utils import audio, peaks
from smst.models import dft

(fs, x) = audio.wavread('../../../sounds/oboe-A4.wav')
N = 512*2
M = 511
t = -60
w = np.hamming(M)
start = .8*fs
hN = N/2
hM = (M+1)/2

x1 = x[start:start+M]
mX, pX = dft.fromAudio(x1, w, N)
ploc = peaks.peakDetection(mX, t)
iploc, ipmag, ipphase = peaks.peakInterp(mX, pX, ploc)
pmag = mX[ploc]
freqaxis = fs*np.arange(mX.size)/float(N)

plt.figure(1, figsize=(9, 6))
plt.subplot (2,1,1)
plt.plot(freqaxis, mX,'r', lw=1.5)
plt.axis([0,7000,-80,max(mX)+1])
plt.plot(fs * iploc / N, ipmag, marker='x', color='b', linestyle='', markeredgewidth=1.5)
plt.title('mX + peaks (oboe-A4.wav)')

plt.subplot (2,1,2)
plt.plot(freqaxis, pX,'c', lw=1.5)
plt.axis([0,7000, min(pX),10])
plt.plot(fs * iploc/N, ipphase, marker='x', color='b', linestyle='', markeredgewidth=1.5)
plt.title('pX + peaks')

plt.tight_layout()
plt.savefig('spectral-peaks.png')

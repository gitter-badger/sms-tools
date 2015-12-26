import numpy as np
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import hamming, triang, blackmanharris
import sys, os, functools, time
import smst.models.dftModel as DFT
import smst.utils as utils



(fs, x) = utils.wavread('../../../sounds/sine-440-490.wav')
w = np.hamming(3529)
N = 32768
hN = N/2
t = -20
pin = 4850
x1 = x[pin:pin+w.size]
mX1, pX1 = DFT.dftAnal(x1, w, N)
ploc = utils.peakDetection(mX1, t)
pmag = mX1[ploc]
iploc, ipmag, ipphase = utils.peakInterp(mX1, pX1, ploc)

plt.figure(1, figsize=(9, 6))
plt.subplot(311)
plt.plot(fs*np.arange(mX1.size)/float(N), mX1-max(mX1), 'r', lw=1.5)
plt.plot(fs * iploc/N, ipmag-max(mX1), marker='x', color='b', alpha=1, linestyle='', markeredgewidth=1.5)
plt.axis([200, 1000, -80, 4])
plt.title('mX + peaks (sine-440-490.wav)')

(fs, x) = utils.wavread('../../../sounds/vibraphone-C6.wav')
w = np.blackman(401)
N = 1024
hN = N/2
t = -80
pin = 200
x2 = x[pin:pin+w.size]
mX2, pX2 = DFT.dftAnal(x2, w, N)
ploc = utils.peakDetection(mX2, t)
pmag = mX2[ploc]
iploc, ipmag, ipphase = utils.peakInterp(mX2, pX2, ploc)

plt.subplot(3,1,2)
plt.plot(fs*np.arange(mX2.size)/float(N), mX2-max(mX2), 'r', lw=1.5)
plt.plot(fs * iploc/N, ipmag-max(mX2), marker='x', color='b', alpha=1, linestyle='', markeredgewidth=1.5)
plt.axis([500,10000,-100,4])
plt.title('mX + peaks (vibraphone-C6.wav)')

(fs, x) = utils.wavread('../../../sounds/oboe-A4.wav')
w = np.blackman(651)
N = 2048
hN = N/2
t = -80
pin = 10000
x3 = x[pin:pin+w.size]
mX3, pX3 = DFT.dftAnal(x3, w, N)
ploc = utils.peakDetection(mX3, t)
pmag = mX3[ploc]
iploc, ipmag, ipphase = utils.peakInterp(mX3, pX3, ploc)

plt.subplot(3,1,3)
plt.plot(fs*np.arange(mX3.size)/float(N), mX3-max(mX3), 'r', lw=1.5)
plt.plot(fs * iploc/N, ipmag-max(mX3), marker='x', color='b', alpha=1, linestyle='', markeredgewidth=1.5)
plt.axis([0,6000,-70,2])
plt.title('mX + peaks (oboe-A4.wav)')

plt.tight_layout()
plt.savefig('sines-partials-harmonics.png')


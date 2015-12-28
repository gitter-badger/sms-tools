import math
# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftshift
from scipy.signal import blackmanharris, resample

from smst.utils import audio, peaks, synth
from smst.models import dft, harmonic

(fs, x) = audio.read_wav('../../../sounds/flute-A4.wav')
pos = .8 * fs
M = 601
hM1 = int(math.floor((M + 1) / 2))
hM2 = int(math.floor(M / 2))
w = np.hamming(M)
N = 1024
t = -100
nH = 40
minf0 = 420
maxf0 = 460
f0et = 5
minSineDur = .1
harmDevSlope = 0.01
Ns = 512
H = Ns / 4
stocf = .2
x1 = x[pos - hM1:pos + hM2]
x2 = x[pos - Ns / 2 - 1:pos + Ns / 2 - 1]

mX, pX = dft.from_audio(x1, w, N)
ploc = peaks.find_peaks(mX, t)
iploc, ipmag, ipphase = peaks.interpolate_peaks(mX, pX, ploc)
ipfreq = fs * iploc / N
f0 = peaks.find_fundamental_twm(ipfreq, ipmag, f0et, minf0, maxf0)
hfreqp = []
hfreq, hmag, hphase = harmonic.find_harmonics(ipfreq, ipmag, ipphase, f0, nH, hfreqp, fs, harmDevSlope)
Yh = synth.spectrum_for_sinusoids(hfreq, hmag, hphase, Ns, fs)
mYh = 20 * np.log10(abs(Yh[:Ns / 2]))
bh = blackmanharris(Ns)
X2 = fft(fftshift(x2 * bh / sum(bh)))
Xr = X2 - Yh
mXr = 20 * np.log10(abs(Xr[:Ns / 2]))
mYst = resample(np.maximum(-200, mXr), mXr.size * stocf)  # decimate the mag spectrum

maxplotfreq = 8000.0
plt.figure(1, figsize=(9, 7))
plt.subplot(2, 1, 1)
binFreq = (fs / 2.0) * np.arange(mX.size) / (mX.size)
plt.plot(binFreq, mX, 'r', lw=1.5)
plt.axis([0, maxplotfreq, -100, max(mX) + 2])
plt.plot(hfreq, hmag, marker='x', color='b', linestyle='', lw=2, markeredgewidth=1.5)
plt.title('mX + harmonics')

plt.subplot(2, 1, 2)
binFreq = (fs / 2.0) * np.arange(mXr.size) / (mXr.size)
plt.plot(binFreq, mYh, 'r', lw=.6, label='mYh')
plt.plot(binFreq, mXr, 'r', lw=1.0, label='mXr')
binFreq = (fs / 2.0) * np.arange(mYst.size) / (mYst.size)
plt.plot(binFreq, mYst, 'r', lw=1.5, label='mYst')
plt.axis([0, maxplotfreq, -100, max(mYh) + 2])
plt.legend(prop={'size': 15})
plt.title('mYh + mXr + mYst')

plt.tight_layout()
plt.savefig('hpsModelFrame.png')

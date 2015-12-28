# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft, fftshift
from scipy.signal import hamming, triang, blackmanharris

from smst.utils import audio, peaks, synth
from smst.models import dft

(fs, x) = audio.wavread('../../../sounds/oboe-A4.wav')
M = 601
w = np.blackman(M)
N = 1024
hN = N/2
Ns = 512
hNs = Ns/2
pin = 5000
t = -70
x1 = x[pin:pin+w.size]
mX, pX = dft.fromAudio(x1, w, N)
ploc = peaks.peakDetection(mX, t)
iploc, ipmag, ipphase = peaks.peakInterp(mX, pX, ploc)
freqs = iploc*fs/N
Y = synth.genSpecSines(freqs, ipmag, ipphase, Ns, fs)
mY = 20*np.log10(abs(Y[:hNs]))
pY = np.unwrap(np.angle(Y[:hNs]))
y= fftshift(ifft(Y))*sum(blackmanharris(Ns))

plt.figure(1, figsize=(9, 6))

plt.subplot(4,1,1)
plt.plot(np.arange(-M/2,M/2), x1, 'b', lw=1.5)
plt.axis([-M/2,M/2, min(x1), max(x1)])
plt.title("x (oboe-A4.wav), M = 601")

plt.subplot(4,1,2)
plt.plot(np.arange(mX.size), mX, 'r', lw=1.5)
plt.plot(iploc, ipmag, marker='x', color='b', linestyle='', markeredgewidth=1.5)
plt.axis([0, hN,-90,max(mX)+2])
plt.title("mX + spectral peaks; Blackman, N = 1024")

plt.subplot(4,1,3)
plt.plot(np.arange(mY.size), mY, 'r', lw=1.5)
plt.axis([0, hNs,-90,max(mY)+2])
plt.title("mY; Blackman-Harris; Ns = 512")

plt.subplot(4,1,4)
plt.plot(np.arange(Ns), y, 'b', lw=1.5)
plt.axis([0, Ns,min(y),max(y)])
plt.title("y; Ns = 512")

plt.tight_layout()
plt.savefig('sine-analysis-synthesis.png')

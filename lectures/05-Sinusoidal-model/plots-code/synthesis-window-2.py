# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import ifft, fftshift
from scipy.signal import triang, blackmanharris

from smst.utils import audio, peaks, synth
from smst.models import dft

(fs, x) = audio.read_wav('../../../sounds/oboe-A4.wav')
M = 601
w = np.blackman(M)
N = 1024
hN = N / 2
Ns = 512
hNs = Ns / 2
H = Ns / 4
pin = 5000
t = -70
x1 = x[pin:pin + w.size]
mX, pX = dft.from_audio(x1, w, N)
ploc = peaks.find_peaks(mX, t)
iploc, ipmag, ipphase = peaks.interpolate_peaks(mX, pX, ploc)
freqs = iploc * fs / N
Y = synth.spectrum_for_sinusoids(freqs, ipmag, ipphase, Ns, fs)
mY = 20 * np.log10(abs(Y[:hNs]))
pY = np.unwrap(np.angle(Y[:hNs]))
y = fftshift(ifft(Y)) * sum(blackmanharris(Ns))
sw = np.zeros(Ns)
ow = triang(2 * H);
sw[hNs - H:hNs + H] = ow
bh = blackmanharris(Ns)
bh = bh / sum(bh)
sw[hNs - H:hNs + H] = sw[hNs - H:hNs + H] / bh[hNs - H:hNs + H]

plt.figure(1, figsize=(9, 6))

plt.subplot(3, 1, 1)
plt.plot(np.arange(-hNs, hNs), y, 'b', lw=1.5)
plt.plot(np.arange(-hNs, hNs), max(y) * bh / max(bh), 'k', alpha=.5, lw=1.5)
plt.axis([-hNs, hNs, min(y), max(y) + .1])
plt.title("y; size = Ns = 512 (Blackman-Harris)")

plt.subplot(3, 3, 4)
plt.plot(np.arange(-hNs, hNs), bh / max(bh), 'k', alpha=.9, lw=1.5)
plt.axis([-hNs, hNs, 0, 1])
plt.title("Blackman-Harris")

plt.subplot(3, 3, 5)
plt.plot(np.arange(-hNs / 2, hNs / 2), ow / max(ow), 'k', alpha=.9, lw=1.5)
plt.axis([-hNs / 2, hNs / 2, 0, 1])
plt.title("triangular")

plt.subplot(3, 3, 6)
plt.plot(np.arange(-hNs / 2, hNs / 2), sw[hNs - H:hNs + H] / max(sw), 'k', alpha=.9, lw=1.5)
plt.axis([-hNs, hNs, 0, 1])
plt.title("triangular / Blackman-Harris")

yw = y * sw / max(sw)
plt.subplot(3, 1, 3)
plt.plot(np.arange(-hNs, hNs), yw, 'b', lw=1.5)
plt.plot(np.arange(-hNs / 2, hNs / 2), max(y) * ow / max(ow), 'k', alpha=.5, lw=1.5)
plt.axis([-hNs, hNs, min(yw), max(yw) + .1])
plt.title("yw = y * triangular / Blackman Harris; size = Ns/2 = 256")

plt.tight_layout()
plt.savefig('synthesis-window-2.png')

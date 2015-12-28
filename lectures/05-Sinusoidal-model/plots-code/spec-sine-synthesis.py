# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hamming, triang, blackmanharris

from smst.utils import audio
from smst.models import dft

M = 255
N = 4096
hM = int(M/2.0)
fs = 44100
f0 = 5000
A0 = .9
ph = 1.5
t = np.arange(-hM,hM+1)/float (fs)
x = A0 * np.cos(2*np.pi*f0*t+ph)
w = hamming(255)
mX, pX = dft.fromAudio(x, w, N)
y = dft.toAudio(mX,pX,M)*sum(w)
freqaxis = fs*np.arange(mX.size)/float(N)
taxis = np.arange(N)/float(fs)

plt.figure(1, figsize=(9, 5))
plt.subplot(3,2,1)
plt.plot(freqaxis, mX, 'r', lw=1.5)
plt.axis([0,fs/2,-110, 0])
plt.title ('mW1; Hamming')

plt.subplot(3,2,3)
plt.plot(freqaxis, pX, 'c', lw=1.5)
plt.axis([0,fs/2,min(pX),max(pX)])
plt.title ('pW1; Hamming')

plt.subplot(3,2,5)
plt.plot(np.arange(-hM,hM+1), y[0:M], 'b', lw=1.5)
plt.axis([-hM,hM+1,-1,1])
plt.title ('y1')

w = blackmanharris(255)
mX, pX = dft.fromAudio(x, w, N)
y = dft.toAudio(mX,pX,M)*sum(w)

plt.subplot(3,2,2)
plt.plot(freqaxis, mX, 'r', lw=1.5)
plt.axis([0,fs/2,-110, 0])
plt.title ('mW2; Blackman Harris')

plt.subplot(3,2,4)
plt.plot(freqaxis, pX, 'c', lw=1.5)
plt.axis([0,fs/2,min(pX),max(pX)])
plt.title ('pW2; Blackman Harris')

plt.subplot(3,2,6)
plt.plot(np.arange(-hM,hM+1), y[0:M], 'b', lw=1.5)
plt.axis([-hM,hM+1,-1,1])
plt.title ('y2')

plt.tight_layout()
plt.savefig('spec-sine-synthesis.png')

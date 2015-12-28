import math
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hamming, triang, blackman

from smst.utils import audio, peaks, synth
from smst.models import dft, stft, sine, harmonic

(fs, x) = audio.wavread('../../../sounds/piano.wav')
w = np.blackman(1501)
N = 2048
t = -90
minf0 = 100
maxf0 = 300
f0et = 1
maxnpeaksTwm = 4
H = 128
x1 = x[1.5*fs:1.8*fs]

plt.figure(1, figsize=(9, 7))
mX, pX = stft.fromAudio(x, w, N, H)
f0 = harmonic.findFundamentalFreq(x, fs, w, N, H, t, minf0, maxf0, f0et)
f0 = peaks.cleaningTrack(f0, 5)
yf0 = synth.sinewaveSynth(f0, .8, H, fs)
f0[f0==0] = np.nan
maxplotfreq = 800.0
numFrames = int(mX[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = fs*np.arange(N*maxplotfreq/fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX[:,:N*maxplotfreq/fs+1]))
plt.autoscale(tight=True)

plt.plot(frmTime, f0, linewidth=2, color='k')
plt.autoscale(tight=True)
plt.title('mX + f0 (piano.wav), TWM')

plt.tight_layout()
plt.savefig('f0Twm-piano.png')
audio.wavwrite(yf0, fs, 'f0Twm-piano.wav')

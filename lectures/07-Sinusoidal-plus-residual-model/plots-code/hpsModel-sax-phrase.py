# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hamming, hanning, triang, blackmanharris, resample

from smst import utils
from smst.models import hps

(fs, x) = utils.wavread('../../../sounds/sax-phrase-short.wav'))
w = np.blackman(601)
N = 1024
t = -100
nH = 100
minf0 = 350
maxf0 = 700
f0et = 5
minSineDur = .1
harmDevSlope = 0.01
Ns = 512
H = Ns/4
stocf = .2
hfreq, hmag, hphase, mYst = hps.fromAudio(x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope, minSineDur, Ns, stocf)
y, yh, yst = hps.toAudio(hfreq, hmag, hphase, mYst, Ns, H, fs)

maxplotfreq = 10000.0
plt.figure(1, figsize=(9, 7))

plt.subplot(311)
plt.plot(np.arange(x.size)/float(fs), x, 'b')
plt.autoscale(tight=True)
plt.title('x (sax-phrase-short.wav)')

plt.subplot(312)
numFrames = int(mYst[:,0].size)
sizeEnv = int(mYst[0,:].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = (.5*fs)*np.arange(sizeEnv*maxplotfreq/(.5*fs))/sizeEnv
plt.pcolormesh(frmTime, binFreq, np.transpose(mYst[:,:sizeEnv*maxplotfreq/(.5*fs)+1]))

harms = hfreq*np.less(hfreq,maxplotfreq)
harms[harms==0] = np.nan
numFrames = int(harms[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
plt.plot(frmTime, harms, color='k', ms=3, alpha=1)
plt.autoscale(tight=True)
plt.title('harmonics + stochastic')

plt.subplot(313)
plt.plot(np.arange(y.size)/float(fs), y, 'b')
plt.autoscale(tight=True)
plt.title('y')

plt.tight_layout()
plt.savefig('hpsModel-sax-phrase.png')
utils.wavwrite(y, fs, 'sax-phrase-hps-synthesis.wav')
utils.wavwrite(yh, fs, 'sax-phrase-harmonic.wav')
utils.wavwrite(yst, fs, 'sax-phrase-stochastic.wav')

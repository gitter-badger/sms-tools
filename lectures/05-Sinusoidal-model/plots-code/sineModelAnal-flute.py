# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from smst import utils
from smst.models import sine, stft

(fs, x) = utils.wavread('../../../sounds/flute-A4.wav')
w = np.blackman(601)
N = 1024
H = 150
t = -80
minSineDur = .1
maxnSines = 150
mX, pX = stft.fromAudio(x, w, N, H)
tfreq, tmag, tphase = sine.fromAudio(x, fs, w, N, H, t, maxnSines, minSineDur)

plt.figure(1, figsize=(9.5, 5))
maxplotfreq = 5000.0
maxplotbin = int(N*maxplotfreq/fs)
numFrames = int(mX[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(maxplotbin+1)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX[:,:maxplotbin+1]))
plt.autoscale(tight=True)

tracks = tfreq*np.less(tfreq, maxplotfreq)
tracks[tracks<=0] = np.nan
plt.plot(frmTime, tracks, color='k', lw=1.5)
plt.autoscale(tight=True)
plt.title('mX + sinusoidal tracks (flute-A4.wav)')

plt.tight_layout()
plt.savefig('sineModelAnal-flute.png')

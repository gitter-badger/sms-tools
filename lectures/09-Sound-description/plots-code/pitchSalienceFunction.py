import essentia
import essentia.standard as ess
# matplotlib without any blocking GUI
import matplotlib as mpl

mpl.use('Agg')
from pylab import *
from numpy import *

filename = '../../../sounds/orchestra.wav'
fs = 44100
H = 1024
M = 2048
N = 2 * M
guessUnvoiced = True

window = ess.Windowing(type='hann', zeroPadding=N - M)
spectrum = ess.Spectrum(size=N)
spectralPeaks = ess.SpectralPeaks(minFrequency=50, maxFrequency=10000, maxPeaks=100, sampleRate=fs,
                                  magnitudeThreshold=0, orderBy="magnitude")
pitchSalienceFunction = ess.PitchSalienceFunction()
pitchSalienceFunctionPeaks = ess.PitchSalienceFunctionPeaks(minFrequency=100, maxFrequency=300)

x = ess.MonoLoader(filename=filename, sampleRate=fs)()
x = ess.EqualLoudness()(x)
totalSaliences = []

for frame in ess.FrameGenerator(x, frameSize=M, hopSize=H):
    frame = window(frame)
    mX = spectrum(frame)
    peak_frequencies, peak_magnitudes = spectralPeaks(mX)
    pitchSalienceFunction_vals = pitchSalienceFunction(peak_frequencies, peak_magnitudes)
    salience_peaks_bins_vals, salience_peaks_saliences_vals = pitchSalienceFunctionPeaks(pitchSalienceFunction_vals)
    totalSaliences.append(max(salience_peaks_saliences_vals))

totalSaliences = np.array(totalSaliences)

plt.figure(1, figsize=(9.5, 7))
plt.subplot(2, 1, 1)

plt.plot(np.arange(x.size) / float(fs), x)
plt.axis([0, x.size / float(fs), min(x), max(x)])
plt.ylabel('amplitude')
plt.title('x (orchestra.wav)')

plt.subplot(2, 1, 2)
frmTime = H * np.arange(totalSaliences.size) / float(fs)
plot(frmTime, totalSaliences, color='c', linewidth=1.5)
plt.axis([0, x.size / float(fs), min(totalSaliences), max(totalSaliences)])
plt.ylabel('max pitch salience')
plt.title('pitch salience')

tight_layout()
savefig('pitchSalienceFunction.png')

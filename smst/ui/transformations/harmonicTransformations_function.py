# function call to the transformation functions of relevance for the hpsModel

import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import get_window

from smst.utils import audio, files
from smst.models import sine, harmonic
from .. import demo_sound_path


def analysis(inputFile=demo_sound_path('vignesh.wav'), window='blackman', M=1201, N=2048, t=-90,
             minSineDur=0.1, nH=100, minf0=130, maxf0=300, f0et=7, harmDevSlope=0.01,
             interactive=True, plotFile=False):
    """
    Analyze a sound with the harmonic model
    inputFile: input sound file (monophonic with sampling rate of 44100)
    window: analysis window type (rectangular, hanning, hamming, blackman, blackmanharris)
    M: analysis window size
    N: fft size (power of two, bigger or equal than M)
    t: magnitude threshold of spectral peaks
    minSineDur: minimum duration of sinusoidal tracks
    nH: maximum number of harmonics
    minf0: minimum fundamental frequency in sound
    maxf0: maximum fundamental frequency in sound
    f0et: maximum error accepted in f0 detection algorithm
    harmDevSlope: allowed deviation of harmonic tracks, higher harmonics have higher allowed deviation
    returns inputFile: input file name; fs: sampling rate of input file, tfreq,
                        tmag: sinusoidal frequencies and magnitudes
    """

    # size of fft used in synthesis
    Ns = 512

    # hop size (has to be 1/4 of Ns)
    H = 128

    # read input sound
    fs, x = audio.read_wav(inputFile)

    # compute analysis window
    w = get_window(window, M)

    # compute the harmonic model of the whole sound
    hfreq, hmag, hphase = harmonic.from_audio(x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope, minSineDur)

    # synthesize the sines without original phases
    y = sine.to_audio(hfreq, hmag, np.array([]), Ns, H, fs)

    # output sound file (monophonic with sampling rate of 44100)
    outputFile = 'output_sounds/' + os.path.basename(inputFile)[:-4] + '_harmonicModel.wav'

    # write the sound resulting from the inverse stft
    audio.write_wav(y, fs, outputFile)

    # create figure to show plots
    plt.figure(figsize=(12, 9))

    # frequency range to plot
    maxplotfreq = 5000.0

    # plot the input sound
    plt.subplot(3, 1, 1)
    plt.plot(np.arange(x.size) / float(fs), x)
    plt.axis([0, x.size / float(fs), min(x), max(x)])
    plt.ylabel('amplitude')
    plt.xlabel('time (sec)')
    plt.title('input sound: x')

    if (hfreq.shape[1] > 0):
        plt.subplot(3, 1, 2)
        tracks = np.copy(hfreq)
        numFrames = tracks.shape[0]
        frmTime = H * np.arange(numFrames) / float(fs)
        tracks[tracks <= 0] = np.nan
        plt.plot(frmTime, tracks)
        plt.axis([0, x.size / float(fs), 0, maxplotfreq])
        plt.title('frequencies of harmonic tracks')

    # plot the output sound
    plt.subplot(3, 1, 3)
    plt.plot(np.arange(y.size) / float(fs), y)
    plt.axis([0, y.size / float(fs), min(y), max(y)])
    plt.ylabel('amplitude')
    plt.xlabel('time (sec)')
    plt.title('output sound: y')

    plt.tight_layout()

    if interactive:
        plt.show(block=False)
    if plotFile:
        plt.savefig('output_plots/%s_harmonic_transformation_analysis.png' % files.strip_file(inputFile))

    return inputFile, fs, hfreq, hmag


def transformation_synthesis(inputFile, fs, hfreq, hmag, freqScaling=np.array([0, 2.0, 1, .3]),
                             freqStretching=np.array([0, 1, 1, 1.5]), timbrePreservation=1,
                             timeScaling=np.array([0, .0, .671, .671, 1.978, 1.978 + 1.0]),
                             interactive=True, plotFile=False):
    """
    Transform the analysis values returned by the analysis function and synthesize the sound
    inputFile: name of input file
    fs: sampling rate of input file
    tfreq, tmag: sinusoidal frequencies and magnitudes
    freqScaling: frequency scaling factors, in time-value pairs
    freqStretchig: frequency stretching factors, in time-value pairs
    timbrePreservation: 1 preserves original timbre, 0 it does not
    timeScaling: time scaling factors, in time-value pairs
    """

    # size of fft used in synthesis
    Ns = 512

    # hop size (has to be 1/4 of Ns)
    H = 128

    # frequency scaling of the harmonics
    yhfreq, yhmag = harmonic.scale_frequencies(hfreq, hmag, freqScaling, freqStretching, timbrePreservation, fs)

    # time scale the sound
    yhfreq, yhmag = sine.scale_time(yhfreq, yhmag, timeScaling)

    # synthesis
    y = sine.to_audio(yhfreq, yhmag, np.array([]), Ns, H, fs)

    # write output sound
    outputFile = 'output_sounds/' + os.path.basename(inputFile)[:-4] + '_harmonicModelTransformation.wav'
    audio.write_wav(y, fs, outputFile)

    # create figure to plot
    plt.figure(figsize=(12, 6))

    # frequency range to plot
    maxplotfreq = 15000.0

    # plot the transformed sinusoidal frequencies
    plt.subplot(2, 1, 1)
    if (yhfreq.shape[1] > 0):
        tracks = np.copy(yhfreq)
        tracks = tracks * np.less(tracks, maxplotfreq)
        tracks[tracks <= 0] = np.nan
        numFrames = int(tracks[:, 0].size)
        frmTime = H * np.arange(numFrames) / float(fs)
        plt.plot(frmTime, tracks)
        plt.title('transformed harmonic tracks')
        plt.autoscale(tight=True)

    # plot the output sound
    plt.subplot(2, 1, 2)
    plt.plot(np.arange(y.size) / float(fs), y)
    plt.axis([0, y.size / float(fs), min(y), max(y)])
    plt.ylabel('amplitude')
    plt.xlabel('time (sec)')
    plt.title('output sound: y')

    plt.tight_layout()

    if interactive:
        plt.show()
    if plotFile:
        plt.savefig('output_plots/%s_harmonic_transformation_synthesis.png' % files.strip_file(inputFile))


def main(interactive=True, plotFile=False):
    # analysis
    inputFile, fs, hfreq, hmag = analysis(interactive=interactive, plotFile=plotFile)

    # transformation and synthesis
    transformation_synthesis(inputFile, fs, hfreq, hmag, interactive=interactive, plotFile=plotFile)


if __name__ == "__main__":
    main()

import copy
import os
import subprocess
import sys

import numpy as np
from scipy.io.wavfile import write, read

from .files import ensure_directory

winsound_imported = False
if sys.platform == "win32":
    try:
        import winsound

        winsound_imported = True
    except:
        print "You won't be able to play sounds, winsound could not be imported"

INT16_FAC = (2 ** 15) - 1
INT32_FAC = (2 ** 31) - 1
INT64_FAC = (2 ** 63) - 1
norm_fact = {'int16': INT16_FAC, 'int32': INT32_FAC, 'int64': INT64_FAC, 'float32': 1.0, 'float64': 1.0}


def read_wav(filename):
    """
    Read a sound file and convert it to a normalized floating point array
    filename: name of file to read
    returns fs: sampling rate of file, x: floating point array
    """

    if not os.path.isfile(filename):  # raise error if wrong input file
        raise ValueError("Input file is wrong")

    fs, x = read(filename)

    if len(x.shape) != 1:  # raise error if more than one channel
        raise ValueError("Audio file should be mono")

    if fs != 44100:  # raise error if more than one channel
        raise ValueError("Sampling rate of input sound should be 44100")

    # scale down and convert audio into floating point number in range of -1 to 1
    x = np.float32(x) / norm_fact[x.dtype.name]
    return fs, x


def play_wav(filename):
    """
    Play a wav audio file from system using OS calls
    filename: name of file to read
    """
    if not os.path.isfile(filename):  # raise error if wrong input file
        print("Input file does not exist. Make sure you computed the analysis/synthesis")
    else:
        if sys.platform == "linux" or sys.platform == "linux2":
            # linux
            subprocess.call(["aplay", filename])

        elif sys.platform == "darwin":
            # OS X
            subprocess.call(["afplay", filename])
        elif sys.platform == "win32":
            if winsound_imported:
                winsound.PlaySound(filename, winsound.SND_FILENAME)
            else:
                print("Cannot play sound, winsound could not be imported")
        else:
            print("Platform not recognized")


def write_wav(y, fs, filename):
    """
    Write a sound file from an array with the sound and the sampling rate.
    Creates the directory for the file if it does not exist.
    y: floating point array of one dimension, fs: sampling rate
    filename: name of file to create (can be a path)
    """

    dir = os.path.dirname(filename)
    ensure_directory(dir)

    x = copy.deepcopy(y)  # copy array
    x *= INT16_FAC  # scaling floating point -1 to 1 range signal to int16 range
    x = np.int16(x)  # converting to int16 type
    write(filename, fs, x)

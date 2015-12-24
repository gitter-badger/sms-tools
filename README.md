# Spectral Modeling Synthesis Tools

[SMS Tools](http://mtg.upf.edu/technologies/sms) is a set of techniques and software implementations for the analysis, transformation and synthesis of musical sounds based on various spectral modeling approaches. These techniques can be used for synthesis, processing and coding applications, while some of the intermediate results might also be applied to other music related problems, such as sound source separation, musical acoustics, music perception, or performance analysis. The basic model and implementation was developed in the PhD thesis by X. Serra in 1989 and since then many extensions have been proposed at [MTG-UPF](http://mtg.upf.edu/) and by other researchers.

This repository contains a library written in Python (with a bit of C) and complementary lecture materials for the [Audio Signal Processing for Music Applications](https://www.coursera.org/course/audio) course.

## Project structure

- `smst` - the SMS tools Python package
  - `models` - code for models that can represent sounds
  - `transformations` - code for transforming sounds
  - `ui` - command-line and graphical interface for demo purposes
    - `models`
    - `transformations`
- `tests` - automated tests
- `lectures` - lecture slides + code to generate the plots and other resources
- `sounds` - selected example sounds from Freesound used in the course
- `workspace` - place for student assignments

## Requirements

- Python 2.7
- numpy - numerical computations
- scipy - other scientific computations
- matplotlib - plotting
- cython - for some parts written in C

Optional:

- ipython - interactive notebook
- [essentia](http://essentia.upf.edu/) - audio features extraction

## How to install?

## This repository

If you have `git` installed, just clone the repository:

```
git clone https://github.com/MTG/sms-tools.git
```

Otherwise [download the current version as a ZIP](https://github.com/MTG/sms-tools/archive/master.zip) and extract it.

At present, SMS tools are not available as a Python package, eg. via PyPI.

## Python & its packages

The easiest and free way to install a working Python environment is [Anaconda](https://www.continuum.io/downloads). It has most of the required dependendies already bundled. However, you can also try the packages provided by you platform's native package system (apt, brew, etc.).

### Ubuntu

In Ubuntu (which we strongly recommend) in order to install all these modules it is as simple as typing in the Terminal:

```
$ sudo apt-get install python-dev ipython python-numpy python-matplotlib python-scipy cython
```

### Mac OS X

In OSX (which we do not support but that should work) you install these modules by typing in the Terminal:

```
$ pip install ipython numpy matplotlib scipy cython
```

### General

Then, for using the tools, after downloading the whole package, you need to compile some C functions.

```
sms-tools$ cd smst/models/utilFunctions_C
$ python compileModule.py build_ext --inplace
```

## How to use?

### Models GUI

The basic sound analysis/synthesis functions, or models, are in the directory `smst/models` and there is a graphical interface and individual example functions in `smst/ui/models`. To execute the models GUI type:

```
sms-tools$ cd smst/ui/models
$ python models_GUI.py
```

### Transformations GUI

To execute the transformations GUI that calls various sound transformation functions type:

```
sms-tools$ cd smst/ui/transformations
$ python transformations_GUI.py
```

### Coding projects/assignments

To modify the existing code, or to create your own using some of the functions, we recommend to use the `workspace` directory. Typically you would copy a file from `smst/ui/models` or from `smst/ui/transformations` to that directory, modify the code, and execute it from there (you will have to change some of the paths inside the files).

Look at the many examples of usage of the library in `smst/ui/*` and in `lectures/*/plots-code`. Also do not be afraid to look at the library sources.

## Available models and transformations

### Models

A model provides a different representation of audio than the time-domain samples.

- [Discrete Fourier Transform](smst/models/dftModel.py) - spectrum of a single frame
- [Short-time Fourier Transform](smst/models/stft.py) - spectrogram
- [Sinusoidal model](smst/models/sineModel.py) - for plain tones
- [Harmonic model](smst/models/harmonicModel.py) - for harmonic tones
- [Stochastic model](smst/models/stochasticModel.py) - for noises
- [Sinusoidal + residual model](smst/models/sprModel.py)
- [Sinusoidal + stochastic model](smst/models/spsModel.py)
- [Harmonic + residual model](smst/models/hprModel.py)
- [Harmonic + stochastic model](smst/models/hpsModel.py)

### Transformations

Audio can be transformed by modifying its model.

- [STFT transformations](smst/transformations/stftTransformations.py)
- [Sinusoidal transformations](smst/transformations/sineTransformations.py)
- [Harmonic transformations](smst/transformations/harmonicTransformations.py)
- [Stochastic transformations](smst/transformations/stochasticTransformations.py)
- [Harmonic + stochastic transformations](smst/transformations/hpsTransformations.py)

## Authors

The [people](AUTHORS) who contributed to this software.

## License

All the software is distributed with the [Affero GPL license](http://www.gnu.org/licenses/agpl-3.0.en.html), the lecture slides are distributed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0) license and the sounds in this repository are released under [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license.

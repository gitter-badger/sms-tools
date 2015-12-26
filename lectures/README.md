# ASPMA Lectures

This directory includes the slides (ODT) and resources for lectures of the
[Audio Signal Processing for Music Applications
](https://www.coursera.org/course/audio)
course by prof. Xavier Serra.

Besides the slides there's a Python code which generates the plots and
other resources (eg. sounds) used in the slides.

## Hot to generate the resources?

The code uses sms-tools installed as a Python package `smst`.

Additional requirements (for lecture 09):

- `essentia` (python binding package)

The python code for each lecture is in its `plots-code` subdirectory. All the
scripts except to be ran from their directory.

You can either run each script separately or run all of them automatically.

### Running a single script

Example:

```
$ cd lectures/02-DFT/plots-code/
$ python complex-sinewaves.py
# produces: lectures/02-DFT/plots-code/complex-sinewaves.png
```

### Running all the scripts

There's a simple tool which allows to run all the scripts (each in its own
directory). Note that this may take a lot of time (eg. 10 minutes on a MacBook).

In order to download sounds from Freesound, provide the API key via the
`FREESOUND_API_KEY` environment variable before running the tool. For
convenience save the following line to you `~/.profile` or `~/.bash_profile`
and reload it.

```
export FREESOUND_API_KEY="your own private API key obtained at freesound.org"
```

Generate all the resources at once.

```
$ cd lectures/
$ python make.py plots
```

Also it is able to clean all the generated outputs.

```
lectures$ python make.py clean
```

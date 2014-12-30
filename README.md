sms-tools
========= 

Sound analysis/synthesis tools for music applications written in python (with a bit of C) plus complementary lecture materials.

How to use
----------

In order to use these tools you have to install Python and the following modules: ipython, numpy, matplotlib, scipy, pygame, and cython.

The original code was written for Python 2.7. This branch is converted (via 2to3) to work with the latest Python 3 and be possibly compatible with Python 2.7.

In Ubuntu (which we strongly recommend) in order to install all these modules it is as simple as typing in the Terminal:

<code>$ sudo apt-get install python-dev ipython python-numpy python-matplotlib python-scipy python-pygame cython</code>

On Mac OS X you need Python 3, tkinter, SDL, [XQuartz](http://xquartz.macosforge.org/landing/) (eg. XQuartz-2.7.7.dmg). Pygame It works fine with Python 3.4 on OS X Yosemite. Creating a separate Python virtual environment ([pyvenv](https://docs.python.org/3/library/venv.html)) is recommended.

```
sudo port install libsdl-framework libsdl_ttf-framework libsdl_image-framework libsdl_mixer-framework mercurial py34-tkinter
pip install ipython readline Cython matplotlib numpy scipy
pip install hg+http://bitbucket.org/pygame/pygame
```

Hack: get the tkinter module to the proper Python path (one level higher) ([more info](http://bohumirzamecnik.cz/blog/2014/install-tkinter-with-python-3-on-mac/)).
```
TKMODULE=$(port contents py34-tkinter|grep _tkinter.so)
sudo ln -s $TKMODULE $(echo $TKMODULE|sed 's/site-packages\///')
```

then for using the tools, after downloading the whole package, you need to compile some C functions. For that you should go to the directory <code>software/models/utilFunctions_C</code> and type:</p>

<code>$ python compileModule.py build_ext --inplace </code>

The basic sound analysis/synthesis functions, or models, are in the directory <code>software/models</code> and there is a graphical interface and individual example functions in <code>software/models_interface</code>. To execute the models GUI you have to go to the directory <code>software/models_interface</code> and type: 

<code>$ python models_GUI.py </code>

To execute the transformations GUI that calls various sound transformation functions go to the directory <code>software/transformations_interface</code> and type: 

<code>$ python transformations_GUI.py </code>

To modify the existing code, or to create your own using some of the functions, we recommend to use the <code>workspace</code> directory. Typically you would copy a file from <code>software/models_interface</code> or from <code>software/transformations_interface</code> to that directory, modify the code, and execute it from there (you will have to change some of the paths inside the files). 


Content
-------

All the code is in the <code> software </code> directory, with subdirectories for the models, the transformations, and the interfaces. The lecture material is in the <code>lecture</code> directory and the sounds used for the examples and coming from <code>http://freesound.org</code> are in the <code>sounds</code> directory.

License
-------
All the software is distributed with the Affero GPL licence, and the lecture slides and sounds are distributed with the Creative Commons Attribution-Noncommercial-Share Alike license.


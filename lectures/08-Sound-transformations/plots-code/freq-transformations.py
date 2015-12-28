import numpy as np
# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os

from smst.models import dft
import smst.utils as utils

f0 = 1.0
harms = np.arange(1,6)*f0
freqtransp = harms*2
freqshift = harms + .5
freqstretch = (harms/np.arange(1,6)) * (np.arange(1,6)**1.3)

plt.figure(1, figsize=(9, 7))
plt.subplot(2,2,1)
plt.vlines(harms, 0, 1, color='r', lw=1.2)
plt.axis([0,f0*10,0,1])
plt.title('original harmonics')

plt.subplot(2,2,2)
plt.vlines(freqtransp, 0, 1, color='r', lw=1.2)
plt.axis([0,f0*10,0,1])
plt.title('frequency transposition by 2.0')

plt.subplot(2,2,3)
plt.vlines(freqshift, 0, 1, color='r', lw=1.2)
plt.axis([0,f0*10,0,1])
plt.title('frequency shifting by 0.5')

plt.subplot(2,2,4)
plt.vlines(freqstretch, 0, 1, color='r', lw=1.2)
plt.axis([0,f0*10,0,1])
plt.title('frequency stretching by 1.3')


plt.tight_layout()
plt.savefig('freq-transformations.png')

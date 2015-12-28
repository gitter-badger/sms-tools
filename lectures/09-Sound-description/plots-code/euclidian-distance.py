# matplotlib without any blocking GUI
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def eucDist(vec1, vec2):
  return np.sqrt(np.sum(np.power(np.array(vec1) - np.array(vec2), 2)))

vec1 = np.array([.3, .2])
vec2 = np.array([.6, .7])

plt.figure(1, figsize=(4, 3))

plt.scatter(vec1[0], vec1[1], c = 'r', s=50, hold = True, alpha=0.75)
plt.scatter(vec2[0], vec2[1], c = 'b', s=50, hold = True, alpha=0.75)
plt.plot([vec1[0], vec2[0]], [vec1[1], vec2[1]], 'k')
plt.ylabel('first dimension', fontsize =16)
plt.xlabel('second dimension', fontsize =16)


plt.tight_layout()
plt.savefig('euclidian-distance.png')

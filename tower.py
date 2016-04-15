#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

t, v = np.loadtxt('droptower_vdata.txt', unpack=True)
x = integrate.cumtrapz(v, t, initial=0)
a = np.diff(v)

a = a.itemset(0)
print(len(a), len(x), len(v))
#plt.plot(v,t, x,t, a,t)
plt.show()
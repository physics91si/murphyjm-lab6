#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

t, v = np.loadtxt('droptower_vdata.txt', unpack=True)
x = integrate.cumtrapz(v, t, initial=0)
a = list(np.diff(v))

a = [0] + a

z = (x, v, a)
labels = ('position', 'velocity', 'acceleration')

for y, name in zip(z, labels):
	plt.plot(t,y, label=name)

plt.legend()
plt.title('Droptower Kinematics')
plt.show()
#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

t, v = np.loadtxt('droptower_vdata.txt', unpack=True)
x = integrate.cumtrapz(v, t, initial=0)
diffs = list(np.diff(v))

dt = t[1] - t[0]
a = []
a.append(diffs[0]/dt)
for dv in diffs:
	a.append(dv/dt)

z = (x, v, a)
labels = ('position', 'velocity', 'acceleration')

for y, name in zip(z, labels):
	plt.plot(t,y, label=name)

x_axis = np.zeros(len(x))
plt.plot(t, x_axis, '--')
plt.legend()
plt.title('Droptower Kinematics')

a = [elem for elem in a if elem > 0] # Filter out acceleration values < 0
sum_a = np.sum(a)
avg_a = sum_a/len(a)
print('Average upward acceleration = %f\n') %avg_a

plt.show()
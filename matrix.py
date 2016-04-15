#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from pylab import savefig

def main():
	n = 9
	arr = np.zeros((n,n))

	arr[:,0:3] = 1
	arr[n-1, :]  = 1
	arr[(4,7,1),(5,7,8)] = 1

	plt.spy(arr)
	savefig('arr_plot.png')
	plt.show()

main()
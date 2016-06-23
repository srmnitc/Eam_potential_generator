#code to write eam potential for Ni.
#based on "Application of embedded-atom method to liquid transition metals", SM Foiles 1985, PhyRevB 32/6 
#written by SRM
#calculation of embed function
#more explanations on functions used here can be found at 10.1103/PhysRevB.29.6443 

import numpy as np
import globalsvals as gb
import scipy as sp
import pylab as plt
from scipy.interpolate import interp1d
import sys

#note that the input parameters are values of atomic density calculated
def embed_fn():
	
	x = gb.rho
	y = gb.f_rho
	new_length = gb.nrno
	
	
	dd = gb.maxrho/500.00 
	new_x = np.linspace(x.min(), new_length*dd, new_length)
	new_y = np.zeros(len(new_x))

	tr =0
	for i in range(len(new_x)):
		#normal cubic spline interpolation for values withn range
		if (new_x[i] <= 0.06650):
			new_y[i] = sp.interpolate.interp1d(x, y, kind='cubic')(new_x[i])
		#linear interpolation depending on the slope of last knot for the values out of range
		else:
			if(tr==0):
				xbrutus = new_x[i-1]-new_x[i-2]
				ybrutus = new_y[i-1]-new_y[i-2]
				slope = ybrutus/xbrutus
				c = new_y[i-1] - slope*new_x[i-1]
				tr = 1
			new_y[i] = slope*new_x[i] + c
			print new_y[i]

	return new_y,dd


if __name__ == '__main__':
	print "write test block"

#code to write eam potential for Ni.
#based on "Application of embedded-atom method to liquid transition metals", SM Foiles 1985, PhyRevB 32/6 
#written by SRM
#calculation of atomic density
#more explanations on functions used here can be found at 10.1103/PhysRevB.29.6443

import numpy as np
import globalsvals as gb
import sys

def atomic_density(rr):

	rho_s = calc_rho(gb.cs,gb.ns,gb.chis,rr)
	rho_d = calc_rho(gb.cd,gb.nd,gb.chid,rr)
	return rho_s,rho_d


#sub function to calculate R_i
def calc_capri(n,chi,rr):
	fact1 = (2*chi)**(n+0.5)
	fact2 = (np.math.factorial(2*n))**0.5
	fact3 =  rr**(n-1)*np.exp(-chi*rr)
	return fact1*fact3/fact2

#function to claculate rho
def calc_rho(c,n,chi,rr):
	#dummy to store capital r values
	cap_r = np.zeros(len(chi))
	#loop over chi values 
	for i in range(len(chi)):
		cap_r[i] = calc_capri(n[i],chi[i],rr)

	#array of rho
	rho_arr = cap_r*c

	return ((1/(4.00*np.pi))*np.sum(rho_arr)*np.sum(rho_arr))

if __name__=="__main__":
	rr = float(sys.argv[1])
	t1,t2 = atomic_density(rr)
	t = gb.Ns*t1 + gb.Nd*t2
	print t



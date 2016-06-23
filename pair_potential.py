#code to write eam potential for Ni.
#based on "Application of embedded-atom method to liquid transition metals", SM Foiles 1985, PhyRevB 32/6 
#written by SRM
#calculation of pair potential
#functional form is from the paper mentioned above

import numpy as np
import globalsvals as gb
import sys

def pair_potential(rr):
	#pair potential cutoff is rc
	if (rr<gb.rc):
	    #This value is square of effective charge
	    z_sqr = gb.a1*(gb.rc-rr)**3 + gb.a2*(gb.rc-rr)**4
	    #convert e2 to eV. Angstrom
	    dummy1 = z_sqr*14.399764
	    #convert to bohr hartree read by lammps
	    dummy1 = dummy1/(27.2*0.529)
	    #take square root, because lammps reads values as phi*r = zi*zj
	    dummy1 = dummy1**0.5
	
	    return dummy1
	else:
		return 0

if __name__=="__main__":
	rr=float(sys.argv[1])
	test = pair_potential(rr)
	print test


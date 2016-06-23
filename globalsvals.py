
#code to write eam potential for Ni.
#based on "Application of embedded-atom method to liquid transition metals", SM Foiles 1985, PhyRevB 32/6 
#written by SRM
#file for all parameters

#refernce for atomic density data
#http://journals.aps.org/prb/pdf/10.1103/PhysRevB.29.6443

import numpy as np

#contains details for Ni
#----------------------------------------------------------------
#general potential details
#comments to be added
cmmt = 'Test'
#atomic number
atomno = 28
#atomic weight
atomwt = 58.710
#lattice parameter
latpar = 3.5200
#crystal structure
xtal = "FCC"
#nrho : no of values of emb energy
nrno = 500
#nr : no of values of pair potential
nr = 500
#dr : step width of rr values
dr = 9.6969696969697039e-03
#drho : spacing in density to calculate f_rho_values
drho = 5.0100200400801306e-04
#cutoff value
cutoff = 5.5000000000000114e+00
#max rho value
maxrho = 0.25


#----------------------------------------------------------------
#for atomic density
#total number of outer electrons
N = 10
#Ns measure of electrons in outer s orbitals
Ns = 0.86
#Nd measure of electrons in outer d orbitals
Nd = N-Ns
#s orbital details
#array for n
ns = np.array([1,1,2,2,3,3,4,4])
#array for chi values
chis = np.array([54.88885,38.48431,27.42703,20.88204,10.95707,7.31958,3.92650,2.15289])
#array for expansion coefficients
cs = np.array([-0.00389,-0.02991,-0.03189,0.15289,-0.20048,-0.05423,0.49292,0.61875])
#d orbital details

#array for n
nd = np.array([3,3])
#array for chi values
chid = np.array([12.67582,5.43253])
#array for expansion coefficients
cd = np.array([0.42120,0.70658])


#-------------------------------------------------------------------
#for pair potential
#equation is a1*(rc-r)**3 + a2*(rc-r)**4
a1 = 0.070937
a2 = 0.146031
rc = 3.0045


#---------------------------------------------------------------------
#spline and knots for embedding energy
#rho
rho = np.array([0.0,0.01446,0.02891,0.05783,0.06650])
f_rho = np.array([0.0,-3.5847,-5.1449,-3.4041,0.0])


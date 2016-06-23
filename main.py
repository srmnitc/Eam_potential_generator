#code to write eam potential for Ni.
#based on "Application of embedded-atom method to liquid transition metals", SM Foiles 1985, PhyRevB 32/6 
#written by SRM
#main file
#23.06.16

import numpy as np
import atomic_density as ad
import pair_potential as pp
import embed_function as ef
import globalsvals as gb


#all constats are imported from globalvals
r_start = 0;
#create an array of r values
r_array = np.linspace(0.00,gb.cutoff,gb.nr)
dr = r_array[1] - r_array[0]
rhos = np.zeros(gb.nr)
rhod = np.zeros(gb.nr)
zarr = np.zeros(gb.nr)

#calculate density for r values
for i in range(len(r_array)):
	#density is calculated here
	rhos[i],rhod[i] = ad.atomic_density(r_array[i])
	#pair potential is calculated here
	zarr[i] = pp.pair_potential(r_array[i])

#embedding function calculated here
frho,drho = ef.embed_fn()

#calc final density values
rho = np.zeros(gb.nr)
rho = gb.Nd*rhod + gb.Ns*rhos



#writing in the file in lammps format
#	nAME OF potential file
fout = open('Ni_u3.eam','w')
#first line comment
fout.write(gb.cmmt)
fout.write("\n")
#second line : atom no, atom wt, lattice parameter, xtal structure
fout.write(("{:d}    {:.3f}   {:.3f}    {}\n").format(gb.atomno,gb.atomwt,gb.latpar,gb.xtal))
#no of frho vales, rho spacing for frho, no of dr values, r spacing, cutoff for the potential
fout.write(("{:d}    {:1.16e}    {:d}    {:1.16e}    {:1.16e}\n").format(gb.nrno,drho,gb.nr,dr,gb.cutoff))

#write frho tabulated values
for j in range(0,gb.nrno/5):
	fout.write(("{:1.16e} {:1.16e} {:1.16e} {:1.16e} {:1.16e}\n").format(frho[j*5],frho[j*5+1],frho[j*5+2],frho[j*5+3],frho[j*5+4]))
#write pair pot tabulated values
for j in range(0,gb.nr/5):
	fout.write(("{:1.16e} {:1.16e} {:1.16e} {:1.16e} {:1.16e}\n").format(zarr[j*5],zarr[j*5+1],zarr[j*5+2],zarr[j*5+3],zarr[j*5+4]))
#write atom density tabulated values
for j in range(0,gb.nr/5):
	fout.write(("{:1.16e} {:1.16e} {:1.16e} {:1.16e} {:1.16e}\n").format(rho[j*5],rho[j*5+1],rho[j*5+2],rho[j*5+3],rho[j*5+4]))

fout.close()

#Use this block if individual values should be output for debugging
"""
#print it out
np.savetxt('rho.dat',rho,fmt='%1.16e')
np.savetxt('frho.dat',frho,fmt='%1.16e')
np.savetxt('zarr.dat',zarr,fmt='%1.16e')
np.savetxt('const.dat',dum1,fmt='%1.16e')
np.savetxt('dist.dat',r_array,fmt='%1.16e')

"""
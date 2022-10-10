#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                 				#for path to external scripts
sys.path.insert(0,'/home/manideep/FWC/Matrices/Conic/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Input parameters
c = np.matrix('0,3')		#center of circle

V = np.matrix('9,0;0,16')	
l,P = np.linalg.eigh(V)		#l-eigen_values & v-eigen_vector
f = -V[0,0]*V[1,1]

l1 = l[0]	#lambda_1
l2 = l[1]	#lambda_2

P1 = P[0].T	#eigenvector_1
P2 = P[1].T	#eigenvector_2

e = np.sqrt(1-(l1/l2))			#eccentricity
n = np.sqrt(l2)*P1			#normal to diretrix
k = np.sqrt(-(l2*((e*e)-1)*(-l2*f)))/(l2*e*((e*e)-1))	#constant
F = (k*e*e*n)/l2			#Focus of ellpise
r = LA.norm(c-F.T)

print('Radius of the Circle is',r)


A = np.array([-np.sqrt(l2),0])
B = np.array([np.sqrt(l2),0])
C = np.array([0,np.sqrt(l1)])
D = np.array([0,-np.sqrt(l1)])
m = float(F[0])
F = np.array([m,0])

#Generating the circle
x_circ = circ_gen(C,r)

#Generating the ellipse
x_ellipse = ellipse_gen(np.sqrt(l2),np.sqrt(l1))

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')

#Plotting the ellipse
plt.plot(x_ellipse[0,:],x_ellipse[1,:],label='$Ellipse$')

#Generating all lines
xAB = line_gen(A,B)
xCD = line_gen(C,D)
xCF = line_gen(C,F)

#Plotting all lines
plt.plot(xAB[0,:],xAB[1,:],label='Major Axis')
plt.plot(xCD[0,:],xCD[1,:],label='Minor Axis')
plt.plot(xCF[0,:],xCF[1,:],label='Radius')


#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,F)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','F']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='upper left')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/FWC/Matrices/Conic/conicp.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard/FWC/Matrices/Conic/conicp.pdf'"))
#else
#plt.show()


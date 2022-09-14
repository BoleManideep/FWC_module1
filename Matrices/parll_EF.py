import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

def dir_vec(A,B):
   return B-A
 

def norm_vec(A,B):
   return np.matmul(omat, dir_vec(A,B))

#if using termux
import subprocess
import shlex
#end if


#input parameters
k=2
l=2
x=2
A = np.array([0,-1])
B = np.array([4,-1])
D = np.array([1.5,1])
C = np.array([5.5,1])

P = np.array([2,0])

#E = np.array([0.75,0])
#F = np.array([4.75,0])

##Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

x_PA = line_gen(P,A)
x_PB = line_gen(P,B)
x_PC = line_gen(P,C)
x_PD = line_gen(P,D)

#x_EF = line_gen(E,F)

#Pliotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_DA[0,:],x_DA[1,:])

plt.plot(x_PA[0,:],x_PA[1,:])
plt.plot(x_PB[0,:],x_PB[1,:])
plt.plot(x_PC[0,:],x_PC[1,:])
plt.plot(x_PD[0,:],x_PD[1,:])

#plt.plot(x_EF[0,:],x_EF[1,:])

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-2.pdf')
#subprocess.run(shlex.split("termux-open '/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-2.pdf'")) 
#else
plt.show()

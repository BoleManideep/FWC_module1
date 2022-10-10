import matplotlib.pyplot as plt
import numpy as np

#if using termux
import subprocess
import shlex
#end if

def f(x,a,b,c):
    return a*x**2+b*x+c

label_str = "$-x^2 + 2x +9$"

def df(x):
    return 2*a*x+b

a = -1
b = 2
c = 9

label_str = "$-x^2 + 2x +9$"


#For minima using gradient ascent
cur_x = 1
alpha = 0.001 
precision = 0.000000001 
previous_step_size = 1
max_iters = 100000000 
iters = 100000

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x,a,b,c)
print("<Maximum value of f(x) is", min_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,a,b,c)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()

#plt.savefig('/sdcard/Download/.pdf')
plt.show()

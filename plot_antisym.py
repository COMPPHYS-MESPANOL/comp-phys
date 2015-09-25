#%matplotlib osx
#HW03
#Matthew Espanol
#Partner: Matthew Del Rosario
from numpy import sin
from math import pi
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def psi(x1,x2, n1=1,n2=2, a=1.0):
    psi= 2./a*(sin((n1*pi*x1)/a)*sin((n2*pi*x2)/a)-sin((n1*pi*x2)/a)*sin((n2*pi*x1)/a))
    return psi

def prob_density(p):
    density=(p**2)
    return density

def antisym(x1,x2, n1=1,n2=2, a=1.0):
    return prob_density(psi(x1,x2, n1=1,n2=2, a=1.0))



fig=plt.figure()
ax= fig.add_subplot(121, projection='3d')
x= y = np.linspace(-1,1,150)
xv, yv= np.meshgrid(x, y)
z= psi(xv,yv)
plt.title("Wave Function")
ax.plot_surface(xv,yv, z, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth=0)

ax= fig.add_subplot(122, projection='3d')
x= y = np.linspace(-1,1,100)
xv, yv= np.meshgrid(x, y)
z= antisym(xv,yv)
plt.title("Probability Density")
ax.plot_surface(xv,yv, z, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth=0)
plt.show()
"""

>>> gamma_factorial(1)
1
>>> gamma_factorial(5)
24
>>> gamma(5)
24

"""
from math import exp
from math import factorial
from pprint import pprint

def gamma_factorial(x):
    if x >=1:
        value=factorial(x-1)
    return value

#gamma_factorial(5)   

def gamma_function(x,t,dx=0.5):
    return x**(t-1)*exp(-x)*dx


def gamma_integral(t, a=0.,b=1000.,dx=0.5):
    area=0
    n=int((b-a)/dx)
    for i in range(1,n+1):
        x0=a+(i-1)*dx
        x1=a+i*dx
        area_sub=dx*((gamma_function(x0,t)+gamma_function(x1,t)) /2.)
        area = area+area_sub
    return area
    
def gamma(t):
    if type(t)==int:
        gamma_factorial(t)
        print gamma_factorial(t)
    else:
        gamma_integral(t)
        print gamma_integral
        
gamma(5.5)

if __name__ == "__main__":
    
    import doctest
    #doctest.testmod()

'''doc test did not work, continued to get 'module' object has no attribute testmod'''
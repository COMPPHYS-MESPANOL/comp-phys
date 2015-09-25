'''Computes prime numbers from any given range a to b. First the function prime_finder takes the range of numbers given
and gets rid of all even numbers (these will obviously not be prime) the numbers that are left are appended to the 
list'odd'. Then, if the numbers in 'odd' are 3,5, or 7, they are added to the list 'prime'. For the rest of the numbers
in 'odd', if the remainder of the division by 3,5,or 7 is not 0, it is also added to 'prime'. '''
#HW03
#Matthew Espanol
#Partner: Matthew Del Rosario
import numpy as np
from pprint import pprint 
def prime_finder():
    a,b=input("please give the range(a,b):")
    odd=[]
    prime=[]
    variable= 1
    numbers=np.arange(a,b)
    for n in numbers:
        if n % 2 ==1:
            odd.append(n)
    for x in odd:
        if x == 3 or x==5 or x==7:
            prime.append(x)
        elif x % 3 !=0 and x%5 !=0 and x%7 !=0:
            prime.append(x)
    print "The prime numbers from", a ,"to", b ,"are:" 
    pprint(prime)
    

prime_finder()
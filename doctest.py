"""

>>> F(1)
33.8

"""

def F(C):
    return(9./5)*C + 32.

print F(1)

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
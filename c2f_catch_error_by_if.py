'''
    
    Using if (instead of try...except...else) to catch the error
    of user not entering input parameter.
    
    Note: this is not as good as try...except.  Sometimes the variable is not
    there at all, then the if statement will cause an error by itself.

 
'''


import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-C', type = float)
args = parser.parse_args()

if args.C == None:
    print '\nYou failed to provide Celsius degrees as input on the command line!\n'
    raise TypeError
else:
    C = args.C

F = 9.0*C/5 + 32
print '{:g} C is {:.1f} F'.format(C, F)

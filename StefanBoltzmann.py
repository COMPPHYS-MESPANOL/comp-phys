import math

#frac_diff=0

'''def (curr_diff,last_diff):
    frac_diff=((curr_diff-last_diff/curr_diff))
    return frac_diff
    fpercent=frac_diff*100'''

    
def riemann(a,b,dy):
    n=100
    steps=0
    y=0
    area=0
    print "running..."
    while steps< b:  
        while y<b:
            deltax=(b-a)/n 
            length = (a+y*deltax)
            area += deltax * length
            y+=1.
            steps += 1
            dy /= 2.

    print "number of steps:" , '{:4.1f}'.format(steps)
    print "dy=", "{0:.4f}".format(dy)
    print "the integral evaluated to within specified accuracy:" , "{0:.7f}".format(area)
riemann(0,100,1)
print "the upper limit of its fractional error is estimated to be:" , "{0:.7f}" .format(frac_diff)
print "the actual fractional error is:" , "{0:.7f}" .format(frac_diff*100), "%"
print "correct area", "{0:.7f}" .format(math.pi**4./15.)

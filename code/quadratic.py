
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):

    x=[None,None]
    if (b**2 -4*a*c) < 0:
        print("NULL");
    else:
        x[0]=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x[1]=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x;


print(quadratic(1,2,-3))

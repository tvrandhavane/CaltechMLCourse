'''
Created on Dec 23, 2013

@author: Tanmay
'''
import math

def error(u, v):
    value = u*math.exp(v) - 2*v*math.exp(-u)
    value = value*value
    return value

def partialErroru(u, v):
    value = u*math.exp(v) - 2*v*math.exp(-u)
    value = 2*value*(math.exp(v) + 2*v*math.exp(-u))
    return value

def partialErrorv(u, v):
    value = u*math.exp(v) - 2*v*math.exp(-u)
    value = 2*value*(u*math.exp(v) - 2*math.exp(-u))
    return value

def mainFunction():
    u = 1.0
    v = 1.0
    eta = 0.1
    errVal = error(u, v)
    iteration = 0
    while errVal >= math.pow(10, -14):
        print "errVal =", errVal 
        iteration = iteration + 1
        unew = u - eta*partialErroru(u, v)
        vnew = v - eta*partialErrorv(u, v)
        u = unew
        v = vnew
        errVal = error(u, v)
    print "Number of iterations=", iteration
    print "Final u =", u
    print "Final v =", v
    print "errVal =", errVal
        
mainFunction()
    
'''
Created on Dec 23, 2013

@author: Tanmay
'''
import gradientDescent
import math

def mainFunction():
    u = 1.0
    v = 1.0
    eta = 0.1
    errVal = gradientDescent.error(u, v)
    iteration = 0
    for i in range(15):
        print "errVal =", errVal 
        iteration = iteration + 1
        u = u - eta*gradientDescent.partialErroru(u, v)
        v = v - eta*gradientDescent.partialErrorv(u, v)
        errVal = gradientDescent.error(u, v)
    print "Number of iterations=", iteration
    print "Final u =", u
    print "Final v =", v
    print "errVal =", errVal
        
mainFunction()
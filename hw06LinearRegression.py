'''
Created on Dec 26, 2013

@author: Tanmay
'''

import numpy as np

def readFile(name):
    f = open(name, "r")
    Xtemp = []
    Ytemp = []
    for line in f:
        numbers = line.split()
        Xtemp.append([float(numbers[0]), float(numbers[1])])
        Ytemp.append(float(numbers[2]))
    X = np.array(Xtemp)
    Y = np.array(Ytemp)
    return [X, Y]

def generateZ(X):
    Ztemp = []
    for i in X :
        x1 = i[0]
        x2 = i[1]
        Ztemp.append([1, x1, x2, x1*x1, x2*x2, x1*x2, abs(x1 - x2), abs(x1 + x2)])
    Z = np.array(Ztemp)
    return Z

def getXDagger(X):    
    XDagger = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    return XDagger

def linearRegression(Z, Y):
    Zdagger = getXDagger(Z)
    w = np.dot(Zdagger, Y).T
    return w

def linearRegressionReg(Z, Y, lamda):
    return np.dot(np.dot(np.linalg.inv(np.dot(Z.T, Z) + lamda*np.identity(Z.shape[1])), Z.T), Y)
    
def computeError(Z, Y, w):
    count = 0
    for i in range(Z.shape[0]):
        value = Y[i]*np.dot(w.T, Z[i])
        if value <= 0:
            count = count + 1
    return count/(Z.shape[0]*1.0)

def experiment1():
    [Xin, Yin] = readFile("hw06in.dta")
    Zin = generateZ(Xin)
    w = linearRegression(Zin, Yin)
    errorIn = computeError(Zin, Yin, w)
    [Xout, Yout] = readFile("hw06out.dta")
    Zout = generateZ(Xout)
    errorOut = computeError(Zout, Yout, w)
    print "In-sample error =", errorIn
    print "Out-sample error =", errorOut

def experiment2():
    lamda = 0.01    
    [Xin, Yin] = readFile("hw06in.dta")
    Zin = generateZ(Xin)
    w = linearRegressionReg(Zin, Yin, lamda)
    errorIn = computeError(Zin, Yin, w)
    [Xout, Yout] = readFile("hw06out.dta")
    Zout = generateZ(Xout)
    errorOut = computeError(Zout, Yout, w)
    print "In-sample error =", errorIn
    print "Out-sample error =", errorOut
     
experiment2()
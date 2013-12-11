'''
Created on Dec 10, 2013

@author: Tanmay
'''
import random

def tossCoin():
    temp = random.uniform(-1,1)
    if temp < 0:
        return -1
    elif temp > 0:
        return 1
    else:
        return tossCoin() 

def toss10times():
    heads = 0
    for i in range(10):
        x = tossCoin()
        if x == 1:
            heads = heads + 1
    return heads

def mainFunction():
    print "Coin toss experiment for Hoeffding inequality"
    
    #declare variables
    nus = range(1000)
    
    #toss 1000 coins
    indx = 0
    minNu = 10
    for i in range(1000):
        nus[i] = toss10times()
        if nus[i] < minNu:
            indx = i
            minNu = nus[i]
    
    print "Nu Min =", minNu
    print "Nu 1 =", nus[1]
    rand = random.randint(0, 999)
    print "Nu rand =" , nus[rand]
    return [nus[1], nus[rand], minNu]    

sumMinNu = 0
sumNu1 = 0
sumNuRand = 0
for i in range(100000):
    print "Run Number:", i
    Nus = mainFunction()
    sumMinNu = sumMinNu + Nus[2]
    sumNu1 = sumNu1 + Nus[0]
    sumNuRand = sumNuRand + Nus[1]
print "sumMinNu =",sumMinNu
print "sumNu1 =",sumNu1
print "sumNuRand =",sumNuRand
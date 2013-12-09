import random

def generateTargetFunction() :
    targetFunction(0) = random.uniform(-1,1)
    targetFunction(1) = random.uniform(-1,1)
    return targetFunction

print "Perceptron"
targetFunction = generateTargetFunction()
print targetFunction(0)
print targetFunction(1)
    

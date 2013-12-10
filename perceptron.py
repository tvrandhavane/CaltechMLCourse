import random

def generateRandomPair() :
    pair = [1, 2]
    pair[0] = random.uniform(-1,1)
    pair[1] = random.uniform(-1,1)
    return pair

def generateTargetFunction() :
    targetFunction = range(3)
    point1 = generateRandomPair()
    point2 = generateRandomPair()
    targetFunction[0] = (point1[0]*point2[1] - point2[0]*point1[1]) /  (point1[0] - point2[0])    
    targetFunction[1] = (point1[1] - point2[1]) / (point1[0] - point2[0])
    targetFunction[2] = -1
    return targetFunction

def evaluatef(f, x) :
    value = f[0] * 1 + f[1]*x[0] + f[2]*x[1]
    if value < 0 :
        return 0
    else :
        return 1
    
def mainFunction() :
    print "Perceptron"
    
    #set up variables
    runs = 1000
    N = 100
    totalIterationCount = 0
    totalProbability = 0
    for i in range(runs) :
        print "Turn :", i+1 
        
        #generate target function
        targetFunction = generateTargetFunction()
        print "Target Function: " , targetFunction[0], "," , targetFunction[1] , "," , targetFunction[2]
        
        #generate X's
        X = range(N)
        for i in range(N) :
            temp = [0, 0]
            temp[0] = random.uniform(-1,1)
            temp[1] = random.uniform(-1,1)
            X[i] = temp
            
        #Compute y
        Y = range(N)
        for i in range(N) :
            Y[i] = evaluatef(targetFunction, X[i])
        
        #Compute g
        g = [0, 0, 0]
        iterationCount = 1 
        print "Iteration Number:", iterationCount
        for i in range(N):
            x = X[i]
            temp = evaluatef(g, x)
            if temp != Y[i] :
                iterationCount = iterationCount + 1
                print "Iteration Number:", iterationCount
                if Y[i] == 0 :
                    g[0] = g[0] - 1
                    g[1] = g[1] - x[0]
                    g[2] = g[2] - x[1]
                else :
                    g[0] = g[0] + 1
                    g[1] = g[1] + x[0]
                    g[2] = g[2] + x[1]
                i = 0;            
        print "PerceptronFunction =", g[0] ,"," , g[1], "," , g[2]
        #calculate the probability of g
        count = 0
        for i in range(1000000) :
            x = generateRandomPair()
            fvalue = evaluatef(targetFunction, x)
            gvalue = evaluatef(g, x)
            if fvalue != gvalue :
                count = count + 1
        totalProbability = totalProbability + count
        totalIterationCount = totalIterationCount + iterationCount
        print "Probability =", count
    print "Total Iteration Count =", totalIterationCount
    print "Total Probability =", totalProbability
mainFunction()
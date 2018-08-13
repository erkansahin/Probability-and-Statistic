"""
Erkan Sahin
240201053
Probability and Statistic
Homework 1
"""

import numpy as np
import matplotlib.pyplot as plt


resultsC = []
avgC =[]
resultsA = []
avgA = []
resultsB = []
avgB = []
resultsX =[]
avgX = []
varX= []


def tossCoin():
    coin = int((np.random.rand()) * 2)
    result = -1 if coin==0 else 1
    resultsC.append(result)
    avgC.append(np.mean(resultsC))
    return result

def roll6faceddice():
    dice = int((np.random.rand() * 6)) + 1
    resultsA.append(dice)
    avgA.append(np.mean(resultsA))
    return dice
def roll4faceddice():
    dice = int((np.random.rand() * 4)) + 1
    resultsB.append(dice)
    avgB.append(np.mean(resultsB))
    return dice

def conductAnExperiment(numberOfExperiments):
    for i in range(numberOfExperiments):
        X = roll6faceddice() + roll4faceddice() * tossCoin()
        resultsX.append(X)
        avgX.append(np.mean(resultsX))
        Ex2 =list(map(lambda x: x**2, resultsX))
        varX.append(np.mean(Ex2)-np.mean(resultsX)**2)#Used the handy relationship for variance






def plotGraphs():
    plt.plot(avgA)
    plt.xlabel("Number of Experiments")
    plt.ylabel("Average Value")
    plt.title("6 Faced Dice Experiment\nRandom Variable A")
    plt.show()

    plt.plot(avgB)
    plt.xlabel("Number of Experiments")
    plt.ylabel("Average Value")
    plt.title("4 Faced Dice Experiment\nRandom Variable B")
    plt.show()

    plt.plot(avgC)
    plt.xlabel("Number of Experiments")
    plt.ylabel("Average Value")
    plt.title("Coin Toss Experiment\nRandom Variable C")
    plt.show()

    plt.plot(avgX)
    plt.xlabel("Number of Experiments")
    plt.ylabel("Average Value")
    plt.title("Graph For Random Variable X")
    plt.show()

    plt.plot(varX)
    plt.xlabel("Number of Experiments")
    plt.ylabel("Variance of X")
    plt.title("Variance of X")
    plt.show()

    plt.hist(resultsA)
    plt.ylabel("Frequency")
    plt.xlabel("Values of A")
    plt.title("6 Faced Die Experiment\nRandom Variable A")
    plt.show()
    
    plt.hist(resultsB)
    plt.ylabel("Frequency")
    plt.xlabel("Values of B")
    plt.title("4 Faced Die Experiment\nRandom Variable A")
    plt.show()
    
    plt.hist(resultsC)
    plt.ylabel("Frequency")
    plt.xlabel("Values of C")
    plt.title("Coin Toss Experiment\nRandom Variable C")
    plt.show()
    
    plt.hist(resultsX)
    plt.xlabel("Values of X")
    plt.title("Results of X")
    plt.ylabel("Frequency")
    

conductAnExperiment(100000)
plotGraphs()




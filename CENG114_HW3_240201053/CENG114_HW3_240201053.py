# Erkan Şahin 240201053 Probability and Statistic Report 4

import math
from matplotlib import pyplot as plt
import numpy as np


def MaximumLikelihoodEstimator(alist):
    logarithmicSum =  sum(list(map(lambda x: math.log(x,math.e), alist)))
    result = len(alist) /( -1*logarithmicSum)
    return result


def MethodOfMoments(alist):
    MoM = np.mean(alist)/(1-np.mean(alist))
    return MoM

def experimentSimulation(P, N):
    # The multidimensional list keeps variance, average, method of moments values respectively
    MoM = [[], [], []]
    # This multidimensional list stores variance , average and MLE values respectively
    mle = [[], [], []]
    # Values are accumulation of  variance of MOM and MLE respectively
    varianceAccumulator = [0, 0]
    # Values are accumulation of average of MOM and MLE respectively
    meanAccumulator = [0, 0]
    # Current population
    pop = []
    P = np.array(P)
    for i in range(100000):
        randomList = np.random.random_integers(0, high=9999999, size=N)
        pop = P[randomList]
        MoM[2].append(MethodOfMoments(pop))
        mle[2].append(MaximumLikelihoodEstimator(pop))

        meanAccumulator[0] += MethodOfMoments(pop)
        meanAccumulator[1] += MaximumLikelihoodEstimator(pop)

        MoM[1].append(meanAccumulator[0]/(i+1))
        mle[1].append(meanAccumulator[1]/(i+1))

        varianceAccumulator[0] += (MethodOfMoments(pop)-MoM[1][i])**2
        varianceAccumulator[1] += (MaximumLikelihoodEstimator(pop) - mle[1][i]) ** 2

        MoM[0].append(float(varianceAccumulator[0])/(i+1))
        mle[0].append(float(varianceAccumulator[1])/(i+1))

    plt.figure()
    plt.hist(MoM[2], 100, alpha=0.5, normed=True)
    plt.hist(mle[2], 100, alpha=0.5, normed=True)
    plt.show()

    return MoM[1][-1],  mle[1][-1], MoM[0][-1], mle[0][-1]


population = []
N = [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]

for i in range(10000000):
    population.append(np.random.rand() ** (1 / 2.4))

for i in N:
    print("Sample Size:",i)
    avgOfMoM, avgOfMLE, varOfMoM, varOfMLE = experimentSimulation(population, i)
    print("Mean of MoM = ", avgOfMoM)
    print("Mean of MLE : ", avgOfMLE)
    print("Varience of MoM : ", varOfMoM)
    print("Varience of MLE : ", varOfMLE)

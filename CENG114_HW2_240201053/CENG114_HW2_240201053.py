#Erkan Şahin 240201053 HW2 Probability and Statistic

import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []
total_Xa = 0
total_Xa_square = 0

# Populate the given arrays.
### YOUR CODE HERE ###

for i in range(10000):
    u = np.random.rand()
    U.append(u)
    xA = u**(1/2)
    Xa.append(xA)
    total_Xa += xA
    total_Xa_square += xA ** 2
    av_Xa.append(total_Xa/(i+1))
    vr_Xa.append(total_Xa_square/(i+1) - av_Xa[-1] ** 2)


# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])

plt.figure()
hU = plt.hist(U,100,alpha=0.5,normed=True)
hXa = plt.hist(Xa,100,alpha=0.5,normed=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))
plt.show()

# Plot the average and variance values.
### YOUR CODE HERE ###


plt.title("Variance of Xa")
plt.xlabel("Number of experiments")
plt.ylabel("Variance of X")
plt.plot(vr_Xa)
plt.show()

plt.title("Generated Random variable Xa")
plt.plot(av_Xa)
plt.xlabel("Number of experiments")
plt.ylabel("Average value")
plt.show()


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []
total_Xb = 0
total_Xb_square = 0


# Populate the given arrays.
### YOUR CODE HERE ###

def pdf(x):
    return 2*x

def evaluateX(u):
    return a + (b - a) * u


def evaluateY(v):
    return c * v


a = 0
b = 1
c = 2

while len(Xb) < 10000:
    u = np.random.rand()
    v = np.random.rand()

    X = evaluateX(u)
    Y = evaluateY(v)

    if pdf(X) < Y:
        continue

    Xb.append(X)
    total_Xb += X
    total_Xb_square += X**2

    av_Xb.append(total_Xb/len(Xb))
    vr_Xb.append(total_Xb_square/len(Xb) - av_Xb[-1] ** 2)


# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,normed=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))
plt.show()
# Plot the average and variance values.
### YOUR CODE HERE ###



plt.title("Variance of Xb")
plt.xlabel("Number of experiments")
plt.ylabel("Variance of X")
plt.plot(vr_Xb)
plt.show()

plt.title("Random variable Xb")
plt.plot(av_Xb)
plt.xlabel("Number of experiments")
plt.ylabel("Average value")
plt.show()

#!/bin/env python
from __future__ import print_function
import scipy.stats


def rSquared(sampleSize, fathersInfluence=0.5):
    # loc = mean
    # scale = standard deviation
    fathers = scipy.stats.norm.rvs(loc=170, scale=10, size=sampleSize)
    mothers = scipy.stats.norm.rvs(loc=170, scale=10, size=sampleSize)

    def sonsHeight(fathersHeight, mothersHeight):
        return (fathersHeight * fathersInfluence + mothersHeight * (1 - fathersInfluence))/2

    sons = [sonsHeight(father, mother) for father, mother in zip(fathers, mothers)]

    _, _, r_value, _, _ = scipy.stats.linregress(fathers, sons)
    return r_value ** 2

size = 1000000

#print(sonsHeight(size, fathersInfluence=0.5))


rs = []
influences = []
for influence in [i*0.01 for i in range(101)]:
    rs.append(rSquared(size, fathersInfluence=influence))
    influences.append(influence)
print(zip(influences, rs))


import matplotlib.pyplot as plt
plt.scatter(influences, rs)
plt.xlabel("fathersInfluence")
plt.ylabel("R^2")
plt.show()

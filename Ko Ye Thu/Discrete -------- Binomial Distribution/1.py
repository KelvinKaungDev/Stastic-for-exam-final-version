"""
Discrete
--------
Binomial Distribution
---------------------
hispanic composition of a jury list
n = 12 and pi = 0.20
"""
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

print(binom.pmf(1, 12, 0.20))    # binomial P(Y=1) when n=12, pi=0.20


fig, ax = plt.subplots(1, 1)
n, pi = 12, 0.20    # following creates plot of bin(12, 0.2) pmf
y = list(range(0, 13))    # y values between 0 and 12
ax.vlines(y, 0, binom.pmf(y, n, pi), colors='b', lw=5, alpha=0.5)
plt.xlabel('y')
plt.ylabel('P(y)')
plt.xticks(np.arange(min(y), max(y)+1, 1.0))

plt.show()

print(list(binom.pmf(y, n, pi)))   # display binomial probabilities

mean, variance, skewness = binom.stats(n, pi, moments='mvs')
print(mean, variance, skewness)


from scipy.stats import binom
import matplotlib.pyplot as plt

"""
survey about legalized marijuana
n=3, pi=0.5
"""

fig, ax = plt.subplots(1, 1)
n, p = 3, 0.5
x = [0, 1, 2, 3]
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
plt.xlabel('y')
plt.ylabel('P(y)')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()
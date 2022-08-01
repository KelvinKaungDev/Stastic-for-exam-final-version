"""
Continuous
----------
Uniform Distribution
--------------------
pdf of a uniform random variable over the interval [0,1] can be plotted as
"""

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
x = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)
rv = uniform()
ax.plot(x, rv.pdf(x), lw=2, color='blue')
plt.plot([-0.3,0], [0,0], lw=2, color='blue')
plt.plot([1,1.3], [0,0], lw=2, color='blue')
plt.xticks(np.arange(0, 1.2, 0.2))

print(uniform.rvs(0,100,1))
plt.show()



import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

"""
cdf of a uniform random variable
"""

fig, ax = plt.subplots(1, 1)
x = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)
rv = uniform()

ax.plot(x, rv.cdf(x), lw=2, color='blue')
plt.plot([-0.3,0], [0,0], lw=2, color='blue')
plt.plot([1,1.3], [1,1], lw=2, color='blue')
plt.xticks(np.arange(0, 1.2, 0.2))
plt.show()
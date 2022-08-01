# 1 simulation of 7 coin flips, get number of head (or tail) in 7 flips
import numpy as np

np.random.binomial(7, 0.2, size=1)

# (or)
n, p = 1, 0.2   # no. of flips (trials), prob(success) in each
s = np.random.binomial(n, p, 7)   # 7 simulation of n flips
print(s)

import numpy as np
# proportion = x1 / 100 -> x1/100 heads in 100 coin flips
x1 = np.random.binomial(100, 0.20, 1); print(x1/100)
x2 = np.random.binomial(1000, 0.20, 1); print(x2/1000)
x3 = np.random.binomial(10000, 0.20, 1); print(x3/10000)
x4 = np.random.binomial(100000, 0.20, 1); print(x4/100000)
x5 = np.random.binomial(1000000, 0.20, 1); print(x5/1000000)
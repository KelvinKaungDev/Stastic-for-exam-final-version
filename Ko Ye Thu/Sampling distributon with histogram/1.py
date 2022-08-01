"""
sampling distributions with histogram

exit poll in us presidential election where probability is pi = 0.50 of voting 
for joe biden. simulation for random sample of 2271 voters
"""
import numpy as np
n, p = 2271, 0.50   # values for binomial n, pi
x = np.random.binomial(n, p, 1)   # 1 binomial experiment
print(x, x / n )  # biden votes, simulated proportion of biden votes

"""
deriving the histogram of the million simulated proportions of above code
"""
import statistics
import matplotlib.pyplot as plt

results = np.random.binomial(n, p, 1000000) / n
statistics.mean(results)    # mean of million sample proportion values
statistics.stdev(results)   # standard deviation of million sample proportions

plt.hist(results, bins=14, edgecolor='k')
plt.xlabel('Sample proportion'); plt.ylabel('Frequency')
plt.show()
from matplotlib import pyplot as plt
import numpy as np
"""
sampling distributions with scatter plot
"""

n = 1001  # number of independent experiments in each trial
p = 0.2   # probability of success for each experiment

def run_binom(n, p):
  phat = []
  for i in range(1, n):
    phat.append(np.random.binomial(i, p, 1)/i)    

  return phat

phat = run_binom(n, p)      
len(phat)

fig = plt.figure(figsize=(10, 7))
plt.scatter(range(1, n), phat, s=10)
plt.xlabel('n', size=14)
plt.ylabel('proportion', size=14)
plt.show()

# histogram
"""
deriving the histogram of the million simulated proportions of above code
"""
import statistics
results = np.random.binomial(n, p, 1000000) / n
statistics.mean(results)    # mean of million sample proportion values
statistics.stdev(results)   # standard deviation of million sample proportions

plt.hist(results, bins=14, edgecolor='k')
plt.xlabel('Sample proportion'); plt.ylabel('Frequency')
plt.show()
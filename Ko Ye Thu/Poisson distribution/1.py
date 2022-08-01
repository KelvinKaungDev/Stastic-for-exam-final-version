from scipy.stats import poisson

"""
Poisson Distribution
--------------------
find probabilities of individual values using the pmf or of a range of values 
using the cdf
"""

poisson.pmf(0, 2.3)   # P(Y=0) if Poisson mean=2.3

# the difference of cdf values at 130 and 69 for Poisson with mean=100

print(poisson.cdf(130, 100) - poisson.cdf(69, 100))

# probability within 2 standard deviations of mean (from 80 to 120):
print(poisson.cdf(120, 100))
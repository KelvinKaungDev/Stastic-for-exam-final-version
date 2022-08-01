from scipy.stats import binom

"""
For a simple random sample of n = 3 people, let Y = the number who say yes to 
supporting legalized marijuana. When exactly half the population would respond 
yes, each of the eight sample points is equality likely.
"""

y = 0    # Y probability for discrete random variable y
n = 3    # number of samples
pi = 0.5 # probability of success in each observation


print(binom.pmf(y, n, pi))
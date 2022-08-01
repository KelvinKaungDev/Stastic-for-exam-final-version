from scipy.stats import norm

print(norm.cdf(1) - norm.cdf(-1))  # probability within 1 standard deviation of mean
print(norm.cdf(2) - norm.cdf(-2))  # probability within 2 standard deviation of mean
print(norm.cdf(3) - norm.cdf(-3))  # probability within 3 standard deviation of mean


from scipy.stats import norm

"""
proportion of the self-employed who work between 50 and 70 hours a week, when 
the times have a N(45,15^2) distribution. we can apply normal distributions 
other than the standard normal by specifying mu and sigma
"""

norm.cdf(70, 45, 15) - norm.cdf(50, 45, 15)   # mean=45, standard deviation=15
norm.ppf(0.99)      # 0.99 quantile of standard normal
norm.ppf(0.99, 100, 16)   # 0.99 normal quantile for IQ's
norm.cdf(550, 500, 100)   # SAT=550 is 69th percentile
norm.cdf(30,18,6)   # ACT=30 is 97.7 percentile


from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

"""
plotting pmf of a poisson distribution along with the pdf of a normal with 
mu=100 and sigma=10
"""

fig, ax = plt.subplots(1, 1)
y = list(range(60, 141))  # y values between 60 and 140 with increment of 1
ax.vlines(y, 0, poisson.pmf(y, 100), colors='b', lw=1, alpha=0.5)
ax.plot(y, norm.pdf(y, 100, 10), lw=2, color='r', alpha=0.5)  # normal pdf
plt.xlabel('y')
plt.ylabel('P(y)')
plt.xticks(np.arange(min(y), max(y)+1, 10))
plt.show()




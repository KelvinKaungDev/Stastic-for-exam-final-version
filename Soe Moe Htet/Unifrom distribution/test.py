# Assume you are randomly number by normally distributed with mean at 0 and variance at 4. 
# Find the probability of number will greater than 2.  
# Draw the pdf and cdf of normal distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import seaborn as sb

mean = 20
standard_deviation = 60  # standard deviation = square root of variance

# -------------------------------------------------------------------------------------

prob =  1 - uniform.cdf(2, mean, standard_deviation)
print(prob)     # 0.3085375387259869

# -------------------------------------------------------------------------------------

data = np.linspace(-10, 20, 10000)      # 100 means random numbers between -1 and 2

uniform_pdf =  uniform.pdf(data, 2 , 6)

plt.plot(data, uniform_pdf, color = 'blue')
plt.title(f"uniform Distribution (mean = {mean}, standard_deviation = {standard_deviation}))")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------

data = np.arange(0, 100)

normal_cdf =  uniform.cdf(data, mean, standard_deviation)
plt.plot(data, normal_cdf, color = 'red')
plt.title(f"Normal Distribution (mean = {mean}), (standard_deviation = {standard_deviation})")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------
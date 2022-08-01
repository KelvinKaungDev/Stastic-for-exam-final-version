import imp
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

print(uniform.ppf(0.40, 0 , 1))    # ppf means probability percentile function
                                    # ppf(percentile, loc = default 0, scale = default 1)

data = np.arange(-20, 25)

uniform_ppf =  uniform.ppf(data, 1, 3)

plt.plot(data, uniform_ppf, color = 'blue')
plt.title(f"Normal Distribution (mean = 1, standard_deviation = 3))")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()
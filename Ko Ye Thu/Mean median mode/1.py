# mean and median are rougly the same for symmetric distributions
# for assymmetric distributions,
# mean is affected by outliers
# median (central tendency) is robust (less affected by outliers)
import numpy as np

data = [10, 28, 28, 41, 54]

mean = np.mean(data)
median = np.median(data)

print(mean, median)

# mode - the observation with the highest frequency
from scipy.stats import mode 

data = [10, 28, 28, 41, 54]
print(mode(data))


"""
census
kids  families
1     1.5m
2     1.8m
3     1.0m
4     0.4m
5     0.2m
6+    0.1m
----------
      5.0m
"""

mean = ((1.5 * 1) + (1.8 * 2) + (1.0 * 3) + (0.4 * 4) + (0.2 * 5) + (0.1 * 6)) / 5

print(mean)
# mode is 2
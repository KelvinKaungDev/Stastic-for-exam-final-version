"""
variance describes the spread of data
sample mean
-----------
variance = (sigma ((x - x_bar) ^ 2)) / n - 1
(sum of -> (observation - mean) squared) divided by number of observations minus 1
population mean
---------------
variance = (sigma ((x - mu) ^ 2)) / n

standard deviation is sqrt(variance)
"""

import numpy as np

sample = [5, 4, 6, 39]
# ddof is the degree of freedom


print(np.var(sample, ddof=1))
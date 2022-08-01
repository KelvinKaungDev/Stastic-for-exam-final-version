"""
first quartile is 1/4 of the way into an ordered dataset
second quartile is the median
third quartile is 3/4 the way into an ordered dataset
first decile is 1/10 of the way into an ordered dataset
...
thenth decile is the max of the ordered dataset
first percentile is the 1% of the way into an ordered dataset
forty-second percentile is the 42% of the way into an ordered dataset
"""

# quantile calculation below takes the median into account
import numpy as np

sample = [2, 2, 5, 6, 9, 10, 13]
minimum = min(sample)
maximum = max(sample)
q1 = np.quantile(sample, 0.25)
q2 = np.quantile(sample, 0.50)
q3 = np.quantile(sample, 0.75)



print(minimum, maximum, q1, q2, q3)


"""
inter quartile is difference between two quartiles
e.g. Q3 - Q2
range is max - min
range is suspectable to outliers

box and whisker plot
-+- max
 |
 |
+-+ 3rd quartile  <--+
| |                  |
|-| median           +-- inter quartile range
+-+ 1st quartile  <--+
 |
 |
-+- min
"""
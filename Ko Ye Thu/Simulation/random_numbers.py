# Simulations
# simulate n observations
import numpy as np
y = list(range(0, 10))  # generate a list of integers from 0 to 9
randomlist = np.random.choice(y, 7) # sample n=7 observations


print(randomlist)
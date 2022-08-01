import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Linear regression
"""

GS = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Guns_Suicide.dat', sep='\s+')
GS.info()   # number of non-miossing values per variable

GS.plot(kind='scatter', x='guns', y='suicide', color='blue', figsize=(10, 7))
plt.xlabel('guns', size=14)
plt.ylabel('suicide', size=14)
print(GS.corr()) # correlation matrix for pairs of variables in GS data file

plt.show()

import numpy as np

"""
scatter plot with linear regression line
"""

coef = np.polyfit(GS['guns'], GS['suicide'], 1)
LR_fn = np.poly1d(coef)   # LR_fn: returns fitted y value
fig = plt.figure(figsize=(10,7))
plt.plot(GS['guns'], GS['suicide'], 'o', GS['guns'], LR_fn(GS['guns']))
plt.xlabel('guns', size=14)
plt.ylabel('suicide', size=14)
plt.show()

print()
print()

import statsmodels.formula.api as sm    # fit linear regression
mod = sm.ols(formula='suicide ~ guns', data=GS).fit()
print(mod.params)
print(mod.summary())
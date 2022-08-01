import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# side-by-side box plots

Crime = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Murder2.dat', sep='\s+')
sns.boxplot(y='nation', x='murder', data=Crime, orient='h')
plt.show()


# You can use this funciton from pandas 
# to find count, mean, std, percentiles, min and max 
# but you need to have data in csv format or excel format (in file-type formats), 
# To see the data, click the http://stat4ds.rwth-aachen.de/data/Murder2.dat

print(Crime.groupby('nation')['murder'].describe()) 



# note that you have to use matplotlib.pyplot in visual studio code to see the result

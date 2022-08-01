from scipy.stats import norm

"""
Standard Normal Probability
A set of middle school student heights are normally distributed with a mean of 
150 centimeters and a standard deviation of 20 centimeters. Let H be the height 
of a randomly selected student from this set.

find and interpret P(H > 170)
"""
# loc is mean and scale is standard deviation
# the area under the graph we are finding is 1 standard deviation above the 
# the mean
# since the cdf is comulative until 170, we subtract the cdf from 1 to get the 
# desired value


print(1 - norm.cdf(170, loc=150, scale=20))

"""
Standard Normal Probability
An instructor gives a course grade of B to students who have total score on 
exams and homeworks between 800 and 900, where the maximum possible is 1000. 
If the total scores have approximately a normal distribution with mean 830 and 
standard deviation 50, about what proportion of the students receive a B?
"""
print(norm.cdf(900, loc=830, scale=50) - norm.cdf(800, loc=830, scale=50))
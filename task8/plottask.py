# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# a plot of the function  h(x)=x3 in the range 0 to 10, 
import numpy as np
#generating random numbers with normal distribution using numpy
values = np.random.normal(5, 2, 1000)
print (values)
#plotting a histogram with matplotlib pyplot

import matplotlib.pyplot as plt
plt.hist(values, bins = 'auto')
plt.show()


#references
#https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
#https://stackoverflow.com/questions/71212542/python-generate-random-numbers-with-n-standard-deviations-of-a-mean
#https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram#:~:text=The%20bins%20parameter%20tells%20you%20the%20number%20of,integer%20or%20as%20a%20list%20of%20bin%20edges.
#https://datagy.io/python-matplotlib-plot-function/
 # h(x)=x3 in the range 0 to 10,
def h(x):
  return x ** 3
 
 #create x and y ranges

x = np.linspace (0, 10)
y = h(x)

#plotting the data using the function h(x)=x3 in the range 0 to 10

plt.plot (x,y)
plt.xlabel ('x in range 0 - 10')
plt.ylabel (' y = x^3')
plt.legend()
plt.show ()
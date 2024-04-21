import numpy as np
import matplotlib.pyplot as plt

def h(x):
  return x ** 3
 
 #create x and y ranges

x = np.linspace (0, 10)
y = h(x)

#plotting the data using the function h(x)=x3 in the range 0 to 10

plt.plot (x,y)
plt.show ()

plt.scatter(x, y)
plt.show()
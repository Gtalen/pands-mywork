#plt.text = (120, 10, mean = 5, sd = 2)
#plt.legend()
#label = 'n = 1000', 'mean = 5', 'SD = 2'


"""

values = np.random.normal(5, 2, 1000)  # mean = 5, SD = 2

# Plotting a histogram of the values
plt.hist(values, bins='auto', color='brown', edgecolor='black', xlabel='Values',)

plt.title('Histogram of normal distribution n = 1000, mean = 5, SD = 2')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Adding legend
plt.legend()

plt.show()
"""
"""

 # h(x)=x3 in the range 0 to 10,
def h(x):
  return x ** 3
 
 #create x and y ranges

x = np.linspace (0, 10)
y = h(x)

#plotting the data using the function h(x)=x3 in the range 0 to 10

plt.plot (x,y)
plt.xlabel ('x in range 0 - 10')
plt.ylabel (' y = h(x)^3')
plt.legend()
plt.show ()
"""
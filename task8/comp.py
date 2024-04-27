import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data_normal = np.random.normal(5, 2, 1000)

# Plot histogram of the normal distribution
plt.figure(figsize=(8, 4))
plt.hist(data_normal, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Define the function h(x) = x^3
def h(x):
    return x**3

# Generate values for x in the range 0 to 10
x_values = np.linspace(0, 10, 100)

# Calculate corresponding values for h(x)
y_values = h(x_values)

# Plot the function h(x) = x^3
plt.figure(figsize=(8, 4))
plt.plot(x_values, y_values, color='red')
plt.title('Plot of the Function h(x) = x^3')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid(True)
plt.show()

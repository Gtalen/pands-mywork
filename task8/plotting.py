
#w3schools matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
'''
print (mpl.__version__)
print (np.__version__)
xpoints = np.array([0,6])
ypoints = np.array ([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

plt.plot(xpoints, ypoints, 'o') # o rings is used to plot the points without a line
plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o') #marker is used to emphasize each point
plt.show()
plt.plot(ypoints, marker = '*') #marker is used to emphasize each point
plt.show()
'''
#different markers can be used such as d, p, H, h etc

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse") #labelling x axis
plt.ylabel("Calorie Burnage") #labelling y axis
plt.title("Sports Watch Data",  loc = 'left') #giving it a title, loc to poistion the title to either left, right or center
plt.show()

#font size, colour etc can be assigned

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.grid()  # add gridlines
plt.show()
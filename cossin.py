import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

t = np.linspace(0,6,1)
t = np.arange(0,5,1)
a = 6

x = a%t
y = np.sin(t)

plt.plot(x,y)
ax = plt.gca()  # Get the current Axes instance on the current figure
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
y_min = -7
y_max = -1 * y_min
plt.ylim(y_min,y_max)
plt.grid(True)

plt.show()


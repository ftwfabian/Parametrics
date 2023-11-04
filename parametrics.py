import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
r = 1

x = r * np.cos(t)
y = r * np.sin(t)

plt.plot(x,y)
plt.axis('equal')
plt.show()
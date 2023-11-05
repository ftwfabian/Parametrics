import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
r = 1

x = r * np.cos(t)
y = r * np.sin(t)

x_min = -5
x_max = x_min * -1
y_min = -5
y_max = y_min * -1

plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.plot(x,y)
plt.grid(True, linestyle='--', linewidth = 0.5, color='gray')
plt.axis('equal')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
R= 1
t = np.arange(0, 10, 0.01)
x = R*np.cos(t)**3
y = R*np.sin(t)**3
plt.axis('equal')
plt.plot(x, y)
plt.savefig('fig1.2.png')
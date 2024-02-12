import matplotlib.pyplot as plt 
import numpy as np 

phi = np.arange(0, 8*np.pi, 0.1)
r = 1.2 * phi

x = np.cos(phi)*r
y = np.sin(phi)*r

plt.plot(x, y)
plt.savefig('fig_lab_6_task_4_2.png')
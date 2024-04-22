import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import warnings
import matplotlib
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

def planet(R, vel, t):
    alpha = vel * np.pi / 180 * t
    x = R * np.cos(alpha)
    y = R * np.sin(alpha) * 0.8
    return x, y

def animate(i):
    deimos.set_data(planet(R=6.2, vel=3, t=i))               
    Phobos.set_data(planet(R=11.2, vel=0.7, t=i))
    
    ax.set_title(f'Day on mars: {i}')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    plt.plot([0], [0], 'o', ms=10, color='brown')
    deimos, = plt.plot([], [], 'o', ms=7, color='red')
    Phobos, = plt.plot([], [], 'o', ms=15, color = 'grey')
    

    edge = 12

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=999,
                        interval=20
                        )
    ani.save('Project_limit.gif')
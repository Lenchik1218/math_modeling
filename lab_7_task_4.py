from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = [], []

def animate():
    x0 = 0.1
    y0 = 0.1
    C = 0.3
    D = 0.33
    xdata.append(x0 ** 2 - y0 ** 2 + C)
    ydata.append(2 * x0 * y0 + D)
    fraq.set_data(xdata, ydata)
    return fraq

if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=180,
                        interval=30)

    ani.save('animation_4.gif') 
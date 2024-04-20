import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
ax.set_aspect('equal')
ax.axis('off')

sun = plt.Circle((0, 0), 1, color='yellow')
moon = plt.Circle((0, 0), 0.2, color='gray')

ax.add_patch(sun)
ax.add_patch(moon)

def init():
    return sun, moon

def animate(i):
    angle = np.deg2rad(i)
    moon_x = np.cos(angle) * 1.2
    moon_y = np.sin(angle) * 1.2
    moon.center = (moon_x, moon_y)
    return moon,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

anim.save('moon_animation.gif', writer='pillow')

import datetime
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_clock(frame):
    current_time = datetime.datetime.now()
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second

   
    hour_angle = math.radians((hour * 30) + (minute * 0.5))
    minute_angle = math.radians((minute * 6) + (second * 0.1))
    second_angle = math.radians(second * 6)

    plt.clf()
    plt.axis('off')

  
    circle = plt.Circle((0, 0), 1, edgecolor='black', facecolor='white')
    plt.gca().add_patch(circle)

    
    for i in range(1, 13):
        angle = math.radians(i * 30)
        x = 0.9 * math.sin(angle)
        y = 0.9 * math.cos(angle)
        plt.text(x, y, str(i), fontsize=12, ha='center', va='center')

    
    hour_hand = plt.Line2D((0, 0.5 * math.sin(hour_angle)), (0, 0.5 * math.cos(hour_angle)), lw=4, color='black')
    minute_hand = plt.Line2D((0, 0.7 * math.sin(minute_angle)), (0, 0.7 * math.cos(minute_angle)), lw=3, color='black')
    second_hand = plt.Line2D((0, 0.9 * math.sin(second_angle)), (0, 0.9 * math.cos(second_angle)), lw=2, color='red')

    
    plt.gca().add_line(hour_hand)
    plt.gca().add_line(minute_hand)
    plt.gca().add_line(second_hand)

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_clock, frames=60, interval=1000)

plt.show()

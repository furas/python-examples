#!/usr/bin/env python3

# animated GIF: https://media.giphy.com/media/3og0IR8kl9YxONfB7y/giphy.gif

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
how_many_points = 5

#fig, ax = plt.subplots()
fig = plt.figure()

# X
line_x   = np.arange(0, 2*np.pi, 0.1)
points_x = np.arange(0, 2*np.pi, (2*np.pi-0.1)/(how_many_points-1))

# Y
line_y   = np.sin(line_x)
points_y = np.sin(points_x)

# plots
line,   = plt.plot(line_x,   line_y,  'red')
points, = plt.plot(points_x, points_y, 'go') # 'g' = green, 'o' = circles

# function which change data in plots 
def animate(i):
    #print(i, line_x+i)

    # replace Y
    line.set_ydata(np.sin(line_x+i))
    points.set_ydata(np.sin(points_x+i))

    return line, points
 
# define animation matplot engine
# interval=50 gives fps=20 (50ms*20 = 1000ms = 1second) 
ani = animation.FuncAnimation(fig, animate, line_x, interval=50)#, blit=True)

# display animation - it doesn't stop - you have to close window
plt.show()

# save in file - it may need some time to save all frames
ani.save('animation.gif', writer='imagemagick', fps=20)


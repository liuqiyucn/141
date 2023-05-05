import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the data for the point
x = [0]
y = [0]
z = [0]

# Create the figure and axes for the plot
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# Create the initial point in the plot
point, = ax.plot(x, y, z, 'bo')

# Define the update function for the animation
def update(frame):
    # Update the position of the point
    x.append(frame)
    y.append(frame*2)
    z.append(frame*3)
    point.set_data(x[-1:], y[-1:])
    point.set_3d_properties(z[-1:])
    return point,

x1 = np.linspace(0,20)
y1 = x1*2
z1 = x1*3

#ax.plot(x1, y1, z1, label = "expression")

# Create the animation object
anim = FuncAnimation(fig, update, frames=np.linspace(0, 10, 1000),
                     blit=False)

# Show the plot
plt.legend()
plt.show()
# Horn Antenna-3D
# Study and Simulation of the 3D Radiation Pattern of a Horn Antenna

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


theta = np.linspace(0, np.pi/2, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)


n = 6
r = np.cos(theta)**n


X = r * np.sin(theta) * np.cos(phi)
Y = r * np.sin(theta) * np.sin(phi)
Z = r * np.cos(theta)

# ৩ডি প্লট তৈরি করা
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')


surf = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none', alpha=0.9)


ax.set_xlim([-1.0, 1.0])
ax.set_ylim([-1.0, 1.0])
ax.set_zlim([0.0, 1.0])

# লেবেল এবং শিরোনাম
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Horn Antenna (3D)')

plt.show()

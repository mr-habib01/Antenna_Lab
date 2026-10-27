# 1. Study and Simulation of 3D Radiation Pattern of Dipole Antenna


import numpy as np
import matplotlib.pyplot as plt

# Angular grid
theta = np.linspace(1e-4, np.pi - 1e-4, 181)
phi = np.linspace(0, 2*np.pi, 361)
THETA, PHI = np.meshgrid(theta, phi)

# Normalized E-field pattern of a half-wave dipole
E = np.cos((np.pi/2) * np.cos(THETA)) / np.sin(THETA)
E = np.abs(E)
E /= E.max()

# Spherical to Cartesian coordinates
X = E * np.sin(THETA) * np.cos(PHI)
Y = E * np.sin(THETA) * np.sin(PHI)
Z = E * np.cos(THETA)

# Plot 3D radiation pattern
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(
    X, Y, Z,
    facecolors=plt.cm.jet(E),
    rstride=2, cstride=2,
    linewidth=0, antialiased=True,
    shade=False
)

ax.set_title("3D Radiation Pattern of a Half-Wave Dipole")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect((1, 1, 1))
plt.tight_layout()
plt.show()

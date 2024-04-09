import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np


# Create grid size
n = 60
axes = [n, n, n]

# Create Data
data = np.zeros(axes)

# Set the cross shape
data[:, n//2, n//2] = 1
data[n//2, :, n//2] = 1
data[n//2, n//2, :] = 1

# Colours
# Control Transparency
alpha = 0.9

# Control Colour 
colors = np.empty(axes + [4])
colors[:, :, :] = [1, 1, 1, alpha]  # Set all voxels to grey

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(data, facecolors=colors, edgecolors='grey')

plt.show()

# inital class for GOL
# By Francesca Brzoskowski


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
from scipy import signal

class Game:
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N, N, N), np.int64)
        self.neighborhood = np.ones((3, 3, 3), np.int64)  # 8 connected kernel
        self.neighborhood[1, 1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.N = N

        # Define the color gradient
        self.cmap = LinearSegmentedColormap.from_list('custom', ['yellow', 'pink', 'purple', 'darkblue'])


    def evolve(self):
        # Define the 3D kernel for convolution
        kernel = self.neighborhood
        kernel[1, 1, 1] = 0  # Exclude the center cell from convolution

        if self.finite:
            boundary = 'wrap'
        else:
            boundary = 'fill'

        for _ in range(1):
            # Get weighted sum of neighbors using convolution
            # weights = signal.convolve(self.grid, self.neighborhood, mode='same', method='direct')
            weights = np.around(signal.fftconvolve(self.grid, self.neighborhood, mode='same'))
            # Implement the Game of Life rules by thresholding the weights
            birth = (weights == 3) & (self.grid == self.deadValue)
            survival = ((weights == 6) | (weights == 7)) & (self.grid == self.aliveValue)
            self.grid = np.where(birth | survival, self.aliveValue, self.deadValue)

        return self.grid

    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def plot_3d_grid(self, grid):
        # Create a figure and a 3D axis
        fig = plt.figure(facecolor='black')
        ax = fig.add_subplot(111, projection='3d')

        # Set dark mode
        plt.style.use('dark_background')

        # Get grid dimensions
        grid_size = grid.shape[0]

        # Iterate over each cell in the grid
        for x in range(grid_size):
            for y in range(grid_size):
                for z in range(grid_size):
                    # If the cell is alive, plot it as a cube
                    if grid[x, y, z] == 1:
                        shade = 1 - (z / (grid_size - 1))  # Shade based on z-position
                        color = self.cmap(shade)
                        ax.bar3d(x, y, z, 1, 1, 1, color=color, alpha=0.7)

        # Set plot limits
        ax.set_xlim([0, grid_size])
        ax.set_ylim([0, grid_size])
        ax.set_zlim([0, grid_size])

        # Set plot labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        plt.show()

    def update_plot(self, frame, ax, grid_size):
        ax.clear()
        self.evolve()
        grid = self.getStates()

        # Plot live cells
        for x in range(grid_size):
            for y in range(grid_size):
                for z in range(grid_size):
                    if grid[x, y, z] == 1:
                        shade = 1 - (z / (grid_size - 1))  # Shade based on z-position
                        color = self.cmap(shade)
                        ax.bar3d(x, y, z, 1, 1, 1, color=color, alpha=0.7)

        # Set plot limits
        ax.set_xlim([0, grid_size])
        ax.set_ylim([0, grid_size])
        ax.set_zlim([0, grid_size])

        # Set plot labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        return ax,

    def animate(self, num_frames=64, interval=50):
        # Create a figure and a 3D axis
        fig = plt.figure(facecolor='black')
        ax = fig.add_subplot(111, projection='3d')

        # Set dark mode
        plt.style.use('dark_background')

        # Get grid dimensions
        grid_size = self.grid.shape[0]

        # Create animation
        ani = animation.FuncAnimation(fig, self.update_plot, frames=num_frames, fargs=(ax, grid_size), interval=interval, blit=False)

        # Show animation
        plt.show()

    def insert_blinker(self, index=(0, 0, 0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1] + 1, index[2] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1, index[2] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1, index[2] + 1] = self.aliveValue

    def insertGlider(self, index=(0,0,0)):
        '''
        Insert a glider construct at the index position
        '''
        x, y, z = index
        self.grid[x, y + 1, z] = self.aliveValue
        self.grid[x + 1, y + 2, z] = self.aliveValue
        self.grid[x + 2, z, z] = self.aliveValue
        self.grid[x + 2, y + 1, z] = self.aliveValue
        self.grid[x + 2, y + 2, z] = self.aliveValue
      

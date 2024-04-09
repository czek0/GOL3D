import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import signal

class GameOfLife3D:
    '''
    Object for computing Conway's Game of Life (GoL) in 3D
    '''
    def __init__(self, N=60, finite=False, fastMode=False):
        self.grid = np.zeros((N, N, N), np.int)
        self.neighborhood = np.ones((3, 3, 3), np.int)  # 26 connected kernel
        self.neighborhood[1, 1, 1] = 0  # do not count center voxel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0

    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid

    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules in 3D
        '''
        if self.finite:
            boundary = 'wrap'
        else:
            boundary = 'fill'

        # Get weighted sum of neighbors using convolution
        if self.fastMode:
            weights = np.around(signal.fftconvolve(self.grid, self.neighborhood, mode='same'))
        else:
            weights = signal.convolve(self.grid, self.neighborhood, mode='same')

        # Implement the GoL rules by thresholding the weights
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                for k in range(len(self.grid[0][0])):
                    if self.grid[i][j][k] == self.aliveValue:
                        if int(weights[i][j][k]) < 2:  # rule 1
                            weights[i][j][k] = self.deadValue
                        elif int(weights[i][j][k]) == 2 or weights[i][j][k] == 3:  # rule 2
                            weights[i][j][k] = self.aliveValue
                        elif int(weights[i][j][k]) > 3:  # rule 3
                            weights[i][j][k] = self.deadValue
                    else:
                        if int(weights[i][j][k]) == 3:  # rule 4
                            weights[i][j][k] = self.aliveValue
                        else:
                            weights[i][j][k] = self.deadValue

        # Update the grid
        self.grid = weights

    def insertBlinker(self, index=(0, 0, 0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        for i in range(3):
            self.grid[index[0] + i, index[1] + 1, index[2]] = self.aliveValue

# Function to plot cubes for alive cells
def plot_alive_cells(ax, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(len(grid[0][0])):
                if grid[i][j][k] == 1:
                    ax.scatter(i, j, k, color='b', marker='o')

# Initialize the Game of Life object
game = GameOfLife3D(N=60)

# Insert a 3x1 blinker oscillator
game.insertBlinker(index=(28, 28, 28))

# Plot the first three evolutions
for i in range(3):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_alive_cells(ax, game.getStates())
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Evolution {i+1}')
    plt.show()
    game.evolve()

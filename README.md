# 3D Conway's Game of Life

## Description
This is an implementation of the 3D version of Conway's Game of Life, a cellular automaton devised by the mathematician John Conway. The game simulates the evolution of a population of cells on a three-dimensional grid, following a set of simple rules.


## Demo

![](GOL3D.mov)

## Files
- `conway.py`: This file contains the `Game` class, which implements the logic of the game and provides methods for visualization and animation.
- `Conway_blinker.py`: This file contains an example of how to use the `Game` class, including initializing the game, inserting predefined patterns (blinker and glider), and visualizing the game's evolution.

## Rules of the Game
The rules for the 3D version of Conway's Game of Life are similar to the 2D version, but with a different neighborhood definition. In this implementation, a cell's neighbors are the 26 cells that surround it (including diagonals).

1. **Survival**: Any live cell with 2 or 3 live neighbors survives to the next generation.
2. **Death by Underpopulation**: Any live cell with fewer than 2 live neighbors dies in the next generation, as if caused by underpopulation.
3. **Death by Overpopulation**: Any live cell with more than 3 live neighbors dies in the next generation, as if caused by overpopulation.
4. **Birth**: Any dead cell with exactly 3 live neighbors becomes a live cell in the next generation, as if by reproduction.

## Usage
1. Make sure you have Python and the required libraries (numpy, matplotlib, scipy) installed.
2. Clone or download this repository:
   $ git clone https://github.com/your-repo/game-of-life-3d.git
3. Navigate to the project directory:
   $ cd game-of-life-3d
4. Run the script `Conway_blinker.py` using the command:
   $ python Conway_blinker.py

The script will initialize a `Game` object with a grid size of 60, insert a glider pattern at position (28, 28, 28), and evolve the game once. You can uncomment the lines in the script to visualize the initial state, the state after one evolution, or the state after two evolutions.

Alternatively, you can uncomment the line `life.animate()` to see an animated visualization of the game's evolution.

## Code Explanation

### `conway.py`
This file contains the `Game` class, which has the following methods:

- `__init__(self, N=256, finite=False, fastMode=False)`: Initializes the game with a grid of size `N x N x N`, and sets various parameters such as the neighborhood kernel, alive/dead values, and color gradient.
- `evolve(self)`: Applies the rules of the game to the current state of the grid and updates the grid for the next generation.
- `getStates(self)` and `getGrid(self)`: Returns the current state of the grid.
- `plot_3d_grid(self, grid)`: Visualizes the current state of the grid in a 3D plot.
- `update_plot(self, frame, ax, grid_size)`: A helper function used for animating the game's evolution.
- `animate(self, num_frames=64, interval=50)`: Creates an animated visualization of the game's evolution over `num_frames` generations, with an `interval` (in milliseconds) between each frame.
- `insert_blinker(self, index=(0, 0, 0))`: Inserts a "blinker" oscillator pattern at the specified `index` position in the grid.
- `insertGlider(self, index=(0, 0, 0))`: Inserts a "glider" pattern at the specified `index` position in the grid.

### `Conway_blinker.py`
This file demonstrates how to use the `Game` class. It creates a `Game` object with a grid size of 60, inserts a glider pattern at position (28, 28, 28), and then evolves the game once. The script also includes commented lines that allow you to visualize the initial state, the state after one evolution, or the state after two evolutions. Additionally, there is a commented line that allows you to see an animated visualization of the game's evolution.
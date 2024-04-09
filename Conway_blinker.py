from conway import *
from conway import Game
life = Game(60)
# life.insert_blinker((0, 0, 0))
life.insertGlider((28,28,28))
cells = life.getStates()  # initial state

# evolve once
life.evolve()
cellsUpdated1 = life.getStates()

# # evolve twice
# life.evolve()
# cellsUpdated2 = life.getStates()


# # see results
# life.plot_3d_grid(cells)
# life.plot_3d_grid(cellsUpdated1)
# life.plot_3d_grid(cellsUpdated2)

# ----------------------------------

# life.animate()
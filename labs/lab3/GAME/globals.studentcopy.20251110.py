'''globals.py makes it easier to import information that will be used throughout 
game. We can just call the function rather than retyping all of the things we 
need in the functions that use them.'''

#configuration of the board
ROWS = None
COLS = None
MINES = None

# Symbols and characters for board
MINE = "💣"
HIDDEN = "⬧"
BLANK = " "     # for cells with 0 adjacent mines

# Boards 
base_board = []     # holds the actual mines and numbers
display_board = []  # what the player sees

# Optional for easier debugging or expansion
DEBUG_MODE = False  # set True to print full board for testing
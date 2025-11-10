"""
globals.py

Stores global variables used across Minesweeper modules.
"""

# Board dimensions
ROWS = 8        # number of rows on the board
COLS = 8        # number of columns
MINES = 10      # total number of mines

# Board symbols
HIDDEN = "■"    # unrevealed cell display
FLAG = "⚑"      # optional: flag symbol if you want to add that feature later

# Game boards (will be filled in by initialize_board)
base_board = None
display_board = None

"""
globals.py
Stores global variables used across Minesweeper modules.
"""

# Board settings
ROWS = 8        # number of rows on the board
COLS = 8        # number of columns on the board
MINES = 10      # total number of mines

# Display symbols
HIDDEN = "■"    # symbol for unrevealed cell
FLAG = "⚑"      # optional flag symbol

# Boards (will be created in initialize_board)
base_board = None
display_board = None

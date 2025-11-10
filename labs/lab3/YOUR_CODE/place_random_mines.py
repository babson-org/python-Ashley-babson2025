"""
function: place_random_mines

This function randomly adds a "mine" to different squares on the board.
It updates the given board by placing a fixed number of mines (from globals.MINES),
each represented by the value 10.
"""

import random
import globals as g  # Access global constants like ROWS, COLS, and MINES

MINE_VALUE = 10  # Value used to represent a mine


def place_random_mines(board):
    """
    Randomly place mines on the board.

    Args:
        board (list of lists): 2D board with empty cells (usually 0).

    Returns:
        list of lists: Board with mines placed (marked as 10).
    """
    mines_placed = 0

    # Keep placing until we reach the desired number of mines
    while mines_placed < g.MINES:
        row = random.randint(0, g.ROWS - 1)

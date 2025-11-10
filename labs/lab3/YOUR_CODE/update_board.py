"""
update_board.py

Handles revealing cells on the display board when a player clicks a square.
If the chosen cell is a mine, the game ends.
If it's a 0 (no adjacent mines), automatically reveals neighboring cells.
"""

import globals as g
from get_adjacent_cells import get_adjacent_cells

MINE_VALUE = 10  # Consistent with other files


def reveal_cell(row, col):
    """
    Reveals a single cell on the display board.

    Args:
        row (int): row index
        col (int): column index

    Returns:
        bool: True if safe (not a mine), False if mine hit
    """

    # If already revealed, just ignore
    if g.display_board[row][col] != g.HIDDEN:
        return True

    # If it's a mine — reveal and signal game over
    if g.base_board[row][col] == MINE_VALUE:
        g.display_board[row][col] = "*"
        print("💣 BOOM! You hit a mine!")
        return False

    # Otherwise, reveal the cell value
    g.display_board[row][col] = str(g.base_board[row][col])

    # If there are no adjacent mines, reveal all connected empty cells
    if g.base_board[row][col] == 0:
        for (r, c) in get_adjacent_cells(row, col):
            if g.display_board[r][c] == g.HIDDEN:
                reveal_cell(r, c)

    return True

import globals as g
from get_adjacent_cells import get_adjacent_cells

MINE_VALUE = 10  # Value used to represent a mine

def count_adjacent_mines(board):
    """
    Updates the board so that each non-mine cell shows how many mines are next to it.
    The board is a list of tuples (display_symbol, value).

    Args:
        board (list of lists): the hidden board with mine positions
    """
    for r in range(g.ROWS):
        for c in range(g.COLS):

            # Skip mines
            if board[r][c][1] == MINE_VALUE:
                continue

            # Count neighboring mines
            mine_count = 0
            for (nr, nc) in get_adjacent_cells(r, c):
                if board[nr][nc][1] == MINE_VALUE:
                    mine_count += 1

            # Save as tuple (display_symbol, value)
            board[r][c] = (str(mine_count) if mine_count > 0 else " ", mine_count)

    return board

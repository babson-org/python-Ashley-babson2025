import globals as g
from get_adjacent_cells import get_adjacent_cells

MINE_VALUE = 10

def reveal_cell(row, col):
    """
    Reveals a cell and recursively reveals neighbors if the cell is 0.
    Updates g.display_board.

    Args:
        row (int)
        col (int)

    Returns:
        bool: True if safe, False if mine hit
    """

    # Already revealed
    if g.display_board[row][col][0] != g.HIDDEN:
        return True

    # Mine hit
    if g.base_board[row][col][1] == MINE_VALUE:
        g.display_board[row][col] = ("💣", MINE_VALUE)
        return False

    # Reveal the cell
    g.display_board[row][col] = (str(g.base_board[row][col][1]) if g.base_board[row][col][1] > 0 else " ", g.base_board[row][col][1])

    # If 0, recursively reveal neighbors
    if g.base_board[row][col][1] == 0:
        for (r, c) in get_adjacent_cells(row, col):
            reveal_cell(r, c)

    return True

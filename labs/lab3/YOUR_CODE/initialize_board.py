import globals as g
from place_random_mines import place_random_mines

def initialize_board():
    """
    Creates and initializes the Minesweeper boards:
      - base_board: stores mine locations and numbers (tuple: (display, value))
      - display_board: what the player sees (all hidden at start)

    Returns:
        list: The base board with mines and numbers
    """

    # Create empty base board with tuples (display_symbol, value)
    g.base_board = [[(g.HIDDEN, 0) for _ in range(g.COLS)] for _ in range(g.ROWS)]
    g.display_board = [[(g.HIDDEN, 0) for _ in range(g.COLS)] for _ in range(g.ROWS)]

    # Place mines (updates the second element of tuple)
    g.base_board = place_random_mines(g.base_board)

    return g.base_board

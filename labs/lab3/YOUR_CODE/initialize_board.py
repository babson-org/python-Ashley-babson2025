import globals as g
from place_random_mines import place_random_mines

def initialize_board():
    """
    Creates and initializes the Minesweeper boards:
      - base_board: stores mine locations and numbers
      - display_board: what the player sees (all hidden at start)

    Returns:
        list: The base board with randomly placed mines
    """

    # Create empty boards
    g.base_board = [[0 for _ in range(g.COLS)] for _ in range(g.ROWS)]
    g.display_board = [[g.HIDDEN for _ in range(g.COLS)] for _ in range(g.ROWS)]

    # Place mines on the base board
    g.base_board = place_random_mines(g.base_board)

    # Return the board with mines placed
    return g.base_board

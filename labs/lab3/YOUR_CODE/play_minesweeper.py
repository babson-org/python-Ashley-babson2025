import globals as g
from initialize_board import initialize_board
from count_adjacent_mines import count_adjacent_mines
from update_board import reveal_cell
from get_validated_input import get_validated_input
from game_won import game_won
from print_board import print_board

def play_minesweeper():
    print("💣 Welcome to Minesweeper!")

    # Initialize the boards
    g.board = initialize_board()
    count_adjacent_mines(g.board)

    revealed = set()

    while True:
        # Print current display board
        print_board(g.display_board, 0)

        # Get valid user input
        r, c = get_validated_input(g.ROWS, g.COLS, revealed)
        revealed.add((r, c))

        # Reveal the cell
        safe = reveal_cell(r, c)

        if not safe:
            # Hit a mine
            print_board(g.display_board, 1)

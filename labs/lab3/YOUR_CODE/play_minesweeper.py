import sys
print("DEBUG: sys.path =", sys.path)

import globals as g
from initialize_board import initialize_board
from count_adjacent_mines import count_adjacent_mines
from update_board import reveal_cell
from get_validated_input import get_validated_input
from game_won import game_won
from print_board import print_board


def play_minesweeper():
    print("💣 Welcome to Minesweeper!")

    # --- Board setup with debug ---
    try:
        initialize_board()  # sets g.base_board and g.display_board
        count_adjacent_mines(g.base_board)
        print("DEBUG: Boards initialized successfully")
        print("DEBUG: base_board =", g.base_board)
        print("DEBUG: display_board =", g.display_board)
    except Exception as e:
        print("ERROR during board setup:")
        traceback.print_exc()
        return  # stop execution if setup fails

    revealed = set()

    # --- Main game loop ---
    while True:
        try:
            print_board(g.display_board, 0)

            print("DEBUG: waiting for user input...")
            r, c = get_validated_input(g.ROWS, g.COLS, revealed)

            # Check for mine hit
            if g.base_board[r][c] == 10:  # MINE_VALUE
                g.display_board[r][c] = "*"
                print("💥 Boom! You hit a mine, game over")
                print_board(g.display_board, 1)
                break

            # Reveal the selected cell
            reveal_cell(r, c)

            # Mark cell as revealed
            revealed.add((r, c))

            # Check if the player has won
            if game_won(g.base_board, revealed):
                print_board(g.display_board, 0)
                print("🎉 Congrats! You cleared the board")
                break

        except Exception as e:
            print("ERROR during gameplay:")
            traceback.print_exc()
            break


if __name__ == "__main__":
    play_minesweeper()

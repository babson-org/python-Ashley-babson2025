def get_validated_input(rows, cols, revealed):
    """
    Asks the user for a row and column until valid input is given.

    Ensures the coordinates:
      - Are within the bounds of the board
      - Have not already been revealed

    Args:
        rows (int): Number of rows on the board
        cols (int): Number of columns on the board
        revealed (set or list): Collection of already revealed (r, c) cells

    Returns:
        tuple: (r, c) coordinates for a valid move
    """
    while True:
        try:
            user_input = input("Enter row and column separated by a space (e.g., 2 3): ")
            r, c = map(int, user_input.split())

            # Check if within bounds
            if 0 <= r < rows and 0 <= c < cols:
                # Check if not already revealed
                if (r, c) not in revealed:
                    return r, c
                else:
                    print("That cell is already revealed. Try again.")
            else:
                print("Coordinates out of bounds. Try again.")

        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

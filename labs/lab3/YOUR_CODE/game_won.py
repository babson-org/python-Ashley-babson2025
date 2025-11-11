#Returns True if all non-mine cells are revealed
#this is when you win the game - just leaving the bombs on the board
'''
check if player revealed cells w/ no bombs on the board. 
Loops through each cell - if it finds a non-mine cell (not = 10)
that hasn’t been revealed, it returns False. If all safe cells are revealed, 
it returns True, meaning the player has won.
'''
def game_won(board, revealed):
    for r in range(len(board)):
        for c in range(len(board[0])):
            # Mines are represented by the number 10, not "M"
            if board[r][c] != 10 and (r, c) not in revealed:
                return False
    return True


 
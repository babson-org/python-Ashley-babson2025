
#Returns True if all non-mine cells are revealed 
def game_won(board, revealed): 
    for r in range(len(board)): 

        for c in range(len(board[0])): 

            if board[r][c] != "M" and (r, c) not in revealed: 

                return False 

    return True 

 
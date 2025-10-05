    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
     
    while True:
        
        try:
            # TODO: Convert input to integer
            prompt = int(input ("Select an empty cell (1-9): "))
            
            # TODO: Validate move is in range and not taken
            if prompt < 1 or prompt > 9:
                print("Please enter a number between 1-9") #ensures number is in the bord 
                continue

            if abs(board[prompt-1]) == 10 :
                print("Cell is taken, please pick a new number betwee 1-9")
                continue 
 # TODO: Assign score['player'] to the selected cell on the board
            board[prompt-1] = score['player']  
            break      
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
   

#REPLACE SELECTED INDEX WITH 10 FOR PLAYER MOVE - REMEMBER INDEX FOR THIS WHERE 1 IS REALLY 0

    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8
pass

    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = int(input ("Select an empty cell (1-9): "))
    while True:
        try:
            # TODO: Convert input to integer ^^^^DONE ABOVE^^^^^^
            # TODO: Validate move is in range and not taken
            
        #USING A BOOL STATEMENT IF TRUE, CONTINUE LOOP, IF FALSE, ADD VALUE 

            pass
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
    # TODO: Assign score['player'] to the selected cell on the board

#REPLACE SELECTED INDEX WITH 10 FOR PLAYER MOVE - REMEMBER INDEX FOR THIS WHERE 1 IS REALLY 0

    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8
pass

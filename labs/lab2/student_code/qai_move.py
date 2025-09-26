def ai_move(board: list[int]):
    """
    ai_move(board): Chooses a random available move (used in easy mode).

        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    '''
    function: create AI that places an X as an opponent
    steps:
    #CANNOT = 10 OR -10 --> TAKE ABSOLUTE VALUE OF BOARD 
    - Create outer loop to cycle through board
    - Create loop to go thorugh each item in list 
        - if != 10, replace list item with 10
        - else, continue 
    - Return index for first != 10 
    '''
    # TODO: Loop through board
    
    for i in range (len(board)):
        if abs(board[i]) != 10: # TODO: Find the first index where abs(cell) != 10
            board[i] = 10
            return i # TODO: Return that index as the AI's move
        else:
            continue

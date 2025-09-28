def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
    '''
    1 | 2 | 3
    -----------
    4 | 5 | 6
    -----------
    7 | 8 | 9
    function: sums up rows, col, diagonals to determine winner mathematically 
    process:
        - set list index values to corrsponding letter --> a = item 1 in board 
        - Sum of wins= absolute value is 30
            line sum: 
                - sum 1,2,3
                - sum 4,5,6
                - sum 7,8,9
            column sum: 
                - sum a,d,g
                - sum b,e,h
                - sum c,f,i
            diagnol sum: 
                - sum a,e,i
                - sum c,e,g
    ''' 
    # TODO: Sum the values at board[a], board[b], board[c] 
    # TODO: Return 30 if X wins, -30 if O wins otherwise do not return
    # TODO: For each of the 8 ways to win
    # TODO: Check the cells in each row, column, or diagonal using line_sum
    # TODO: Return 0 if line_sum() didn't return 30 or -30
   
    winning_line = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
#checking winning lines
    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''          
        total = board [a], board [b], board [c]
        if total == 30:
            return 30
        elif total == -30: #elif just another if statement 
            return -30 
        return 0 
#run through the winning lines of board to see if they sum 30/-30
    for a , b , c in winning_line:
        result = line_sum(a, b, c)
        if result != 0:
            return result 
        return 0


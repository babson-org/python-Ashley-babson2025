def get_validated_input(rows, cols, revealed): 

#Ask user for row and column until valid input is given 
#USER PICKES SQUARE TO REVEAL
#Ensures within bounds of boards and is not already revealed  
# by checking if within board set up

    while True: 

        try:  
            user_input = input("Enter row and column separated by a space(ex. 2 3):") 
            r, c = map(int, user_input.split()) 
            if 0 <= r < rows and 0<= c< cols: 
                if (r, c) not in revealed: 
                    return r, c 

                else: 
                    print("That cell is already revealed, try again") 
            else:  
                print("Coordinates out of bounds, try again") 

        except ValueError: 
            print("Invalid input. Please enter two numbers separated by a space") 

 
"""
Lab 1 – Python Basics
Author: <Ashley Braren>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""
# ==============================
# Part 1: Draw a Diamond
# ==============================
'''
Draw diamond function: The goal of this function is to take user input
and draw a diamond with the height of the user input. The height is how many 
rows the diamond will fill

Process:
- Take user numeric user input using a loop to prevent user crash
- Drawing the top half, including the middle row (widest point) 
    - For this, taking input/2 + 1 to capture middle 
    - Spaces in the middle will have to increase by 2 to push both * to next widest point
- Drawing bottom half, deducting a row since the middle is counted for
    - input/2 - 1 to not add an extra row
    - decrease spaces in middle by two to taper towards one point at end 
'''
def draw_diamond():
    # TODO: Prompt user for an odd number
    #make sure number entered doesn't crash from user input with loop
    while True:
        try:
            height = int(input("Enter an odd number for the diamond height: "))
            if height % 2 == 0 : 
                print('Please enter an ODD number')
                continue
            break
        except ValueError:
            print("Please enter a numeric value")
    print(f"You entered: {height}")
# TODO: Draw the top half of the diamond
    for i in range(1,height + 1,2):
        '''
        - start at 1 so 0 doesn't print
        - height + 1 creates the middle row so there's no duplicate with bottom half
        - step is 2 since 2 stars have to be added in each row
        '''
        space = (height - i) // 2
        if i == 1: 
            print(" " * space + "*") 
            # adds a single start -> * space adds spaces to center it, works like a grid
            '''
            4 x 4 grid of printed characters
            _ _ _ *
            _ _ * _ 
            _ * _ _ 
            * _ _ _
            
            '''
        else: 
            print(" " * space + "*" + " " * (i- 2) + "*")
            # _*___* -> first space, start, inside space (i-2) since 2 stars, followed by second *

# TODO: Draw the bottom half of the diamond
    for i in range(height-2, 0 , -2 ): #stop at 0, not 1 because last num not included
        space = (height - i )//2
        if i == 1: 
            print(" " * space + "*")
        else: 
            print(" " * space + "*" + " " * (i- 2) + "*")

'''
- height starts 2 below since the top half has more to create middle
- spaces 
- i counts up on the top and down on the bottom
'''
draw_diamond()

# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Text Analysis Function: Take user input and give a simple overview of the text 
    by counting letters, words, and sentences combining tools from previous exercises

    Process:
    - Ask the user for a block of text - is there a loop to prevent crash?
    - using alpha function, count characters that are LETTERS
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """
    # TODO: Get user input
    text = input("Enter some text: ").strip()
    
    # initialize counter
    #letters = 0 - count alphabetical characters
    # words = 1 - starts at 1 to count last word
    # setences = 0 - count sentence ending punctuation

    # TODO: Count letters
    letters = 0
    for az in text:
        if az.isalpha():
            letters += 1

# put all in for loop - if char alpha letter += 1, elif char == ' ' words = += 1 elif char in (.,?,!) sent = += 1

    # TODO: Count words
# use len after splits!
    words = len(text.split()) 
    # breaking text string into separate strings based on word

    # TODO: Count sentences
# count how many . ? ! there are with a count 
    sent = text.count("?") + text.count ("!") + text.count (".")

    # TODO: Print the results
    # { } prints the value of the var 
    print(f"Letters: {letters}")
    print(f"Words: {words}")  #  broke string into sepaarte strings, counting separate strings     
    print(f"Sentences: {sent}")    

# Uncomment to test Part 2
text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
#SHIFTING BY ASSIGNED NUMBER TO LETTER NOT BY NUMBER IN STRING!!!
#MAKE ALL UPPERCASE OR ALL LOWERCASE TO ELIMINAT EXTRA ORD STEPS
def caesar_cipher():
    """
    Caeser Cipher Function: Taking user input and shifting values to code or decode a message
    Process:
    - Take user text input
    - Take user number input - this is what characters are "shifting" by
    - Each letter in alphabet has a numeric assignment (ord function)
    - with original message, assign each letter to its corresponding value
    - to encrypt - ADD shift number to ord value and assign to new variable
        -  "new number" = original number + shift, showing the letter with the corresponding NEW value
    - to decrypt do same but REVERSE shift in opposite direction
        - moves letters back from encrypted message by the value they were shifted by
    """
    # TODO: Get user input text
    text = input("Enter text: ").lower()

    # TODO: Get shift value
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a numeric value")
    print(f"You entered: {shift}")

    # TODO: Ask user whether to encrypt or decrypt
    while True:
        choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
        if choice in ["e", "d"]:
            break
        else:
            print("Invalid choice. Please type 'e' or 'd'.")

    # TODO: Implement encryption and decryption logic
    result = ""
    #assigning number to char in text 
    for char in text: 
        if char.isalpha():
            start = ord ('a')
            position = ord(char)- start
    # ord function: unicode integer value for letter -> each letter has numeric representation
    #encryption
            if choice == 'e':
                new_ord = (position + shift) % 26 #wraps to beggining for end letters
            else: 
                new_ord = (position - shift) % 26
            newchar = chr(start + new_ord)
        #chr function: converts unicode integer value to a letter
            result += newchar
        else:
            result += char

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()



# ==============================
# Main Program
# ==============================
def main():
    print("Lab 1 - Python Basics")
    print("1. Draw Diamond")
    print("2. Text Analysis")
    print("3. Caesar Cipher")
    choice = input("Select part to run (1-3): ")
    
    if choice == "1":
        draw_diamond()
    elif choice == "2":
        text_analysis()
    elif choice == "3":
        caesar_cipher()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
    
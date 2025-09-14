"""
Lab 1 – Python Basics
Author: <Ashley Braren>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""
# ==============================
# Part 1: Draw a Diamond
# ==============================
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
        print(" "* space + "*" * i)
    for i in range(height-2, 0 , -2 ): #stop at 0, not 1 because last num not included
        space = (height - i )//2
        print(" " * space + "*" * i)
# TODO: Draw the bottom half of the diamond
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
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """
    # TODO: Get user input
    text = input("Enter some text: ")
    
    # TODO: Count letters
    letters = 0
    for az in text:
        if az.isalpha():
            letters += 1
            

    # TODO: Count words
# use len after splits!
    words = len(text.split())

    # TODO: Count sentences
# count how many . ? ! there are with a count 
    sent = text.count("?") + text.count ("!") + text.count (".")

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {words}")        # replace 0
    print(f"Sentences: {sent}")    # replace 0

# Uncomment to test Part 2
text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
#SHIFTING BY ASSIGNED NUMBER TO LETTER NOT BY NUMBER IN STRING!!!
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """
    # TODO: Get user input text
    text = input("Enter text: ")

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
            start = ord('A') if char.isupper() else ord ('a')
            position = ord(char)- start
    #encryption
            if choice == 'e':
                new_ord = (position + shift) % 26 #wraps to beggining for end letters
            else: 
                new_ord = (position - shift) % 26
            newchar = chr(start + new_ord)
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
    
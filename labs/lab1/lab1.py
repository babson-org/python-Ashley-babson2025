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
#have to add 2 stars to i for each additional row 
#have to subtract spaces with each row 
    for i in range(1,height + 1,2):
        space = (height - i) // 2
        print(" "* spaces + "*" * i)
        #finish bottom half come back to 
# TODO: Draw the bottom half of the diamond
# start with most stars and decrease on way down starting with stars then add spaces
    for i in range(1,"height"):
        #make space var for here too 
        print("*"* + " "(height+1))
draw_diamond()

  



# Uncomment to test Part 1
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

    # TODO: Count words

    # TODO: Count sentences

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {0}")        # replace 0
    print(f"Sentences: {0}")    # replace 0

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """
    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
    result = ""

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()


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

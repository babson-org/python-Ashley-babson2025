from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
steps=['step1','step2','step3']
def make_tea(myList):
    myList[2] = "step5"
    for item in myList:
        print(item)
    

make_tea(steps)
print(steps)

# enter your code here

'''Another way to do it:
steps = ['step1','step2','step3]
def make_tea(myList):
    myList[2] = "step 5"
    for item in myList:
        print(item)

make_tea(steps) #passes list of steps into function and calls the function
        '''

def make_tea():
    print("How to make tea:")
    print("step one: pick tea flavor")
    print("step two: fill pot with water")
    print("step three: put pot on stove on high")
    print("step four: wait for it to boil")
    print("step five: once boiling add to mug")
    print("step six: put tea bag in mug with boiled water")
    print("step seven: wait for tea bag to steep")
    print("step eight: enjoy")
make_tea()

pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
list = [2,4,6,8,10]
list.append(list[4]+2)
list.append(list[5]+2)
list.append(list[6]+2)
print(list)

'''
for i in range(3):
    next = nums[-1] + 2 + i *2
    print(next)
'''

pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
first_name = input("Enter first name:")
last_name = input("Enter last name:")
print("Hello", first_name, last_name)

pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here
import sys
import platform 
import pprint

pprint.pprint(dir(sys))
print(sys.version)
print(sys.platform)

pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here

'''
txt = 'please enter an integer:'
while True:
    try:
        x = int(input(txt))
        break
    except ValueError:
        txt = 'follow directions, enter a number:'

        other functions instead of operators:
        - total
        - diff
        - prod
        - div 
        - flr (rounded down div)
    '''
#program will crash in this version, use try and except block to mitigate crash from user
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print("Here are some math functions")
print("addition:", num1+num2)
print("subtraction:", num1-num2)
print("multiplication", num1*num2)
print("division:",num1/num2)
print("rounded division:", num1//num2)

pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''
txt = input('please entr some text:')
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.split())

# enter your code here
sent = input("Enter a short sentence:")
print(sent.upper())
print(sent.lower())
print(sent.capitalize())
for word in sent.split():
    print(word)


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here
10 + 2 * 5 / 2 - 3 ** 2
(10 + ( 2 * 5)) / (2 - (3 ** 2))
pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
fav_food = ["sushi", "pizza", "popcorn"]
fav_food [1] = "pickles"
print(fav_food)

pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
t = (7,3,1)
t[1] = 8
print(t)

pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here
dictionary = {"name": "Ashley", "age": 20}
dictionary["age"] = 100
print(dictionary)
favorite_numbers = [7,3,8]
favorite_numbers.append(14)
print(favorite_numbers)

pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here
quote = input("Enter your favorite quote:")
with open('quotes.txt', 'w') as f:
    f.write(quote)
with open('quotes.txt', 'r') as f:
    content = f.read()
print(content) 
# end open file


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here
numbers = []
for i in range (5):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

print(sum(numbers))
print(sum(numbers)/len(numbers))


pause=input('pause')
clear_screen()






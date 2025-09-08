#%%
# print 'hello' 5 times using an arithmetic operator
print ("Hello"*5)

#%%
# print 'hello' 5 times using a loop
count = 0 
while count < 5:
    print ("Hello")
    count += 1
    #you can do count = count + 1 as well - addressing what is in the addressed count
#%%
# print 'hello' 5 times on the same line using a loop
count = 0 
while count < 5:
    print ("Hello", end="...")
    count += 1
print ()
    #have to add print function to add a new line - after loop stays on same line
    # end replaces new line with something else in this case "..."
#%%
''' using nested loops print the following:

00 01 02
10 11 12
20 21 22
'''
#outerloop runs before inner loop does
#pattern - outside increases by 10, following increases by 1
row = 0
while row < 3:
        col = 0
        while col < 3:
             print ((str(row) + str(col)), end = " ")
             col += 1
        print(" ")     #prints new line after the the nested loop runs this is in the outside loop
        row +=1

'''
HOW TO CLEAN UP USING A FORLOOP
for row in range (3): #row
     for col in range(3): #column this is the nested loop
          print(str(row) + str(col), end = " ")
     print ()
print()
'''

#%%
# define txt and input some text from the keyboard into it
txt = "Enter name"
choice = (input(txt))

#%%
# print each letter in txt 
txt = "Enter name"
choice = (input(txt))
print(choice)
#%%
# assign the variable letter to the first letter in txt
choice_txt = "Enter name"
txt = (input(txt))
print(txt)
letter = txt[0]
#%%
# print out all the letters in txt that are equal to the first letter
choice_txt = "Enter name"
txt = (input(txt))
letter = txt[0]
if txt == letter:
     print(letter)

'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''

#%%
'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
             1) use len(), %, enumerate
                  2) also assign shifted_list = [None] * length  (you'll need to determine 
                          the length variable)
                               3) shift inside the for loop
                                    4) print out the printed list outside the for loop
                                    '''



 # %%
myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length 

shift = 3

for idx in range(length):
     new_idx = (idx+3) % length
     shifted_list[new_idx]= myList[idx]
print(shifted_list)

for idx,item in enumerate(myList):
     #enumerate goes through list and in idx puts in index, in item it puts in value 
     print(idx, item)

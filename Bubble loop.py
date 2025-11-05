
#checking each number in a list, and then swapping them 
def bubble_sort(values):
    sorted = values.copy()
    size = len(sorted)

for pass_num in range(size-1):

    for idx in range (size - 1 - pass_num):
        if sorted[idx] > sorted[idx+1]:
            sorted[idx], sorted[idx+1] = sored[idx+1], sorted[idx]

return(sorted)


#function that takes in 2 lists and merges them together to make one sorted list of outpu c
#start by combining the lists 
#then sort normally 


#need to check against both lists and append
left = [1,7,27,36]
right = [3,6,15,39]

def combine(left,right):
    array = []
    l_cur = 0
    r_cur = 0 

    cnt = 0
    while cn < 50:
        cnt += 1


#def combine





def combine(left, right):
    array = []
    l_cur = 0
    r_cur = 0

    cnt = 0

    while l_cur < len(left) and r_cur < len(right): 
        if left[l_cur] < right[r_cur]:
            array.append(left[l_cur])
            l_cur += 1
        else:
            array.append(right[r_cur])
            r_cur +=1

    return array + left[l_cur:]+ right[r_cur:]

#using the combine function to arrang list [54321]
#diving list into two lists, use combine method to put both together 
#keep building algorith until its sorted 

#need to be able to split data 



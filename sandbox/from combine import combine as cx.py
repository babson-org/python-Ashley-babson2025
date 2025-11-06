from combine import combine as cx

def combine_sort(unsorted):
    size = len(unsorted)
    left = unsorted[0:1]  # start with the first element

    for idx in range(1, size):
        right = [unsorted[idx]]  # wrap single element in list
        left = cx(left, right)   # combine keeps it sorted

    return left

print(combine_sort([5,4,3,2,1]))



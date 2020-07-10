def linear_search(arr, target):
    # Your code here
    target_index = -1
    for item in arr:
        target_index += 1
        if item == target:
            return target_index

    return -1   # not found

import math
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    left = 0
    right = len(arr)-1

    while left <= right:
        pivot = math.ceil((left+right)//2)
        if arr[pivot] == target:
            return pivot
       
        if arr[pivot] < target:
            left = pivot + 1    
        elif arr[pivot] > target:
            right = pivot-1


    return -1  # not found

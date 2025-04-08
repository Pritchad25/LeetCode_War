#!/usr/bin/python3
"""Given an array containing 0s, 1s and 2s, sort the array in-place. You should 
treat numbers of the array as objects, hence, we can't count 0s, 1s, and 2s 
to recreate the array.

Approach:
1. We can use a Two Pointer's approach while iterating through the array. Let's say 
the two pointers are called low and high which are pointing to the first and the 
last element of the array respectively. 
2. So while iterating, we will move all 0s before low and all 2s after high so that 
in the end, all 1s will be between low and high.
"""
def swap(arr, i, j):
    '''Swaps two numbers'''
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def DutchNationalFlag(arr):
    '''Sorts an array of 0s, 1s & 2s IN-PLACE'''
    #all elements < low are 0 and all elements > high are 2
    #all elements from >= low < i are 1
    low = 0
    high = len(arr) - 1
    for i in range(high + 1):
        if arr[i] == 0:
            swap(arr, i, low)
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else: #the case for arr[i] == 2
            swap(arr, i, high)
            #decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1
    return (arr)

print(DutchNationalFlag([1, 0, 2, 1, 0]))

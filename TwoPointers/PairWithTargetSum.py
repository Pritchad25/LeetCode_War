#!/usr/bin/python3
'''Pair With Target Sum (Easy)
Given an array of sorted numbers and a target sum, find a pair in the array whose 
sum is equal to the given target. Write a function to return the indices of the two 
numbers (i.e. the pair) such that they add up to the given target.
Solution
1. Given that the input array is sorted, an efficient way would be to start with 
one pointer in the beginning and another pointer at the end. Lets call the pointer
in the beginning `left` and initialize it with the index of the first element of the
array which is 0, ie, left = 0 and the end pointer `right` and initialize it with
the index of the last element of the array, which can be found as len(array) - 1, ie
right = len(array) - 1
2.  At every step (ie for each iteration), we will see if the numbers pointed by the 
two pointers add up to the target sum. So, our loop will only run if the start
point is always < end pointer. If they do not, we will do one of two things:
    (i) If the sum of the two numbers pointed by the two pointers is > target 
    sum, this means that we need a pair with a smaller sum. So, to try more pairs, we 
    can decrement the end-pointer, ie, right--
    (ii) If the sum of the two numbers pointed by the two pointers is < the 
    target sum, this means that we need a pair with a larger sum. So, to try more pairs, 
    we can increment the start-pointer, ie left++
'''

def PairWithTargetSum(arr, targetSum):
    '''Returns the indices of the pair of elements
    whose sum == targetSum.
    '''
    left = 0 #the start pointer initialized with index of element at the beginning of array
    right = len(arr) - 1 #end pointer initialized with the index of the last element of array
    resultIndices = [] #stores the indices of the elements whose sum == targetSum
    #iterate through the elements while left < right
    while (left < right):
        currentSum = arr[left] + arr[right] #keep track of the sum of the current elements 
        #pointed to by the pointers
        if currentSum == targetSum:    #append the indices of those elements to the list if true
            resultIndices.append(left)
            resultIndices.append(right)
            return resultIndices
        if currentSum > targetSum:
            right -= 1 #decrement the end pointer. we need a pair with a smaller sum
        else: #means currentSum is less
            left += 1 #increment the start pointer. we need a pair with a bigger sum
    return [] # an empty list

print("The elements whose sum == targetSum are in indices: ", PairWithTargetSum([2, 5, 9, 11], 11))
'''Time Complexity: O(N)
Space Complexity: O(1), because as the size of the input grows exponentially, the
size of the memory space where our data and variables are going to be stored will remain the 
same, eg if it was 8 bytes in total, it will remain as is, that is CONSTANT and also because
vele u8 is a constant.
'''

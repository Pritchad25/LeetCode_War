#!/usr/bin/python3
from collections import deque
'''Medium
Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less
than the target number.

Pattern: This problem follows the Sliding Window and the Two Pointers pattern
Similarities: Triplets With Smaller Sum with 2 differences:
    (i) In this problem, the input array is not sorted.
    (ii) Instead of finding triplets whose sum < a target, we need to find 
    all subarrays having a product < target. Meaning the length of these
    subarrays is not necessarily 3 but varies from 1 up to possibly length 
    of the array
Approach:
The implementation will be quite similar to Triplets With Smaller Sum.
deque is a class in the collections module of Python. It stands for double-ended queue
which allows to add or remove elements at both ends efficiently.In this case,deque was used to
create a temporary list `temp_list` that could efficiently add elements to the beginning 
with the `appendleft` method. This list was then converted to a regular list and added to the
`result` list.
'''
def SubarrayProductLessThanTarget(arr, target):
    '''Finds and returns ALL of the contiguous subarrays whose
    product is less < target.
    '''
    result = []
    product = 1 #because the 1 * k = k, where k is a constant
    left = 0
    for right in range(len(arr)): #iterates through the whole array
        product *= arr[right] #every element in the array is a subarray, meaning it has the
        #potential or high chance of having a product < target, hence we check for every element
        #of the array
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left - 1, -1): #
            temp_list.appendleft(arr[i])
            result.append(list(temp_list)) #we want to store the state of temp_list at this 
            #specific point in time. By using list(temp_list), we ensure that result contains 
            #a snapshot of temp_list's contents at the time of the append operation.
    return result

print(SubarrayProductLessThanTarget([2, 5, 3, 10], 30))
'''Time Complexity: The main for loop managing the sliding window takes
O(N) but creating subarrays can take up to O(N2).in the worst case. 
Therefore overall, our algorithm will take O(N3).
Space Complexity: O(N2) space will be required for the output list, while
the algorithm runs in O(N) space which is used for the temp list.'''

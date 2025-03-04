#!/usr/bin/python3
''' EASY
1. We will start by adding one element at a time to the sum of the current window, ie, append to windowSum
until the windowSum >= S
2. These elements will constitute our Sliding Window (subarray) and we are asked 
the smallest such window (subarray) whose sum is >= S. We will keep track of the 
length ((windowEnd - windowStart) + 1) of this window as the smallest window so far.
3. We will continue adding an element to the Sliding window(subarray) ie slide the window
ahead in a stepwise fashion.
4. In each step, we will also try to shrink the Sliding window if the windowSum >= S. We will
shrink the window until the windowSum < S, as we want to find the smallest window whose sum is >= S.
5. While shrinking, we will also do two things:
    1) keep track of the length of current window as the smallest window so far.
    2) shrink the Sliding window, ie subtract the element at the start of the window, from windowSum
    3) slide the window ahead, ie increment windowStart
'''

def findSmallestSubArrayGivenSum(arr, S):
    '''finds the smallest subarray whose sum is >= S'''
    windowStart = 0 #keeps track of the start of every window
    windowSum = 0 #keeps track of the sum of the current window
    minLength = float('inf') # assigning infinity to it, keeps track of the smallest subarray so far
    #iterating through every element of the array
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        #shrinking the window until its sum < S
        while (windowSum >= S):
            minLength = min(minLength, (windowEnd - windowStart) + 1)
            windowSum -= arr[windowStart] #shrink the Sliding Window
            windowStart += 1 #slide the window ahead
    return minLength

print("Length of the smallest subarray whose is >= S is:", findSmallestSubArrayGivenSum([3, 4, 1, 1, 6], 8))
'''The time complexity of this algorithm is O(N): the outer loop runs for every element,
and the inner loop processes the inner loop processes each element only once,
therefore the time complexity of the algorithm will be O(N+N) which is asymptotically 
equivalent to O(N). 
The space complexity is the amount of memory taken by an algorithm to run based
on or in relation to the input. It represents the MAXIMUM amount of memory that is a
needed AT ANY POINT during the execution of the algorithm.
There's 2 types space complexity: 
    1) Fixed space complexity is when the size of the space required to store data and variables
    is independent of the size or the length of the input.
    2) Variable space complexity is when the size of the space required to store data and variables
    is dependent on the size or length of the input.

In this algorithm, regardless of the input size, we are using only a 
fixed number of variables, windowStart, maxSum, windowSum and 
windowEnd. These variables(in ternms of total number) do not change with the size of 
the input array.Therefore, the space complexity is constant, or O(1), because the amount 
of memory used (to store the variables and data) does not change with the size of the input, 
and is therefore INDEPENDENT of the input size.
Created on Feb 21, 2024
@author: Pritchard Ncube
''' 
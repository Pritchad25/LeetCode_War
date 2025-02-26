#!/usr/bin/python3
'''Maximum Sum Subarray with size K.
Given an array of positive numbers & a positive number 'k', 
find maximum sum of any contiguous subarray of size k.
'''
'''
1. We are going to add 1 element at a time to the current value of windowSum, ie append the element to WindowSum
until we reach the end of the window, symbolised by k - 1.
2. These elements will constitute our Sliding window (or subarray). We are told to find the maximum sum of such a
window. So, we will keep track of the sum of the current window, call it windowSum.
3. In each step, we will try to slide the window ahead (add the element at the end of the current window), 
in a stepwise fashion.
4. We will slide the window ahead, if we have reached the end of the current window, symbolised by k - 1.We will
continuously do so as long as we're at the end of window. While sliding the window ahead, we will do 3 things:
           i) keep track of the sum of the current window as the highest sum so far
           ii) shrink the window, ie, shrink the sum of the current window, by taking away the element
           at the start of window
           iii) slide the window ahead.
'''
def findMaxSumSubArray(arr, k):
    '''finds the max sum of a contiguos subarray.'''
    windowStart = 0   #keeps track of the start of every window
    maxSum = 0  # keeps track of the window with highest sum so far
    windowSum = 0 # keeps track of the sum of the current window
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if (windowEnd >= k - 1):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum

print('Maximum Sum of a subarray with size k is:', findMaxSumSubArray([2, 1, 5, 1, 3, 2], 3))    
'''Time complexity: O(N), linear time, as the loop runs for every element of the array
   Space Complexity: O(1), constant space, because the amount of memory space needed
   to store the data and variables does not change with the size of the input, ie the
   memory space is fixed.
'''
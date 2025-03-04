#!/usr/bin/python3
'''Find average of Contiguous Subarray.'''
'''1. We are going to add 1 element at a time to the current value of windowSum, ie append the element to WindowSum
until we reach the end of the window, symbolised by k - 1.
2. These elements will constitute our Sliding window (or subarray). We are told to find the average of such a
window. So, we will keep track of the sum of the current window, call it windowSum.
3. In each step, we will try to slide the window ahead (add the element at the end of the current window), 
in a stepwise fashion.
4. We will slide the window ahead, if we have reached the end of the current window, symbolised by k - 1.We will
continuously do so as long as we're at the end of window. While sliding the window ahead, we will do 3 things:
           i) append to a list the average of the current window
           ii) shrink the window, ie, shrink the sum of the current window, by taking away the element
           at the start of window
           iii) slide the window ahead.
'''

def findAverageSubArray(arr, k):
    '''find the average of all contiguos subarrays
    in the array.'''
    windowStart = 0
    windowSum = 0
    result = []
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if (windowEnd >= k - 1):
            result.append(windowSum / k)
            windowSum -= arr[windowStart]  #shrinking the window
            windowStart += 1     #sliding the window ahead
    return result

print("The averages of all contiguous subarrays are:", findAverageSubArray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
        

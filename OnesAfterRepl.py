#!/usr/bin/python3
'''Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s 
with 1s, find the length of the longest contiguous subarray having all 1s
Pattern: Sliding Window Pattern
Similarity: Longest Subarray with same letters after Replacement.
Algorithms: at least 1 loop and 1 if statement
D.S: HashMap
Approach:
1. We will add number at a time starting from the beginning of the array into our HashMap, 
where our HashMap keeps track of the frequency of each number.
2. These numbers will constitute our Sliding Window; we are asked to find the longest such window
with the 1's AFTER REPLACEMENT. We will keep track of the length of this window as the longest so far.
We will also keep track of the count of the maximum number of times 1 is repeating for the 
current window, ie, we keep track of the count of HIGHEST NUMBER OF TIMES 1 is repeating for the current 
window, lets call it maxOnesRepeatCount. This means that for every 1 that we add to our Sliding window,
this variable has to be accounted for, ie checked/catered for, for every iteration, because we dont know
where the window with the highest/max number of repeating 1's occurs, so for every 1 that we add into our
sliding window or subarray, that window has the potential of having the 1's REPEATING THE HIGHEST NUMBER OF
TIMES.

3. So at any time (ie for every iteration), we know that there is a window which has 1 repeating the HIGHEST 
NUMBER OF TIMES and because we dont know where that window or subarray occurs and since each window has 
the potential of having 1 REPEATING THE HIGHEST NUMBER OF TIMES, we should try to replace the 
remaining 0's IN EVERY ITERATION.
-So for each iteration, after we have incremented the frequency of each 1, we have to check the frequency 
of each 1 if its highest, compared to the current value for maxOnesRepeatCount

4. WE REPLACE THE REMAINING LETTERS by incrementing max_length (which keeps track of the longest substring
with 1's AFTER REPLACEMENT)
Number of remaining 0'S to replace = window size - maxOnesRepeatCount
If the Number of remaining 0'S to replace <= K, then we HAVE TO REPLACE THOSE 0's, by incrementing max_length. 
So in essence, if the second if statement's condition evaluates to false, then it means the Number of 
remaining 0'S to replace <= K, so we replace them by incrementing max_length.

5. In each step, we will also try to shrink the Sliding window, if Number of remaining 0'S to replace > K,
because we arent allowed more than K 0's, we can only replace K 0's.
Either, we are shrinking the Sliding window or REPLACING THE REMAINING 0's, meaning THESE TWO EVENTS ARE 
MUTUALLY EXCLUSIVE.
'''
def LongStrOnesAfterRepl(arr, k):
    windowStart = 0 #keeps track of the start of every windoW
    max_length = 0 #keeps track of the longest subarray with 1's only after replacement
    maxOnesRepeatCount = 0 #keeps track of the count of the HIGHEST NUMBER OF TIMES 1 is repeating for the current window
    numFreqMap = {} #keeps track of the freq of each 0 and 1
    #iterates through each element of the array
    for windowEnd in range(len(arr)):
        rightNum = arr[windowEnd]
        if rightNum not in numFreqMap:
            numFreqMap[rightNum] = 0
        #otherwise, ALWAYS increment the number's frequency
        numFreqMap[rightNum] += 1
        #check the frequency of each 1 if its highest, compared to the current value for maxOnesRepeatCount
        maxOnesRepeatCount = max(maxOnesRepeatCount, numFreqMap[rightNum])
        #try to shrink the window if Number of 0's to replace is > K
        if(((windowEnd - windowStart) + 1) - maxOnesRepeatCount > k):
            leftNum = arr[windowStart]
            numFreqMap[leftNum] -= 1 #shrink the window
            windowStart += 1 #slide the window ahead
        #otherwise, REPLACE THE REMAINING 0's by incrementing the remaining max_length
        max_length = max(max_length, (windowEnd - windowStart) + 1)
    return max_length

print("Length of longest Substring with ones after replacement is:", LongStrOnesAfterRepl([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

'''Time Complexity: O(N), where N is the number of elements in the array
Space Complexity: O(1), since we can expect a fixed set of input, which is 1s and 0's'''

 
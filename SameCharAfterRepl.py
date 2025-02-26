#!/usr/bin/python3
'''
Given a string with lowercase letters only, if you are allowed to replace no more than 
'k' letters with any letter, find the length of the longest substring having the 
same letters after replacement.

Pattern: Sliding Window
Similarity: Longest Substring with No repeating chars
DS: HashMap to count the frequency of each letter.
Approach.
1. We will add one char at a time to our HashMap starting from the beginning where our HashMap
keeps track of the frequency of each letter.

2. These chars will constitute our Sliding Window and we are told to find the longest such window
with same letters after replacement. We'll keep track of the count of the letter that is repeating
the HIGHEST NUMBER OF TIMES in the current window (meaning for every letter we add to our Sliding
Window, this variable has to be accounted for, ie checked/catered for, for every iteration, because we 
dont know which letter repeats the HIGHEST), lets call it maxRepeatLetterCount. 

maxRepeatLetterCount has to be dealt with for every iteration, why?because, first of all we dont know where 
in the current window we are going to have a letter that is repeating the HIGHEST NUMBER OF TIMES, so 
for each iteration,after we have incremented the frequency of each letter, we have to check 
the frequency of each letter if its the highest, compared to the current value for maxRepeatLetterCount.So in other
words, each letter has the potential of repeating the HIGHEST NUMBER OF TIMES for this window, so hence we check for
every letter.

3. So at any time (FOR EVERY ITERATION) we know that there is a window which has 1 letter repeating 
maxRepeatLetterCount, that is, repeating the HIGHEST NUMBER OF TIMES, so we should try to replace the remaining
letters. WE REPLACE THE REMAINING LETTERS by incrementing max_length(which keeps track of the longest substring
with same letters AFTER REPLACEMENT).
Number of remaining letters to replace = window size - maxRepeatLetterCount
If Number of letters remaining to replace is <= K, then we have to replace THOSE letters, by 
incrementing max_length. So in essence, if the second if statement's condition evaluates to false, then it means 
the Number of letters remaining to replace is <= K, so we replace them by incrementing max_length.

4.In each step, we will also try to shrink the Sliding window, if Number of letters remaining to replace is > K.
5. Either, we are shrinking the Sliding window or REPLACING THE REMAINING LETTERS, meaning THESE TWO EVENTS ARE 
MUTUALLY EXCLUSIVE.
'''


def LongStrSameCharAfterRepl(str1, k):
    '''Returns the longest substring with the same
    letters AFTER REPLACEMENT.
    '''
    windowStart = 0 #keeps track of the start of every window
    maxRepeatLetterCount = 0 #keeps track of the count of the letter repeating THE HIGHEST NUMBER OF TIMES FOR A WINDOW
    max_length = 0 #keeps track of the length of the longest substring with same letter AFTER replacement
    charFreqMap = {} #keeps track of the frequency of each letter
    #iterates through the entire string
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        #assign 0 if char not in Map
        if rightChar not in charFreqMap:
            charFreqMap[rightChar] = 0
        #otherwise, ALWAYS INCREMENT its frequency by 1
        charFreqMap[rightChar] += 1
        #check if the frequency each letter is the highest compared to current value of maxRepeatLetterCount
        #if so, assign it to maxRepeatLetterCount
        maxRepeatLetterCount = max(maxRepeatLetterCount, charFreqMap[rightChar])
        #shrink the window if the number of remaining letters to replace is > K
        if (((windowEnd - windowStart) + 1) - maxRepeatLetterCount > k):
            leftChar = str1[windowStart]
            charFreqMap[leftChar] -= 1 #shrink the Sliding Window, done by decrementing its frequency
            windowStart += 1 #slide the window ahead
        #otherwise, if we not shrinking, REPLACE THE REMAINING letters
        max_length = max(max_length, (windowEnd - windowStart) + 1)
    return max_length

print("Length of longest Substring with same letter after replacement is:", LongStrSameCharAfterRepl("aabccbb", 3))

'''Time Complexity is: O(N), where N is the number of letters in the string
    Space Complexity: O(1) As we are expecting only the lower case letters in 
    the input string, we can conclude that the space complexity will be
    O(26), to store each letter's frequency in the HashMap, which is 
    asymptotically equal to O(1).
'''
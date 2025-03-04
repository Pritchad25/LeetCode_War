#!/usr/bin/python3
'''Permutation in String
Given a string and a pattern, find out if the string contains any permutation of the pattern.

If a pattern has n distinct characters, then it has n! permutations.
pattern: Sliding Window pattern
Similarities: Longest Substring with K distinct chars, but in this case
we want to find out whether or not there's a substring with matching distinct chars
as a given pattern.
Approach:

1. We will start by adding all characters from the pattern into our Hashmap to keep track
of the frequency of each character in the pattern.
2. We are asked to find out whether or not the string contains ANY permutation of pattern, meaning our goal is
to match all the characters from this HashMap with a sliding window or subarray  in the given string.
3. Iterate through the string, adding one character at a time into the sliding window or subarray.
4. If the character being added matches a character in the HashMap, decrement its frequency
in the map. If the character frequency becomes zero, we got a complete match of that character, so we
will increment `matched` which is a variable that keeps track of the total matches to the
characters in the Hashmap.
5. If at any time (meaning we check this FOR EVERY ITERATION), the no. of chars matched == to no. of distinct
chars in the pattern(total chars in the HashMap), we've found the required permutation.
6. If windowsize or subarray size(which is represented by the position of windowEnd) >= length of the 
pattern(pattern) - 1(-1 coz windowEnd starts from 0, so to get the actual size of subarray, we would 
have to subtract 1, from the length of whatever we are comapring it against), shrink the window to 
make it == the size of the pattern. At the same time, if the character going out was part of the 
pattern, this means AT THIS PARTICULAR POINT IN TIME you would've already accounted for it as HAVING 
MATCHED shown by its frequency in the Map being == 0, so, you wouldve to decrement the `matched` variable 
if its frequency is 0. And then put it back for matching.

Note: numbers 4, 5, and 6 are all individual parts of our algorithm
'''
def findPermutationInString(string2, pattern):
    '''Returns true if the string contains ANY permutation of
    the pattern, otherwise false.
    '''
    windowStart = 0 #keeps track of the start of the window or subarray
    charFreqMap = {} #keeps track of the frequency of each letter of the pattern
    matched = 0 #keeps track of the total count of characters of the permutation that have been matched 
    #adding characters into the HashMap
    for char in pattern:
        if char not in charFreqMap:
            charFreqMap[char] = 0
        charFreqMap[char] += 1
    #iterates through the whole string
    for windowEnd in range(len(string2)):
        rightChar = string2[windowEnd]
        #decrement its frequency if it matches a character of pattern
        if rightChar in charFreqMap:
            charFreqMap[rightChar] -= 1
            #if its frequency is 0, we have found a match for a character in our pattern; incement `matched`
            if charFreqMap[rightChar] == 0:
                matched += 1
        #return true if all chars of the pattern in the HashMap have been matched
        if matched == len(charFreqMap):
            return True
        #shrink the window size if its > length of the pattern
        if (((windowEnd - windowStart) + 1) >= len(pattern)):
            leftChar = string2[windowStart]
            #checking if the char going out is part of the Map
            if leftChar in charFreqMap:
                #if it has already been matched, decrement `matched`
                if charFreqMap[leftChar] == 0:
                    matched -= 1
                #put the character again in the HashMap for matching, by incrementing its frequency
                charFreqMap[leftChar] += 1
            windowStart += 1 #shrink the window
    return False

print(findPermutationInString("odicf", "dc"))
'''Time complexity : O(N + M), where N is the number of chars in the string
and M is the number of chars in the pattern.
Space Complexity: O(M), since in the worst case, the whole pattern can have distinct 
characters which will go into the HashMap.

Also we've learnt another way of calculating the size of the window:
windowEnd >= len(pattern) - 1, or ((windowEnd - windowStart) + 1) >= len(pattern) - 1
'''
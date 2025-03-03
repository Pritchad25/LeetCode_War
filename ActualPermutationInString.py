#!/usr/bin/python3
'''The Actual Anagram/Permutations of Pattern in the given string.
Given a string and a pattern, find all anagrams of the pattern in the 
given string. return a list of starting indices of the anagrams of 
the pattern in the given string.
Pattern: Sliding Window
Similarities: very similar to the Permutation of a given Pattern in a given string problem
Algorithms: at least 2 loops and 3 if statements

1. We will start by adding all the characters of the pattern into a HashMap,
to keep the frequency of each character of the pattern.
2. We are asked to return as a list, the starting indices of the anagrams of the pattern
in the given string, lets call this list `result`.
3. We will then iterate through the entire string and add 1 charcter at a time to our Sliding window
or subarray. If a character matches a character of the pattern, we will decrement its frequency
in the HashMap. If its frequency is 0, then it means we have found a match for a character of the pattern
and so we will increment the variable `matched` which keeps track of the total count of matches of the 
characters in the pattern. 
4. If the total count of matches of the characters in the pattern == the total of chars 
of the pattern (length of the Map), we append to the `result` list the current value of windowStart
5. If the windowsize or subarray size (which is determined or found by taking the current value of
windowEnd and adding 1) >= length of the pattern - 1(-1 coz windowEnd starts from 0, so to get 
the actual size of subarray, we would have to subtract 1, from the length of whatever 
we are comapring it against), then we have to shrink the window.
6. If the character going out is in the Map, and its frequency is 0(meaning AT THIS PARTICULAR POINT 
IN TIME you would've already accounted for it as HAVING MATCHED), decrement the matched variable(since
character is going out) otherwise if its frequency is not 0, put the character back to the Map by
incrementing its frequency.Then shrink the window.
''' 

def ActualPermutationInString(string3, pattern):
    '''Returns the list of starting indices of the Anagrams of
    the pattern in the string.'''
    windowStart = 0 #keeping track of the start of every window
    result = [] #stores the starting indices of all anagrams of the pattern in the string
    charFreqMap = {} #stores the frequency of all characters in the pattern
    matched = 0 #keep track of the total count of the matches to the characters in the HashMap
    #storing the frequency of each character of the pattern in the HashMap
    for char in pattern:
        if char not in charFreqMap:
            charFreqMap[char] = 0
        charFreqMap[char] += 1
    #iterate through the whole string
    for windowEnd in range(len(string3)):
        rightChar = string3[windowEnd]
        #decrement its frequency if its in the Map
        if rightChar in charFreqMap:
            charFreqMap[rightChar] -= 1
            #consider this char a match to the character of the Pattern
            #in the Hashmap if its frequency is 0
            if charFreqMap[rightChar] == 0:
                matched += 1
        #append the index if matched == len(Map)
        if matched == len(charFreqMap):
            result.append(windowStart)
        #shrink the size of the window if it is >= len(pattern)
        if ((windowEnd - windowStart) + 1 >= len(pattern)):
            leftChar = string3[windowStart]
            if leftChar in charFreqMap:
                if charFreqMap[leftChar] == 0:
                    matched -= 1
                #put the character back into the HashMap for matching
                charFreqMap[leftChar] += 1
            windowStart += 1 #shrink the window
    return result

print("Starting indices of the anagrams of the pattern in the given string:", ActualPermutationInString("abbcabc", "abc"))

'''Time Complexity: O(N + M), N being number of characters of string
and M being number of characters of pattern
Space Complexity : O(M), since in the worst case, the whole pattern can have distinct 
characters which will go into the HashMap.
'''
'''
1. We will keep a running count of every matching instance of a character.
If its frequency is 0 or more, then we have found a match for our character 
in the HashMap. The substring doesnt have to be an anagram of the pattern(if it was
supposed to be, then we wouldve only wanted a single match of a character of the pattern
in the HashMap, which single match is denoted by its frequency in the HashMap, being
== 0,(where if it is, then we have found a complete SINGLE match to the character of
the pattern in the HashMap)).Now because the required substring can have some additional 
characters and doesn't need to be a permutation of the pattern, we count every matching instance
to the character of the pattern that is in the HashMap, denoted by charFreqMap[rightChar] >= 0, 
by incrementing `matched` variable.decrement its frequency and if its frequency is still 0 or more,
 that means theres a single ormore of that character that matches to the one in the Hashmap, so 
 THEREFORE COUNT EVERY MATCHING OF THAT CHARACTER, by incrementing `the` matched variable.
2. Whenever we have matched all the characters (matched == len(pattern)), we will try to shrink 
the window from the beginning, keeping track of the smallest substring that has all the 
matching characters.
3. We will stop the shrinking process as soon as we remove a matched character from the sliding window. 
Meaning our shrinking process is in a loop, while(matched == len(patter))
-One thing to note here is that we could have redundant matching characters, e.g., we might have 
two 'a' in the sliding window when we only need one 'a'. In that case, when we encounter 
the first 'a', we will simply shrink the window without decrementing the matched count. We will 
decrement the matched count when the second 'a' goes out of the window, meaning, we'll decrement the
matched count only when a useful occurrence of a matched character is going out of the
window
-
-if (minLength > windowEnd - windowStart + 1), this window size represents the window that has 
all matching characters. That is, it is the length of that window that has all matching characters.
So in the if condition, we checking if the current value of minlength is > this length, if it is, we
then assign the length of this window or its size to minlength, THAT IS THE SMALLEST SUBARRAY
WITH ALL CHARACTERS OF THE PATTERN THAT ARE IN THE HASHMAP, ie, ALL MATCHING CHARACTERS.
-we then keep track of the start of that window, by storing windowStart to a variable called
subStrStart, ie, subStrStart = windowStart
-"useful occurrence" is when THE ONLY MATCH (charFreqMap[leftchar] == 0) for our character of the 
pattern that is in the HashMap is the one going out of the window or being shrunk out of the window, that is when 
we can decrement `matched` and then put that character back for matching by incrementing 
its frequency. Otherwise, if the letter's frequency is 
'''
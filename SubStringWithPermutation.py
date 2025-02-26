#!/usr/bin/python3
'''
Pattern: Sliding Window
Similarities: Permutation of A String
D.S: HashMap
Algos: at least 1 or 2 loops and if statement
Approach:
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
Meaning our shrinking process is in a loop, while(matched == len(pattern))
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

def SubStrWithPattern(string, pattern):
    windowStart = 0 #keeps track of the start of every window
    matched = 0 #tracks the total count of matches to the characters of the pattern that are in the HashMap
    subStrStart = 0 #keeps track of the start of a substring that has all characters of pattern
    minLength = len(string) + 1 # keeps track of the smallest substring all characters of pattern.
    #we assigned len(string) + 1 as the maximum of value
    charFreqMap = {} #keeps track of the frequency of each letter of the pattern
    #track the frequency of each letter of the pattern
    for char in pattern:
        if char not in charFreqMap:
            charFreqMap[char] = 0
        charFreqMap[char] += 1
    #iterate through all the characters of the string
    for windowEnd in range(len(string)):
        rightChar = string[windowEnd]
        #decrement its frequency if the char is in the HashMap
        if rightChar in charFreqMap:
            charFreqMap[rightChar] -= 1
            #Dont only count the Complete match to the character of the pattern in HashMap
            #but COUNT every matching instance, ie frequency >= 0
            if charFreqMap[rightChar] >= 0:
                matched += 1
        #shrink the window when have matched all the characters
        while (matched == len(pattern)):
            #keeping track of the length of the current window as the smallest so 
            #far with all characters of pattern before shrinking
            if (minLength > (windowEnd - windowStart) + 1):
                minLength = (windowEnd - windowStart) + 1
                #keep track of the start of that window
                subStrStart = windowStart
            leftChar = string[windowStart]
            #We will stop the shrinking process as soon as we remove a 
            #matched character from the sliding window
            if leftChar in charFreqMap:
                #note that we could have redundant matching characters
                #decrement `matched` only when a `useful occurence` of the character
                #that matches the one in the HashMap, is the one being taken out, put it back
                #for matching, then shrink the window, 
                #otherwise if its frequency is 1 or more, just put it back for matching and 
                # then shrink the window
                if charFreqMap[leftChar] == 0:
                    matched -= 1
                #put the character back for matching
                charFreqMap[leftChar] += 1
            windowStart += 1 #shrink the window
    if minLength > len(string):
        return "" # an empty string
    else:
        return string[subStrStart : minLength + 1]

print("The substring is ", SubStrWithPattern("abdabca", "abc"))
'''The algorithm works for these test cases, "aabdec", "abc" and "adcad", "abc" and not for 
the above case, please check it.
Time Complexity:  O(N + M) where 'N' and 'M' are the number of characters in the 
input string and the pattern respectively.
Space Complexity: O(M) since in the worst case, the whole pattern can have distinct 
characters which will go into the HashMap.
'''

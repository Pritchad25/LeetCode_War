#!/usr/bin/python3
'''No repeat substring.'''

def NoRepeatSubString(str1):
    '''returns the length of the longest substring with
    no repeating chars (Hard)
    pattern: Sliding Window
    similarities: Longest Substring with exactly K distinct chars, but our K is variable.
    Analysis Techniques:
    1. We will add one char at a time to our HashMap starting from the beginning, where our HashMap
    keeps track of the last index of each character, NOT the frequency of each char.
    2. These chars will constitute our Sliding Window and we are told to find the longest such window with NO
    REPEATING CHARS. We will keep track of the length((windowEnd - windowStart) + 1) of this window as the
    longest so far.
    3. After this, we will keep adding an element to our Sliding window ie slide the window ahead in a stepwise.
    4. In each step, we will try to shrink the window ahead, if the char exist in the HashMap. We will 
    shrink the window ahead according to the char's last index + 1(the +1 to cater for the character's actual position).
    When we shrink the window ahead, we will re-store the letter if it was already in the HashMap, and assign 
    its last index to it. If we dont shrink the window (meaning that letter is not repeating or is not in the HashMap)
    then we will simply store it in our HashMap, and assign its last index to it.
    5. Either we slide the window shrink or increment max-length, ie, those two things are mutually exclusive.
    '''

    windowStart = 0 #keeps track of the start of every window
    max_length = 0 #keeps track of the longest window with no repeating chars
    charFreqMap = {} #keeps track of the last index of each character
    #iterates through the entire string
    for windowEnd in range(len(str1)):
        leftChar = str1[windowEnd]
        #slide the window ahead if the char is in the hashmap, according to the last character position(index + 1)
        if leftChar in charFreqMap:
            windowStart = max(windowStart, charFreqMap[leftChar] + 1)
        #if char isnt there in HashMap, keep track of its last index. If char is there, slide the window
        #and re-store the letter into the HashMap.
        charFreqMap[leftChar] = windowEnd
        max_length = max(max_length, (windowEnd - windowStart) + 1)
    return max_length

str2 = "abccde"
print("Length of longest substring with NoRepeatChars is:", NoRepeatSubString(str2))

'''Time Complexity: O(N), where N is the number of chars in the string.
Space Complexity: O(1), The space complexity of the algorithm will be O(K), where K
is the number of distinct characters in the input string.
This also means K <= N, because in the worst case, the whole string might not 
have any repeating character so the entire string will be added to the HashMap.
Having said that, since we can expect a fixed set of characters in the input string 
(e.g., 26 for English letters), we can say that the algorithm runs in fixed space O(1);
in this case, we can use a fixed-size array instead of the HashMap.
'''
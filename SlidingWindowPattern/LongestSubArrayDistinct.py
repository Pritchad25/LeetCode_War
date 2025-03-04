#!/usr/bin/python3
'''MEDIUM.
pattern: Sliding Window
Similarity: Maximum Sum contiguous subarray
D.S: HashMap
Algorithm: at least 1 loop
Approach:
1.We will start by adding one character at a time to our HashMap, until theres
more than K distinct chars in the HashMap. If the letter is not in the HashMap,
we will add it with value 0; if it's already there, we increment its value.
2. These chars will constitute our Sliding Window(subarray). We are asked to find the
longest such window(subarray) with exactly K distinct chars. We will keep track of the length
of this window as the longest so far.
3. After this we will keep on adding one element to the window, ie, slide the window ahead, in a
stepwise fashion.
4. In each step we will also try to shrink the Sliding Window(subarray) from the beginning if the 
number of distinct charsin the HashMap > K. We will shrink the window UNTIL there's exactly K 
distinct chars in the window, as we intend to find the longest such window with exactly K distinct chars.
5. While shrinking the Sliding window, we will do 3 things:
    i)decrement the frequency of the letter  which is being removed from the window in the HashMap.
   ii)If the frequency becomes zero after decrementing, remove it from the HashMap.
   iii)slide the window ahead.
'''

def findMaxWindDistK(str1, k):
    '''finds the longest subarray with exactly K distinct chars.'''
    windowStart = 0 #keeps track of the start of every window
    max_length = 0 #keeps track of the longest window
    charFreqMap = {} #stores the number of times a particular char appears in the current window(freq of it)
    #iterates through entire string
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar not in charFreqMap:
            charFreqMap[rightChar] = 0
        charFreqMap[rightChar] += 1
        #shrink the window if number of distinct chars > k, until theres exactly k distinct chars in HashMap
        while(len(charFreqMap) > k):
            leftChar = str1[windowStart] #store the character
            charFreqMap[leftChar] -= 1 #shrink the window, which is done by decrementing its frequency
            if charFreqMap[leftChar] == 0: #if its frequency is 0, remove it from the map
                del charFreqMap[leftChar]
            windowStart += 1 #slide the window ahead
        max_length = max(max_length, (windowEnd - windowStart) + 1)
    return max_length

print("Longest Subarray with 3 distinct character is:", findMaxWindDistK("abbebi", 3))
'''Time complexity is O(N) linear time: where N is the number of characters in the input string. The outer for 
loop runs for all characters and the inner while loop processes each character only once, therefore 
the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).
Space Complexity is O(K), coz at the worst case, we will as we will be storing a 
maximum of K+1 characters in the HashMap.

'''
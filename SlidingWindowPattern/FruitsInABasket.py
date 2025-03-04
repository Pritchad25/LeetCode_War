#!/usr/bin/python3
'''Medium
pattern: Sliding Window
similarity: Longest Contiguous Subarray with K distinct chars. Why?
We are asked to return the maximum number of fruits in both the baskets
where each of the 2 baskets can have only one type of fruit and we are to put
maximum number of fruits in each basket and each basket can have 
only one type of fruit. In this case, our K == 2
D.S: HashMap
Approach:
1. We will add one char(fruit) starting from the beginning into the HashMap until
we have more than or (greater than) K distinct fruit types or fruit trees in the HashMap.
2. These chars will constitute our Sliding Window. We are asked to find the longest (maximum) such
window with exactly K=2 distinct chars(fruit types or fruit trees). We will keep track of 
the length((windowEnd - windowStart) + 1) of this window as the longest window so far.
3. After this, we will add one more char(fruit type or fruit tree) to the Sliding Window
ie slide the window ahead in a stepwise fashion
4. In each step, we will try to shrink the Sliding window, ie shrink the HashMap, if the number of distinct
chars(fruit types or fruit trees) is > K==2. We will shrink the window until there's exactly K==2 distinct chars(fruit
types or fruit trees) because we want to find the longest window with exactly K==2 distinct chars(fruit types or fruit trees).
5.While shrinking, we will also do 3 things:
    i) decrement its frequency from the hashMap
    ii) if its frequency is 0, delete the char(fruit type or fruit tree) altogether.
    iii) slide the window ahead.
'''

def MaxFruitsIn2Baskets(arr, K=2):
    '''finds the maximum number of fruits in both the baskets.'''
    windowStart = 0 #keeps track of the start of every window
    max_length = 0 #keeps track of the longest window with exactly K==2 fruit types or fruit trees
    fruitFreqMap = {} #the HashMap to keep the frequency of each fruit type or fruit tree
    #iterate through the whole array
    for windowEnd in range(len(arr)):
        rightFruit = arr[windowEnd]
        #check if the fruit exists in the Hash Map already
        if rightFruit not in fruitFreqMap:
            fruitFreqMap[rightFruit] = 0
        fruitFreqMap[rightFruit] += 1
        #shrinking and sliding if number of distinct fruits is > K
        while(len(fruitFreqMap) > K):
            leftFruit = arr[windowStart] #store the fruit at the beginning of the Sliding window
            fruitFreqMap[leftFruit] -= 1 #shrink the Sliding Window
            if fruitFreqMap[leftFruit] == 0: #if its frequency is 0, remove it from the HashMap
                del fruitFreqMap[leftFruit]
            windowStart += 1
        #we are either shrinking the Sliding window and sliding the window, or 
        #incrementing max_length to keep track of the length of the current window
        #longest so far with exactly 2 fruit types or fruit trees.These 2 events are 
        #Mutually Exclusive.
        max_length = max(max_length, (windowEnd - windowStart) + 1)
    return max_length

print("The maximum number of fruits in both baskets is:", MaxFruitsIn2Baskets(['A', 'B', 'C', 'B', 'B', 'C']))
'''Time Complexity is O(N): the outer loop runs for all fruit types, so at the worst
case, it is going to run O(N),where an N is the number of fruit types or fruit trees
in the array. The inner loop processes each char or fruit type once, so at the worst case, 
it will run O(N) times, so in essence, the algorithm runs O(N + N), at worst case, which is
asymptotically equivalent to O(N)

Space Complexity is O(1) Why? Because, first of all, space complexity can be 1 of 2 types:
fixed space complexity or variable space complexity. If its fixed, then the size of memory space
used to store data and variables is INDEPENDENT of the size input eg if the total size of the space 
used to store the data and variables is 4 bytes for say input of 100 elements, if input grows to 1000 elements,
the space for variables will remain 4 bytes, in other words, SAME SIZE OF MEMORY SPACE; so in the worst case
the algorithm will run on constant space and also CONSTANT because 4 is a constant. 
If its variable, the the size of memory space used to store data and variables is DEPENDENT on the size of
the input, eg if the total size of the space used to store the data and variables is 4 bytes 
for say input of 100 elements, if input grows to 200 elements, then it is HIGHLY LIKELY that the 
space for variables will also double to 8 bytes, meaning for variable space complexity, you have to analyse your
algorithm and see what exactly is being stored and how that process of storing is happening and deduce the complexity
from there.

So, its O(1), because, at the worst case, theres going to be a maximum of three types of 
fruits stored in the frequency map.So, at the worst case, our algorithm is going to run on constant space
meaning, at the worst case, the hashMap will take 3 bytes of space and will take that amount regardless
of how exponentially the size of input grows eg 100 fruit types, 3 bytes; 1000, 3 bytes njalo njalo
 '''
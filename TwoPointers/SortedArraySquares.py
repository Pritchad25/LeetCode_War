#!/usr/bin/python3
'''
Given a sorted array, create a new array containing squares of all the numbers of the 
input array in the sorted order.

Pattern: Two Pointers' Approach
Approach:
- This is a straightforward question. The only trick is that we can have negative 
numbers in the input array, which will make it a bit difficult to generate 
the output array with squares in sorted order.

1. Since the numbers at both ends can give us the largest square, we
could use two pointers starting at both ends of the input array, meaning
one pointer(left) will start at index 0, at the beginning of the array (ie left will 
be initialised to index 0) and the other(right), at end of array (ie, at index len(array) - 1)
-we will iterate throughout the entire array (from start to end of array), finding the square of 
each element, so our loop will run while left <= right, ie from start(index 0) to 
end (len(array) - 1).
2. At any step(ie AT ANY ITERATION), whichever pointer gives us the bigger square we add it 
to the result array and move to the next/previous number according to the pointer. 
-We add the biggersquare at highest index of our new array(coz we want the squares to 
be in sorted form as well); we keep track of the highest index where a square can be stored 
in our new array in the variable `highestSquareIndex` and its initialised to the actual 
highest index in our new array which is given by `len(array) - 1`. 
-When we add the bigger square at highest index of our new array, we will 
decrement `highestSquareIndex`, so the next big square gets in at the next highestSquareindex, 
after the previous.
-After adding the bigger square to our result array, we move to the next number(left++) (if the left pointer
gave us the bigger square) or to the previouss number(right--) (if the right pointer
gave us the bigger square).

“traverse” means moving through the input array from both the beginning (left end) and 
the end (right end).
'''

def SortedArraySquares(arr):
    '''Returns a new array of the squares of every element
    of the input array, in sorted form.
    '''
    left = 0 #pointer at the beginning of the array (index 0)
    n =  len(arr)
    right = len(arr) - 1 #pointer at the end of array (index (len(arr) - 1))
    highestSquareIndex = len(arr) - 1 #keeps track of the highest Index where 
    #the bigger Square should be put in our new array, and its initialised to the highest index
    #iterate through the array from start to end of array, finding the square of each element.
    squares = [0] * n #the new array of squares.
    while (left <= right):
        #whichever pointer gives us the bigger square, we add it to our array, at the highest index
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare: #meaning the left pointer gave us the bigger square
            squares[highestSquareIndex] = leftSquare
            highestSquareIndex -= 1 #so the next big square gets in at the next highestSquareindex,
            #after the previous
            left += 1 # move to the next number
        else: #meaning the right pointer gave us the bigger square
            squares[highestSquareIndex] = rightSquare
            highestSquareIndex -= 1
            right -= 1 #move to the previous number
    return squares

print("Squares in sorted order are:", SortedArraySquares([-2, -1, 0, 2, 3]))
print("Squares in sorted order are:", SortedArraySquares([-3, -1, 0, 1, 2]))

'''Time complexity: O(N)
Space complexity: O(N), as the space required to store the data and variables grows 
with the growth in input size and also coz this space will be used for the output array.
'''

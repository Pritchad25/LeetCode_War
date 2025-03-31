#!/usr/bin/python3
'''We are given an array containing positive and negative numbers. Suppose the array contains a 
number 'M' at a particular index. Now, if 'M' is positive we will move forward 'M' indices and 
if 'M' is negative move backwards 'M' indices. You should assume that the array is circular 
which means two things:
1. If, while moving forward, we reach the end of the array, we will jump to the first element to 
continue the movement.
2. If, while moving backward, we reach the beginning of the array, we will jump to the last 
element to continue the movement.

Write a method to determine if the array has a cycle. The cycle should have more than one 
element and should follow one direction which means the cycle should not contain both forward 
and backward movements.

Approach:
-This problem involves finding a cycle in the array and, as we know, the Fast & Slow pointer 
method is an efficient way to do that.
-We can start from each index of the array to find the cycle.If a number does not have a cycle 
we will move forward to the next element.There are a couple of additional things we need to take
care of:
1. As mentioned in the problem, the cycle should have more than one element. This means that when 
we move a pointer forward, if the pointer points to the same element after the move, we have a 
one-element cycle.Therefore, we can finish our cycle search for the current element(ie start
searching for a cycle in the next element).
2. The other requirement mentioned in the problem is that the cycle should not contain both 
forward and backward movements. We will handle this by remembering the direction of each element 
while searching for the cycle. If the number is positive, the direction will be forward and if 
the number is negative, the direction will be backward. So, whenever we move a pointer forward, 
if there is a change in the direction, we will finish our cycle search right there for the 
current element.
`for i in range(len(arr)):` ie from the start of the array(element at index 0) to the last 
element of array (element at index len(arr) - 1)
`isForward` is for remembering the direction of the current element while searching for the cycle
for the current element; If the number is positive, the direction will be forward so `isForward`'s
will be True and if the number is negative, the direction will be backward, so `isForward`'s 
value will be False
-`slow`&`fast` are our Fast & Slow Pointers for finding a cycle in our circular array.They are initialized
to the index of the current element, so that if the current element is positive, we move forward i indices
and if the current element is negative, we move backward i indices 
-`if slow or fast becomes '-1' this means we can't find cycle for this number` because it means
there has been a change in the direction and the requirement of our cycle is that it SHOULD NOT
contain both forward and backward movements; therefore we'll FINISH or END our cycle search right
there for this current element
-`isForward != direction` from findNextIndex function means there's been a change of direction (
same explanation as above) 
-findNextIndex function is the one that moves our slow and fast pointers forward(whether from
front to back (FORWARD) or back to front(BACKWARD))
-`if (nextIndex == currentIndex)`,where nextIndex is the variable that holds the new position
of our pointer AFTER MOVING IT FORWARD; if this variable holds the same value as 
currentIndex(the variable that holds the current position of our pointer), that means the pointer
points to the same element after the move which means we have 1 ELEMENT CYCLE; therefore we will
FINISH or END our cycle search right there for this current element by returning -1.
-`nextIndex = (currentIndex + arr[currentIndex] + arr.size()) % arr.size();` - in this formular,
`currentIndex` is the current position in the array, `arr[currentIndex]` is the value at the 
current index in the array which we add to the current index to determine the next inde, 
`+ arr.size()` here we add the size of the array to ensure that the result of the addition(
currentIndex + arr[currentIndex]) is non-negative, `% arr.size()` the modulus operator % is used
with the size of the array to ensure that the calculated index wraps around to the start of the 
array if it exceeds the size of the array. This creates a circular or cyclic effect. So, the 
formula calculates the next index in a circular array, taking into account the direction of 
movement (forward or backward) indicated by the value at the current index.
'''
class CircularArrayLoop:
    @staticmethod
    def loopExists(arr):
        for i in range(len(arr)):
            isForward = arr[i] >= 0  # if we are moving forward or not
            slow = i
            fast = i

            # if slow or fast becomes '-1' this means we can't find cycle for this number
            while True:
                slow = CircularArrayLoop.findNextIndex(arr, isForward, slow)  # move one step for slow pointer
                fast = CircularArrayLoop.findNextIndex(arr, isForward, fast)  # move one step for fast pointer
                if fast != -1:
                    fast = CircularArrayLoop.findNextIndex(arr, isForward, fast)  # move another step for fast pointer
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
        return False

    @staticmethod
    def findNextIndex(arr, isForward, currentIndex):
        direction = arr[currentIndex] >= 0
        if isForward != direction:
            return -1  # change in direction, return -1
        # wrap around for negative numbers
        nextIndex = (currentIndex + arr[currentIndex]) % len(arr)
        # one element cycle, return -1
        if nextIndex == currentIndex:
            nextIndex = -1
        return nextIndex

'''Time Complexity: O(N2), where N is the number of elements in the array. This complexity is 
due to the fact that we are iterating all elements of the array and trying to find a cycle for 
each element.
Space Complexity: O(1) runs in constant space

Alternative Approach:
In our algorithm, we don't keep a record of all the numbers that have been evaluated for cycles. 
We know that all such numbers will not produce a cycle for any other instance as well. If we can 
remember all the numbers that have been visited, our algorithm will improve to O(N) but it 
will also increase the space complexity to O(N)
'''

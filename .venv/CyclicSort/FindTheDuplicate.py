#!/usr/bin/env python3
'''Can we solve the above problem in O(1) space AND without modifying the input array

Approach
-While doing the cyclic sort, we realized that the array will have a cycle due to the duplicate 
number and that the start of the cycle will always point to the duplicate number.
-This means that we can use the fast & the slow pointer method to find the duplicate number or 
the start of the cycle similar to Start of LinkedList Cycle.
'''
class DuplicateNumber:
    '''Finds the Duplicate Number
    using the Fast & Slow Pointer
    Algorithm
    '''
    @staticmethod
    def findDuplicate(arr):
        '''Finds Duplicate without
        modifying the array

        Args:
            arr - the array of unsorted numbers
        '''
        slow = 0
        fast = 0
        while(True):
            slow = arr[slow] #enters the cycle first
            fast = arr[arr[fast]] #enters the cycle second & will keep moving twice as quick as 
            #slow
            if slow == fast: #ie, the two pointers have met; they are pointing to the same value.
                #meaning the LinkedList has a cycle.
                break
        # find the cycle length
        current = arr[slow]
        cycleLength = 0
        while(True):
            current = arr[current]
            cycleLength += 1
            if (current == arr[slow]):
                break
        
        return DuplicateNumber.findStart(arr, cycleLength)
    
    @staticmethod
    def findStart(arr, cycleLength):
        '''Finds the start of the cycle
        which is our duplicate number.

        Args:
            arr - the array of integers
            cycleLength - the length of the cycle
        '''
        pointer1 = arr[0]
        pointer2 = arr[0]
        # move the pointer2 ahead 'cycleLength' steps
        while (cycleLength > 0):
            pointer2 = arr[pointer2]
            cycleLength -= 1
        
        # increment both pointers until they meet at the
        #start of the cycle
        while (pointer1 != pointer2):
            pointer1 = arr[pointer1]
            pointer2 = arr[pointer2]
        return pointer1

# Testing
if __name__ == "__main__":
    print("Duplicate Number is: ", DuplicateNumber.findDuplicate([1, 4, 4, 3, 2]))
    print("\nDuplicate Number is: ", DuplicateNumber.findDuplicate([2, 1, 3, 3, 5, 4]))
    print("\nDuplicate Number is: ", DuplicateNumber.findDuplicate([2, 4, 1, 4, 4]))

'''Time Complexity: O(N) &
Space Complexity: O(1)
'''

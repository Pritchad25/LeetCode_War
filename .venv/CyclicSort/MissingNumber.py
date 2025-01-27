#!/usr/bin/env python3
'''We are given an array containing 'n' distinct numbers taken from the range 0 to 'n'. Since the
array has only 'n' numbers out of the total 'n + 1' numbers, find the missing number.

Question Clarification:
-`range 0 to 'n'` - this line means that the array will ALWAYS have digits from the range 0 up to
n
-Say n is 5, so these distinct numbers in the array was taken from the range 0 to 5.Since the 
array has only 5 numbers out of the total pool of '6' numbers, find the missing number.

Pattern: this problem follows the Cyclic Sort pattern
Similarities: Cyclic Sort problem

Approach:
1.Since the input array contains UNIQUE or DISTINCT numbers from the range 0 to 'n', we can use a 
similar strategy as discussed in Cyclic Sort to place the numbers on their correct index.
-Once we have every number in its correct place or correct position, we can iterate the array to 
find the index which does not have the correct number, and that index will be our missing number.

-However, there are two differences with the Cyclic Sort problem:
1. In this problem, the numbers are ranged from '0' to 'n', compared to '1' to 'n' in the Cyclic 
Sort problem. This will make 2 changes in our algorithm:
    (i)In this problem, each number should be equal to its CORRECT INDEX, compared to `index + 1`
    in the Cyclic Sort. Therefore => nums[i] == nums[nums[i]] .Each number in Cyclic Sort, was 
    equal to its index plus 1 (index + 1), when the Cyclic Sort algorithm finished running. So, 
    in this problem, when the MissingNumber algorithm finishes running(meaning when we have found
    the missing number), each number in the array should be == to its index, ie, 
    nums[i] == nums[nums[i]]
    (ii)Since the array will have 'n' numbers, this means array indices will range from 0 to'n-1'
    Therefore, we will ignore the number 'n' as we can't place it in the array, so => 
    nums[i] < nums.length
2. Say we are at index i. If we swap the number at index i to place it at its correct index, we 
can still have the wrong number at index i. This was true in Cyclic Sort too. It didn't cause any 
problems in Cyclic Sort as over there, we made sure to place one number at its correct place in 
each step, but that wouldn't be enough in this problem as we have one extra number due to the 
larger range. Therefore, we will not move to the next number after the swap until we have a 
correct number at the index i.
-`nums[i] == nums[nums[i]]` - this `nums[nums[i]]` IS the correct index of the number that we are
currently standing on `nums[i]`. So, if the number that we are currently standing on `nums[i]` IS
NOT EQUAL TO ITS CORRECT INDEX (`nums[nums[i]]`), THEN this means this number `nums[i]` is at the
WRONG PLACE or at the WRONG POSITION and there currently is a WRONG NUMBER at this 
number's(`nums[i]`) correct index, THEREFORE, we have to swap the 2 numbers so that, this number
that we're currently standing on `nums[i]` goes to its CORRECT INDEX, and this index should be ==
to this number `nums[i]`.
-When the while loop exits, we will be done with the Cyclic Sort.
-`swap(nums, i, nums[i])` -  Say we are at index 1. If we swap the number at index 1(say, its 0)
to place it(the number 0) at its correct index(index 0, where, say, there's the number 4 
currently), we can still have the wrong number at index 1(the number 4). This was true in Cyclic 
Sort too. It didn't cause any problems in Cyclic Sort as over there, we made sure to place one 
number at its correct place in each step; but that wouldn't be enough in this problem as we have
one extra number due to the larger range. 
Therefore, we will not move to the next number after the swap until we have a correct number at 
the index 1(where currently there's 4 and 4 shouldnt be there).
-` if (nums[i] != i)` - once we have put each number on its correct index or correct position in 
the first while loop, we then iterate the array AGAIN starting from the first element to the last,
and check each number if its equal to the index that it is currently positioned at.If any number
that we currently standing on IS NOT EQUAL to the index on which it is currently positioned, then
that index IS OUR MISSING NUMBER, therefore we return it.
-`return nums.size()` - if each and every number starting from the first element to the last IS
EQUAL to its index or the index that its positioned at, then that means the missing number is
DIRECTLY PROPORTIONAL (in other words) EQUAL to the length of the array because the n numbers in
the array which are ALL EQUAL to their indices, where taken from the range 0 to n, so the missing
number is n which is EQUIVALENT to the length of the array, therefore we return the length of the
array as the missing number.
'''
class MissingNumber:
    '''Defines static methods for
    finding the missing numbers
    '''
    @staticmethod
    def findMissingNumber(nums):
        '''Finds the missing number in an
        array of n integers
        
        Args:
            nums: array of n integers taken from range 0 to n
        '''
        i = 0
        while (i < len(nums)):
            # Place each number at its correct index
            if (nums[i] < len(nums) and nums[i] != nums[nums[i]]):
                MissingNumber.swap(nums, i, nums[i])
            else:
                i += 1 # Move on to the next number
        
        # find the first number missing from its index, that will be our required number
        for i in range(len(nums)):
            if (nums[i] != i):
                return i
        
        return len(nums)
    
    @staticmethod
    def swap(arr, i, j):
        '''Swaps elements of an array
        '''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [4, 0, 3, 1]
    print("Missing Number: ", MissingNumber.findMissingNumber(v1))
    v1 = [8, 3, 5, 2, 4, 6, 0, 1]
    print("\nMissing Number: ", MissingNumber.findMissingNumber(v1))

'''Time Complexity: O(N) where N is the number of elements in the array. Although we are not 
incrementing the index i when swapping the numbers, this will result in more than 'N' iterations 
of the loop, but in the worst-case scenario, the while loop will swap a total of 'n-1' numbers 
and once a number is at its correct index, we will move on to the next number by incrementing i
In the end, we iterate the input array again to find the first number missing from its index, so
overall,our algorithm will take O(N) + O(N - 1) + O(N) which is asymptotically equivalent to O(N)
'''
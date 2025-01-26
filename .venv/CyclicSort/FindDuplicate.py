#!/usr/bin/env python3
'''We are given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. The 
array has only 1 duplicate but it can be repeated multiple times. Find that duplicate number 
without using any extra space. You are, however, allowed to modify the input array.

Question Clarification:
-`'n+1' numbers taken from the range 1 to 'n'` - say n=5, our array contains 6 numbers
-`1 duplicate but it can be repeated multiple times` - meaning if a number in our array is a
duplicate, it can be repeated 1 time or 2 times or 3 times in the array, ie MULTIPLE TIMES but
the size of the array will never change, ie it will always be `n + 1`.

Pattern: Cyclic Sort pattern
Similarities: Missing Number
Approach:
-Following a similar approach, we will try to place each number on its correct index.
-Since there is only one duplicate(ie, only 1 number that is a duplicate), if, while swapping 2
numbers, both the numbers being swapped are the same(EQUAL), we have found our duplicate!

-`if (nums[i] != i + 1)` - Before we CYCLICALLY SORT the array, for each number, we check if 
the number that we're currently standing in IS NOT EQUAL to its CURRENT INDEX + 1; if this is the
case, then this number (`nums[i]`) is not the correct number for this index that we're currently
on, so we will look for this number (`nums[i]`)'s CORRECT INDEX, in the next if statement and 
swap the 2 numbers when we find it (which is us CYCLICALLY SORTING the array);(else part) if its 
not the case (meaning nums[i] == i + 1), that means this number (`nums[i]`)'s CURRENT INDEX is 
its CORRECT INDEX, so we will simply move on to the next number
-Note that we say each number will be == to its CORRECT INDEX + 1 because our range starts from 1
to n, so when every number is in its CORRECT INDEX after the array is CYCLICALLY SORTED, each
number will be == to its CORRECT INDEX + 1.This "trick" here is only associated with problems
where the range of numbers in the array is 1 to n.
-`if (nums[i] != nums[nums[i] - 1])` - that is, is the number that we're currently standing on NOT
EQUAL to the number that is standing at this number(`nums[i]`)'s CORRECT INDEX. If that is the
case, then we will swap these 2 numbers. `i` is the index of the number that we're currently
standing on, ie, it is the index of the number `nums[i]` and `nums[i] - 1` is this 
number(`nums[i]`)'s CORRECT INDEX. The `swap` method will take these 2 indices and swap the 
numbers at those positions or indices, thus placing `nums[i]` at its CORRECT INDEX. (else part)
if that is not the case (meaning nums[i] == nums[nums[i] - 1]), this means the number that we're 
currently standing in `nums[i]` IS EQUAL to the number that is standing at this 
number(`nums[i]`)'s CORRECT INDEX, thus we would have found the duplicate, so we return the number
that we are currently standing in `nums[i]` as our duplicate. We only need 2 numbers 
that are equal to find a duplicate.
'''
class FindDuplicate:
    '''Finds a Duplicate'''
    @staticmethod
    def findNumber(nums):
        '''Finds the Duplicate Number in
        an array of unsorted numbers.

        Args:
            nums: the unsorted array of numbers containing a 
            duplicate number
        '''
        i = 0
        while(i < len(nums)):
            if (nums[i] != i + 1):
                if (nums[i] != nums[nums[i] -1]):
                    FindDuplicate.swap(nums, i, nums[i] - 1)
                else: # we have the duplicate number
                    return nums[i]
            else:
                i += 1 # move on to the next number
        return -1 # there's no duplicate
    
    @staticmethod
    def swap(arr, i, j):
        '''Swaps 2 integers of an array
        IN-PLACE
        '''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [1, 4, 4, 3, 2]
    print("The Duplicate is: ", FindDuplicate.findNumber(v1))

    v1 = [2, 1, 3, 3, 5, 4]
    print("\nThe Duplicate is: ", FindDuplicate.findNumber(v1))

    v1 = [2, 4, 1, 4, 4]
    print("\nThe Duplicate is: ", FindDuplicate.findNumber(v1))

'''Time Complexity: O(N), where is the total Number
of elements in the array
Space Complexity: O(1): The algorithm runs in constant space, but 
modifies the input array.
'''
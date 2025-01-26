#!/usr/bin/env python3
'''We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array
originally contained all the numbers from 1 to 'n', but due to a data error, one of the numbers 
got duplicated which also resulted in one number going missing. Find both these numbers.

Question Clarification:
-`Find both these numbers.` - find the number that got duplicated and the number that went 
missing.

Pattern: Cyclic Sort
Similarities: Find All Duplicate

Approach
-Following a similar approach, we will place each number at its correct index. 
-Once we are done with the CYCLIC SORT, we will iterate through the array to find the number that 
is not at the CORRECT INDEX. Since only 1 number got CORRUPTED(DUPLICATED), the number at the 
wrong index is the duplicated number and the index itself represents the missing number.
-`if (nums[i] != i + 1` - that is, if the number that we currently standing in `nums[i]` IS NOT
EQUAL to its CORRECT INDEX, then this number `nums[i]` is at the WRONG INDEX and is thus the
CORRUPTED or DUPLICATED NUMBER and this number `nums[i]`'s WRONG INDEX is the MISSING NUMBER.
'''
class FindCorruptNums:
    '''The Missing Number & the
    Corrupt Number.
    '''
    @staticmethod
    def findNumbers(nums):
        '''Finds the Duplicate Number &
        the Missing Number
        
        Args:
            nums - the unsorted array of 
            integers
        '''
        i = 0
        while ( i < len(nums)):
            if (nums[i] != nums[nums[i] - 1]):
                FindCorruptNums.swap(nums, i, nums[i] - 1)
            else:
                i += 1 # move on to the next number
        
        for i in range(len(nums)):
            if (nums[i] != i + 1):
                return [nums[i], i + 1]
    
        return [-1, -1] # no duplicate and no missing number
    
    @staticmethod
    def swap(arr, i, j):
        '''Swaps 2 integers IN-PLACE.
        '''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [3, 1, 2, 5, 2]
    nums = FindCorruptNums.findNumbers(v1)
    print(f"{nums[0]}, {nums[1]}")

    v1 = [3, 1, 2, 3, 6, 4]
    nums = FindCorruptNums.findNumbers(v1)
    print(f"\n{nums[0]}, {nums[1]}")

'''Time Complexity: O(N)
Space Complexity: O(1).The algorithm runs in constant space
'''
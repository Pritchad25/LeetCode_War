#!/usr/bin/env python3
'''We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'.The array 
has some duplicates, find all the duplicate numbers without using any extra space.

Pattern: Cyclic Sort
Similarities: Find Duplicate

Approach
-Following a similar approach, we will place each number at its correct index. 
-After that, we will iterate through the array to find all numbers that are not at the correct 
indices. All these numbers are duplicates.
-`if (nums[i] != i + 1):` ie, if the element that we're currently standing on `nums[i]` IS NOT
EQUAL to its CORRECT INDEX + 1, then this number `nums[i]` is a duplicate number, so add this 
number or this element in the list `duplicateNumbers`
'''
class FindAllDuplicate:
    '''All Duplicate Numbers'''
    @staticmethod
    def findNumbers(nums):
        '''Finds all Duplicate Numbers
        in an unsorted array of integers.

        Args:
            nums - the unsorted array of integers
        '''
        i = 0
        while (i < len(nums)):
            if (nums[i] != nums[nums[i] - 1]):
                FindAllDuplicate.swap(nums, i, nums[i] - 1)
            else:
                i += 1 #move on to the next number
        
        duplicateNumbers = []
        for i in range(len(nums)):
            if (nums[i] != i + 1): 
                duplicateNumbers.append(nums[i])
        
        return duplicateNumbers
    
    @staticmethod
    def swap(arr, i, j):
        '''Swaps 2 integers IN-PLACE
        '''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [3, 4, 4, 5, 5]
    duplicates = FindAllDuplicate.findNumbers(v1)
    print("Duplicates are: ")
    for num in duplicates:
        print(num, end=" ")
    
    v1 = [5, 4, 7, 2, 3, 5, 3]
    duplicates = FindAllDuplicate.findNumbers(v1)
    print("\nDuplicates are: ")
    for num in duplicates:
        print(num, end=" ") 
'''Time Complexity: The time complexity of the above algorithm is O(N).
Space Complexity: Ignoring the space required for storing the duplicates, the algorithm runs in
constant space in O(1).
'''
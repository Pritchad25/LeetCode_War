#!/usr/bin/env python3
'''We are given an unsorted array containing numbers taken from the range 1 to n.The array can 
have duplicates, which means some numbers will be missing. Find all those missing numbers.

Pattern: This problem follows the Cyclic Sort pattern
Similarities: Missing Number

Approach
-this problem is similar to Missing Number with 1 difference: In this problem, there can be many 
duplicates & range == length of array(eg if n=5, theres 5 numbers in the array; there can be 
duplicates but the total number of elements in the array should be 5 and these numbers were taken
from the range 1 to 5, which is a total pool of 5 numbers, so range == length of array) whereas 
in 'Missing Number' there were no duplicates and the range was > length of the array(eg if n=5, 
theres 5 UNIQUE numbers in the array but these numbers were taken from the range 0 to 5 which is 
a total pool of 6 numbers, so range was > the length of array).
However, we will follow a similar approach though as discussed in Missing Numbers to place the 
numbers on their correct indices. Once we are done with the cyclic sort we will iterate the array 
to find all indices that are missing the correct numbers.

-`if (nums[i] != nums[nums[i] - 1])` - that is, is the number that we're currently standing on NOT
EQUAL to the number that is standing at this number(`nums[i]`)'s CORRECT INDEX. If that is the
case, then we will swap these 2 numbers. `i` is the index of the number that we're currently
standing on, ie, it is the index of the number `nums[i]` and `nums[i] - 1` is this 
number(`nums[i]`)'s CORRECT INDEX. The `swap` method will take these 2 indices and swap the 
numbers at those positions or indices, thus placing `nums[i]` at its CORRECT INDEX.
-Note that we say each number will be == to its CORRECT INDEX + 1 because our range starts from 1
to n, so when every number is in its CORRECT INDEX after the array is CYCLICALLY SORTED, each
number will be == to its CORRECT INDEX + 1.This "trick" here is only associated with problems
where the range of numbers in the array is 1 to n.
- When the while loop exits, we will be done with the Cyclic Sort. Each number that is in the 
array will be in its CORRECT index. Next, we will iterate the array to find all indices that are 
missing the correct numbers. What we do know though is that, when this second loop finishes each
number should be == its index + 1
-`nums[i] != i + 1` - In this array that is NOW CYCLICALLY SORTED, for each number, we check if 
the number that we're currently standing in IS NOT EQUAL to its CORRECT INDEX + 1; if this is the
case, then this number (`nums[i]`) is not the correct number for this index that we're currently
on, so THIS NUMBER(`nums[i]`)'S INDEX + 1 is A MISSING NUMBER, so we add it to our list of 
MISSING NUMBERS
'''
class AllMissingNumbers:
    '''Class for find all missing numbers'''
    @staticmethod
    def findNumbers(nums):
        '''Finds all missing numbers in an
        unsorted array of integers
        '''
        i = 0
        while (i < len(nums)):
            if (nums[i] != nums[nums[i] - 1]):
                AllMissingNumbers.swap(nums, i, nums[i] - 1)
            else:
                i += 1
        
        missingNumbers = []
        for i in range(len(nums)):
            if (nums[i] != i + 1):
                missingNumbers.append(i + 1)
        return missingNumbers
    
    @staticmethod
    def swap(arr, i , j):
        '''Swaps 2 integers IN PLACE'''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [2, 3, 1, 8, 2, 3, 5, 1]
    missing = AllMissingNumbers.findNumbers(v1)
    print("Missing Numbers: ")
    for num in missing:
        print(num, end=" ")
    
    v1 = [2, 4, 1, 2]
    missing = AllMissingNumbers.findNumbers(v1)
    print("\nMissing Numbers: ")
    for num in missing:
        print(num, end=" ")
    
    v1 = [2, 3, 2, 1]
    missing = AllMissingNumbers.findNumbers(v1)
    print("\nMissing Numbers: ")
    for num in missing:
        print(num, end=" ")

'''Time Complexity: O(N)
Space Complexity: O(1)
Ignoring the space required for the output array, the algorithm runs in 
constant space.
'''
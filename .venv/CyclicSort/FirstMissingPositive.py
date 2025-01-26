#!/usr/bin/env python3
'''Given an unsorted array containing numbers, find the smallest missing positive number in it.

Pattern: Cyclic Sort
Similarities: Missing Number, with 1 BIG difference: In this problem, the numbers are not 
bound by any range so we can have ANY number in the input array.

Approach:
-we will follow a similar approach though as discussed in `Missing Number` to place the numbers 
on their correct indices and ignore all numbers that are OUT OF THE RANGE of the array, that is 
IGNORE ALL negative numbers and all numbers >= the length of the array. 
-Once we are done with the cyclic sort, we will iterate the array and the 
first index that does not have the correct number will be the smallest missing positive number.

nums: [2, 1, 3, 6, 5], k =2
After the cyclic sort our array will look like:
nums: [1, 2, 3, 6, 5] (we are ignoring all numbers >= length of the array.Here, to IGNORE, means
that as we move along the array CYCLICALLY SORTING each number, when we encounter a number that
fulfills the above condition, we will simply skip that number, ie MOVE ON TO the next number and 
leave it at the position or at index we found it in. When the array has been CYCLICALLY SORTED,
each number will be in its CORRECT INDEX; we will then iterate it once more, now checking if each
number is == to its CORRECT INDEX + 1; a number that we encounter that is NOT EQUAL to its CORRECT
INDEX + 1 IS IN THE WRONG INDEX and this number's WRONG INDEX is the MISSING NUMBER)

-`if (nums[i] > 0 && nums[i] <= nums.size() && nums[i] != nums[nums[i] - 1])` - that is, is the 
number that we're currently standing on `nums[i]` > 0 and <= length of the array AND is the 
number that we're currently standing on `nums[i]` NOT EQUAL to the number that is standing at 
this number(`nums[i]`)'s CORRECT INDEX. If that is the case, then we will swap these 2 numbers.
`i` is the index of the number that we're currently standing on, ie, it is the index of the 
number `nums[i]` and `nums[i] - 1` is this number(`nums[i]`)'s CORRECT INDEX. The `swap` method 
will take these 2 indices and swap the numbers at those positions or indices, thus placing 
`nums[i]` at its CORRECT INDEX.

-`if (nums[i] != i + 1): return i + 1`, that is, is the number that we're currently standing on
NOT EQUAL to its CORRECT INDEX + 1, then this number  `nums[i]` is on the WRONG INDEX, therefore
this number (`nums[i]`)'s WRONG INDEX (`i + 1`) is the smallest missing positive number so we
RETURN IT.
-`return len(nums) + 1` - We ignored all numbers >= length of the array, so if there's no
smallest missing positive number currently in our array, the NEXT SMALLEST MISSING POSITIVE 
NUMBER is the one next to the length of the array in terms of size, so its denoted by 
`len(nums) + 1`, hence we return this.
'''
class FirstMissingPositive:
    '''Smallest Missing Positive Number
    '''
    staticmethod
    def findNumber(nums):
        '''Finds the smallest missing
        positive number
        Args:
            nums - unsorted array of numbers
        '''
        i = 0
        while (i < len(nums)):
            if (nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]):
                FirstMissingPositive.swap(nums, i, nums[i] - 1)
            else:
                i += 1
        
        for i in range(len(nums)):
            if(nums[i] != i + 1):
                return i + 1 # this index is the smallest missing positive number
        
        return len(nums) + 1 #Otherwise, return the NEXT SMALLEST MISSING POSITIVE NUMBER
    
    @staticmethod
    def swap(arr, i, j):
        '''Swaps 2 integers IN-PLACE
        '''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [-3, 1, 5, 4, 2]
    print(FirstMissingPositive.findNumber(v1))

    v1 = [3, -2, 0, 1, 2]
    print(FirstMissingPositive.findNumber(v1))

    v1 = [3, 2, 5, 1]
    print(FirstMissingPositive.findNumber(v1)) 

'''Time Complexity: O(N)
Space Complexity: O(1)
'''
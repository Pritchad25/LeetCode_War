#!/usr/bin/env python3
'''Given an unsorted array containing numbers and a number 'k', find the first 'k' missing 
positive numbers in the array.

Pattern: Cyclic Sort
Similarities: FirstMissingPositive, The only difference is that, in this problem, we need to find
the first 'k' missing numbers compared to only the first missing number.

Approach
-We will follow a similar approach as discussed in FirstMissingPositive to place the numbers on 
their correct indices and ignore all numbers that are out of the range of the array(ie ignore 
all the negative numbers and numbers >= length of the array)
-Once we are done with the cyclic sort we will iterate through the array to find indices that do 
not have the correct numbers.

-If we are not able to find 'k' missing numbers from the array, we need to add additional numbers
to the output array.To find these additional numbers we will use the length of the array.
For example, if the length of the array is 4, the next missing numbers will be 4, 5, 6 and so on.
-One tricky aspect is that any of these additional numbers could be part of the array. Remember, 
while sorting, we ignored all numbers that are >= the length of the array. So all indices that 
have the missing numbers could possibly have these additional numbers.
-To handle this, we must keep track of all numbers from those indices that have missing numbers
ie keep track of all numbers that are standing in wrong indices. 
Let's understand this with an example:

nums: [2, 1, 3, 6, 5], k=2
After the cyclic sort our array will look like:
nums: [1, 2, 3, 6, 5] (we are ignoring all numbers >= length of the array.Here, to IGNORE, means
that as we move along the array CYCLICALLY SORTING each number, when we encounter a number that
fulfills the above condition, we will simply skip that number, ie MOVE ON TO the next number and 
leave it at the position or at index we found it in. When the array has been CYCLICALLY SORTED,
each number will be in its CORRECT INDEX; we will then iterate it once more, now checking if each
number is == to its CORRECT INDEX + 1; a number that we encounter that is NOT EQUAL to its CORRECT
INDEX + 1 IS IN THE WRONG INDEX and this number's WRONG INDEX is the MISSING NUMBER)

From the sorted array we can see that the first missing number is 4(as we have 6 in the 4th index)
but to find the second missing number we need to remember that the array does contain 6.Hence, the
next missing number is 7.

-`while (i < len(nums) and len(missingNumbers) < k):` - this loop will exit when we
reach the end of the array or when we have found all k missing numbers.
-`extraNumbers.add(nums[i])` - keep track of this number that we're currently standing on 
`nums[i]` by storing it in `extraNumbers` because this number `nums[i]` is standing in the WRONG 
INDEX.
-`i = 1 while(len(missingNumbers) < k):` - the loop starts at 1 going forward(while 
len(missingNumbers) < k) because some of our missing numbers are > the length of the array.
Remember, while sorting, we ignored all numbers that are >= the length of the array.So, when the
first for loop above exits and we have not found ALL our required missing numbers, the NEXT 
missing numbers will be > the length of the array.So, we say i=1 so that we check for the
missing number(s) starting from the first number that is > length of the array, going forward,ie
checking each and every one of those numbers to see if its the missing number to fill up the
required number of missing positive numbers we need to find. Hence, the following line:
-candidateNumber = i + len(nums), that is, every number that is a CANDIDATE to be a missing 
number NOW or at this present stage in our algorithm, is greater than the length of the array. So
we will check if each number we're currently standing on (that is > the length of the array) is 
present in our array, and if it is, we move on to check the next immediate number after the one 
we're currently standing on, which is also > the length of the array, by incrementing
i by 1 (i += 1)
-missing_numbers = []
-extra_numbers = set(), its a set
'''
class FirstKMissingPositive:
    '''First K Missing Positive
    Numbers.
    '''
    @staticmethod
    def findNumbers(nums, k):
        '''Finds the first k missing
        positive numbers.
        
        Args:
            nums - an unsorted array of positive numbers.
            k - the number of missing positive
            numbers to find
        '''
        i = 0
        while ( i < len(nums)):
            if ((nums[i] > 0 and nums[i] <= len(nums)) and (nums[i] != nums[nums[i] - 1])):
                FirstKMissingPositive.swap(nums, i, nums[i] - 1)
            else:
                i += 1 #move on to the next number
        
        missingNumbers = []
        extraNumbers = set() # a set
        i = 0
        while (i < len(nums) and len(missingNumbers) < k):
            if (nums[i] != i + 1):
                missingNumbers.append(i + 1) #add this index as the missing Number to our list
                extraNumbers.add(nums[i]) #add this current number which is standing in the wrong index
            i += 1
        
        # add the remaining missing numbers
        i = 1
        while(len(missingNumbers) < k):
            candidateNumber = i + len(nums) #every candidate number is > len of array
            #check if this candidate number exists in the array.If it does, ignore this step
            if candidateNumber not in extraNumbers:
                missingNumbers.append(candidateNumber)
            i += 1 # move on to the next candidate number
        
        return missingNumbers
    
    @staticmethod
    def swap(arr, i, j):
        '''Swaps 2 integers IN-PLACE
        '''
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

# Testing
if __name__ == "__main__":
    v1 = [3, -1, 4, 5, 5]
    missingNumbers = FirstKMissingPositive.findNumbers(v1, 3)
    print("Missing numbers: ")
    for num in missingNumbers:
        print(num, end=" ")
    
    v1 = [2, 3, 4]
    missingNumbers = FirstKMissingPositive.findNumbers(v1, 3)
    print("\nMissing numbers: ")
    for num in missingNumbers:
        print(num, end=" ")

    v1 = [-2, -3, 4]
    missingNumbers = FirstKMissingPositive.findNumbers(v1, 2)
    print("\nMissing numbers: ")
    for num in missingNumbers:
        print(num, end=" ")

'''Time Complexity: O(N + k), as the last 2 while loops will run for
O(N) and O(k) times respectively.
Space Complexity: O(k), the algorithms needs O(k) to store the `extraNumbers`
'''
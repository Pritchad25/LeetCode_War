#!/usr/bin/env python3
'''We are given an array containing 'n' objects. Each object, when created, was assigned a unique 
number from 1 to n based on their creation sequence. This means that the object with sequence 
number 3 was created just before the object with sequence number 4.

Write a function to sort the objects IN-PLACE on their CREATION SEQUENCE NUMBER in O(n) and
and without any extra space.

For simplicity, let's assume we are passed an integer array containing only the sequence numbers,
though each number is actually an object.

Question Clarification:
-Say n is 5, so we're given an array containing 5 objects. Each object, when created,was assigned 
a unique number from 1 to 5 based on their CREATION SEQUENCE. This means that the object with 
sequence number 3 was created just before the object with sequence number 4. So, if we have, for
example, the object with sequence number 3 being followed by an object with sequence number 1,then
there's an anomaly there that needs to be solved because BY RIGHT, these objects should be in 
ASCENDING ORDER of their CREATION SEQUENCE numbers. So, we solve this anomaly by doing what the
question is asking which is to `write a function that sorts the objects IN-PLACE on their 
CREATION SEQUENCE NUMBER...`
-`an integer array containing only the sequence numbers` - these objects should be IN ORDER based 
on their CREATION SEQUENCE numbers

Approach
-As we know, the input array contains numbers in the range of 1 to 'n'. We can use this fact to 
devise an efficient way to sort the numbers. Since all numbers are UNIQUE, we can try placing 
each number at its correct place, i.e., placing '1' at index '0', placing '2' at index 1', and so
on.
-we will iterate the array one number at a time and if the current number that we're standing on
is not at the correct index, we will swap it with the number that is at its correct index. This 
way we will go through ALL NUMBERS, 1 by 1 ONE TIME & place them in their correct indices, hence,
sorting the whole array. 

-`while (i < nums.size())` - we want to take ONE NUMBER AT A TIME, check if this number is at its 
correct index and IF ITS NOT, swap this number with the number that is at its(this number) 
correct index and we want to do this FOR EVERY NUMBER, starting from the number at the beginning 
of the array(i==0) UNTIL we reach the number at the end(i==nums.size() - 1), therefore to
automate this, we will use a `while` loop with the condition `i < nums.size()`, hence the
above while structure.If you look closely, this `i==0 i==nums.size() - 1`, CLEARLY tells you that
we want our loop to run AS LONG AS i < nums.size(), because both of i's values are truly and
genuinely LESS THAN nums.size()
-`i++` - we will be moving on to the next number in the array, because at the current position of
i, we have already placed the correct number at its correct index, therefore we can move on to
the next number, by incrementing i.
-`j = nums[i] - 1` - here, we are storing the CORRECT INDEX of the number which we are currently
standing `nums[i]`,meaning we are storing the correct position where `nums[i]` should be at. 

-`if (nums[i] != nums[j])`-After storing the CORRECT POSITION of the number that we're currently 
standing on `nums[i]`, we then check, `Is the number which we are currently standing on `nums[i]`
NOT EQUAL to the number that is at `nums[i]`'s CORRECT POSITION;if this is true, then we have to
SWAP those 2 numbers, to put the number which we are currently standing on `nums[i]` AT ITS 
CORRECT POSITION. After swapping, WE DO NOT MOVE TO THE NEXT NUMBER because the number that is 
NOW at index `i` IS NOT AT ITS CORRECT INDEX or CORRECT POSITION. Therefore, we have to store its
correct index at `j` & then move on to this if statement. When this if statement's condition 
becomes false, it means the number which we are currently standing on `nums[i]` IS EQUAL TO the 
number that is at `nums[i]`'s CORRECT POSITION meaning this number (nums[i]) is at its CORRECT 
POSITION, so we have move to the next number `nums[i + 1]`, hence the else part `i++`
'''

class CyclicSort:
    '''Defines a sorting method and
    a swapping method
    '''
    @staticmethod
    def sort(nums):
        '''sorts the creation sequence numbers
        of objects in Ascending order
        '''
        i = 0
        while (i < len(nums)):
            j = nums[i] - 1 #storing the correct position of nums[i]
            #swapping numbers
            if (nums[i] != nums[j]):
                CyclicSort.swap(nums, i, j)
            else:
                i += 1 # move on to the next number
    
    @staticmethod
    def swap(nums, i, j):
        '''swaps 2 integers of an array'''
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

# Testing
if __name__ == "__main__":
    arr = [3, 1, 5, 4, 2]
    CyclicSort.sort(arr)
    for num in arr:
        print(num, end=" ")
    print("\n")

    arr = [2, 6, 4, 3, 1, 5]
    CyclicSort.sort(arr)
    for num in arr:
        print(num, end=" ")
    print("\n")

    arr = [1, 5, 6, 4, 3, 2]
    CyclicSort.sort(arr)
    for num in arr:
        print(num, end=" ")

'''Time Complexity: O(N), where N is the number of elements in the array. Although we are not 
incrementing the index i when swapping the numbers, this will result in more than 'N' iterations 
of the loop, but in the worst-case scenario, the while loop will swap a total of 'n-1' numbers 
and once a number is at its correct index, we will move on to the next number by incrementing i
So overall, our algorithm will take O(N) + O(N - 1), which is asymptotically equivalent to O(N)
Space Complexity: O(1)
'''


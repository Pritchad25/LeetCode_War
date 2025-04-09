#!/usr/bin/python3
'''Remove Duplicates (easy)
Given an array of sorted numbers, remove all duplicates IN-PLACE from it. You should 
not use any extra space; after removing the duplicates in-place return the new 
length of the array.

Pattern: Two Pointers Approach
Approach: 
-In this problem, we need to remove the duplicates in-place such that 
the resultant length of the array remains sorted. In order for us to remove
duplicates IN-PLACE, we need to have a way of holding the index where there is
a duplicate number or element. The way is this: the if condition becomes false 
ONLY when we have found a duplicate number, and when it does, nextNonDuplicate
will remain the same for the next iteration, meaning its holding the index where 
there is a duplicate number or element which we want to remove IN_PLACE, meaning
we will hold this index until we encounter a non duplicate number and this number 
will then replace the number in the index that is being held by nextNonDuplicate, that 
is how we remove IN_PLACE. When we encounter duplicates and remove them IN-PLACE, we are
actually shifting THE NON DUPLICATES to the left.
-Since the array is sorted, one way to do this is to shift the elements left 
whenever we encounter duplicates, meaning we will keep one pointer for iterating 
the array (i is the pointer in the below algorithm, starting at 1 since IT IS A GIVEN
THAT the first element of array is a non duplicate) and one pointer for placing the 
next non-duplicate number (and this pointer is nextNonDuplicate, it is the one that places 
the next non duplicate number or element next to another non duplicate via this line:
`arr[nextNonDuplicate] = arr[i]`)
-So our algorithm will be to iterate the array and whenever we see a non-duplicate 
number we move it next to the last non-duplicate number we've seen.
-below `arr[nextNonDuplicate - 1]` represents the previous element  and `arr[i]` represents 
the current element we are standing in.`
'''

def removeDuplicates(arr):
    '''removes all duplicates inplace and returns the new
    length of the array.
    '''
    nextNonDuplicate = 1 #tracks the index of the NEXT NON DUPLICATE number or element, 
    #since 1st element is a non duplicate
    #iterates the whole array, starting at i = 1 since its a given that the first element of
    #of the array is a non duplicate. from i = 1 to size of array excluded"
    for i in range(1, len(arr)):
        if arr[nextNonDuplicate - 1] != arr[i]:
            arr[nextNonDuplicate] = arr[i] #assign this non duplicate number next to the 
            #previous non duplicate one and/or remove a duplicate IN-PLACE.
            nextNonDuplicate += 1 #increment to the index of the nextNonDuplicate number
    return nextNonDuplicate

def removeKeyDuplicates(arr, key):
    '''returns the length of new array, after removing all instances 
    or occurrences of key from the array of unsorted numbers.

    We can follow a two-pointer approach and shift numbers left 
    upon encountering the 'k'
    '''
    nextElement = 0;  #index of the next element which is not 'key'
    #iterates the whole array, starting at index 0 of the array since its NOT a given that 
    #the first element of array is NOT a duplicate of key, so we have to check every element
    #starting from the beginning.
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i] #assign this non duplicate number next to the 
            #previous non duplicate one and/or remove a duplicate IN-PLACE.
            nextElement += 1 #increment to the index of the nextElement which is not 'key'
    return nextElement 

    

print("Length of the new array without duplicates is:", removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
print("Length of the new array without duplicates is:", removeDuplicates([2, 2, 2, 11]))
print("Length of the new array without the duplicates of the key is:", removeKeyDuplicates([3, 2, 3, 6, 3, 10, 9, 3], 3))
print("Length of the new array without the duplicates of the key is:", removeKeyDuplicates([2, 11, 2, 2, 1], 2))

'''Time Complexity of both: O(N)
Space Complexity of both: O(1)
'''

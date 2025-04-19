#!/usr/bin/python3
'''Medium.
Given an array `arr` of unsorted numbers and a target sum, write a function that returns the
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j & k are 
three different indices.
Rephrased: Given an array of unsorted numbers and a target sum, write a function that returns
the count of all UNIQUE triplets whose sum < target sum.
Pattern: Two Pointers
Similarities: Triple Sum To Zero
Aprroach 
- shares similarities with TripleSumToZero, The only difference is that, in this problem, we need 
to find the triplets whose sum is less than the given target.
- To meet the condition i != j != k, we need to make sure that each number is used EXACTLY once.

1. Following a similar approach, first, we can sort the array and then iterate through 
it, taking one number at a time. 
2. Let's say during our iteration we are at number X, so we need to find 'Y' and 'Z'
such that X + Y + Z < Target Number. 
-At this stage, our problem translates into finding a pair (Y & Z) whose sum is < Target - X, ie
Y + Z < Target - X
3. We can use a similar approach as discussed in TripletSumToZero
'''

def search_triplets(arr, target):
    '''Finds all unique triplets in an array of 
    unsorted numbers whose sum < targetSum.
    Firstly, finds the start of all triplets in this
    array, and executes another function to find the 
    pair Y & Z such that, Y + Z < Target - X  (where X is 
    the number that we are currently standing in in the function 
    searchTriplets) and returns the total count of all 
    triplets (subarrays of size 3) whose sum < target
    '''
    arr.sort() #sorting the array first
    count = 0 #keeps track of the total count of triplets whose sum < target
    for j in range(len(arr) - 2):#len(arr) - 2 is the formular that finds the total number of
    #triplets(subarrays with 3 elements) that exist in an array. So this loop is going to run
    #for the total number of triplets that exist in the array.
        count += searchPair(arr, target - arr[j], j + 1) #`target - arr[j]` is our TargetSum.We 
        #want to find two elements(Y and Z) such that Y + Z < target - arr[j], `j + 1` is 
        #where our left pointer will start, its +1 coz we want to start finding the pair 
        #whose sum is < target - arr[j](current number) from the first element after the 
        #current element we standing in in the function searchTriplets, going forward
    return count

def searchPair(arr, targetSum, left):
    '''This helper function helps us to find the pair Y & Z 
    such that Y + Z < target - arr[j] and increments `count`
    if we have found any valid triplets.
    '''
    count = 0
    right = len(arr) - 1 #end pointer initialized with the index of the last element of array
    #iterating from point where left is standing to the end of array
    while (left < right):
        if (arr[left] + arr[right] < targetSum): # if we've found the triplet
            #since arr[right] >= arr[left](because we sorted the array), therefore, we can 
            #replace arr[right] by any number between left and right to get 
            #a sum less than the target sum
            count += right - left
            left += 1
        else:
            right -= 1 #we need a pair with a smaller sum
    return count
print(search_triplets([-1, 0, 2, 3], 3))
'''Time Complexity: O(N2), Sorting the array will take O(NlogN)
The searchPair() function will take O(N), searchTriplets will take
O(NlogN + N2) which is asymptotically equivalent to O(N2)
Space Complexity: Ignoring the space required for the output array, the 
space complexity of the above algorithm will be O(N) which is required 
for sorting if we are not using an in-place sorting algorithm.
'''

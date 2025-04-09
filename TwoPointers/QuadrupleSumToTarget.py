#!/usr/bin/python3
'''Problem Challenge 1
Given an array of unsorted numbers and a target number, find all 
unique quadruplets in it, whose sum is equal to the target number.

Pattern: Two Pointer's Approach
Similarities: TripletSumToZero

Approach:
-we need to find (and return) quadruplets(a subarray of 4 elements)
with a target sum == target number
-we need to find all the unique triplets meaning the subarrays of 4 elements
have to be different from each other.
1. First, we will sort the array and then iterate through it taking 
one number at a time.
2. Let's say during our iteration we are at number 'W' and 'X', we need to find 'Y' and 'Z' 
such that W+X+Y+Z==target number.
3. So in essence, our problem translates into finding a pair (Y,Z) such that
W+X+Y+Z == target number. We will do this in a different function, lets call 
it, `searchPairs`.In this function, 
-At every step (ie for each iteration), we will see if the numbers pointed by the
two pointers add up to the target sum(-X). So, our loop will only run if the start
point is always < end pointer
'''
def searchQuadruplets(arr, target):
    '''Finds all unique triplets in an array of unsorted numbers that 
    add up to target number.Firstly, finds the start of all quadtruplets 
    in this array, takes care of duplicates and executes another
    function to find the triplet X, Y & Z such that X+Y+Z = Target - W,
    (where W is the number that we are currently standing in in
    the function searchQuadruplets) and return all quadruplets(subarrays of
    size 4) whose sum == target
    '''
    arr.sort()#sorting the array first. All duplicates are now next to each other, therefore
    #they're easier to skip
    quadruplets = []# where the triplets are going to be stored
    for i in range(len(arr) - 3):#len(arr) - 3 is the formular that finds the total number of
        #quadruplets(subarrays with 4 elements) that exist in an array. So this loop 
        #is going to run for the total number of quadruplets that exist in the array
        if i > 0 and arr[i] == arr[i - 1]:#skip same element to avoid duplicate quadruplets. 
            #It is a given that the first element is not a duplicate ie i = 0 is not a 
            #duplicate;but from  i == 1 going upwards, There's no guarantee so we have 
            #to check and remove.
            continue
        j = i + 1 #our second element which is next to i(hence the `+1`)
        for j in range(len(arr) - 2):#len(arr) - 2 is the formular that finds the total number of
            #triplets(subarray with 3 elements) that exist in an array. So this loop is going
            #to run for the total number of triplets that exist in the array
            if j > i + 1 and arr[j] == arr[j - 1]:#skip same element to avoid duplicate triplets.
                #It is a given that the first element from where we start to search pairs is 
                #not a duplicate ie j = i + 1 is not a duplicate; but from j == i + 1 + 1 going
                #upwards, there's  no guarantee so we have to check and remove
                continue
            searchPairs(arr, target, i, j, quadruplets)#`target` is our targetsum. we want to
            #find two elements(Y and Z) such that i + j + Y + Z == target
    return quadruplets

def searchPairs(arr, targetSum, first, second, quadruplets):
    '''Searches for the pair (Y, Z) such that 
    first + second + Y + Z == targetSum and assigns that pair,
    first and second as a quadruplet into our 2D array called
    quadruplets.
    '''
    left = second + 1 #where our left pointer is going to start its +1 coz we want to start 
    #finding the pair (Y, Z) such that first + second + Y + Z == targetSum from the first 
    #element after the one we are currently standing in via pointer `j` going forward.
    right = len(arr) - 1 #end pointer initialized with the index of the last element of array
    #iterating from point where left is standing to the end of array
    while (left < right):
        sum = arr[first] + arr[second] + arr[left] + arr[right]#sum of any given pair and i & j
        if sum == targetSum: #found the quadruplet
            result = []
            result.append(arr[first])
            result.append(arr[second])
            result.append(arr[left])
            result.append(arr[right])
            quadruplets.append(result)
            left += 1
            right -= 1
            #skipping same element to avoid duplicate triplets or triplets that have the same
            #elements
            while(left < right and arr[left] == arr[left - 1]):#move to the next number until u find
                left += 1#one that is not a duplicate of the previous and loop condition becomes false
            while(left < right and arr[right] == arr[right + 1]):#move to the next number from the back
                right -= 1# or to the previous number until u find one that is not a duplicate of the
                #previous and loop condition becomes false
        elif sum < targetSum:
            left += 1# we need a bigger sum, so remove element where left is standing on
            #as it didn't give us a biggerSum, that is closer to target(targetSum)
        else:#meaning targetSum < currentSum, we need a smaller sum so we remove element where right is
            right -= 1#standing on as it didnt give us a smaller sum that is closer to target(targetSum)

print(searchQuadruplets([2, 0, -1, 1, -2, 2], 2))
'''Time Complexity: Sorting the array will take O(NlogN). Overall, 
searchQuadruplets will take O(NlogN + N3) which is asympotically 
equivalent to O(N3).
Space Complexity: The space complexity of the above algorithm will be
O(N) which is required for sorting.
'''

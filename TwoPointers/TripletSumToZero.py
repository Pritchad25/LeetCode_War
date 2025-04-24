#!/usr/bin/python3
'''
Given an array of unsorted numbers, find all unique triplets in it 
that add up to zero.(Medium)

Pattern: Two Pointers Approach
Similarities: Pair with Target Sum, a couple of differences are that the 
input array is not sorted and instead of a pair whose sum is == to a certain 
targetSum, we need to find (and return) triplets(a subarray of 3 elements) with a target 
sum of zero(targetSum == 0).
Another difference  is that we need to find all the unique triplets, ie all
the subarrays of size 3 whose sum == 0 have to be different from each other
instead of the indices of the pair whose sum is == 0
Approach:
1. To follow a similar approach, first, we will sort the array and then 
iterate through it taking one number at a time.
2. Let's say during our iteration we are at number 'X', so we need to 
find 'Y' and 'Z' such that X+Y+Z==0
3. So in essence, our problem translates into finding a pair whose 
sum is equal to, '-X' (as from the above equation Y + Z == -X). We will do 
this in a different function, lets call it, `searchPair`. In this function,
-At every step (ie for each iteration), we will see if the numbers pointed by the
two pointers add up to the target sum(-X). So, our loop will only run if the start
point is always < end pointer. 
-If they do, we will add this pair and -targetSum as a triplet into our matrix 
`triplets`, then move to the next number on both pointers, then we take care of 
duplicates according to step 4.
-If they do not, we will do one of two things:
    (i) If the sum of the two numbers pointed by the two pointers is > target 
    sum, this means that we need a pair with a smaller sum meaning we remove the 
    current value where right is pointing as it hasnt given a smaller sum. 
    So, to try more pairs, we can decrement the end-pointer, ie, right-- moving 
    to the next number from the back or moving to the previous number.
    (ii) If the sum of the two numbers pointed by the two pointers is < the 
    target sum, this means that we need a pair with a larger sum meaning we
    remove the current value where left is pointing as it hasnt given a bigger sum.
    So, to try more pairs, we can increment the start-pointer, ie left++, moving 
    to the next number
4. Since we need to find all the unique triplets we have to
skip any duplicate number.The duplicate number is found if the
element we currently standing in (arr[i]) == arr[i - 1](the previous
element). In the first function, we skip the duplicate number(arr[i])
by moving to the next iteration (continue). In the 2nd function, 
we skip the duplicate number(arr[i]), according to which pointer
is standing at this duplicate number, ie, if left is standing in the
duplicate number(arr[left](current)being == arr[left - 1)(previous), we move 
to the next number(left ++) and if right is standing in the duplicate number(arr[right]
being == arr[right + 1]) move to the next number from the back (right--)
or move to the previous number).Since we will be sorting the array, all the 
duplicate numbers will be next to each other and are easier to skip.

'''
def searchTriplets(arr):
    '''
    Finds all unique triplets in an array 
    of unsorted numbers that add up to zero.
    Firstly, finds the start of all triplets in this
    array, takes care of duplicates and executes another
    function to find the pair Y & Z such that, Y + Z = -X,
    (where X is the number that we are currently standing in in
    the function searchTriplets) and return all triplets(subarrays 
    of size 3) whose sum == 0
    '''
    arr.sort() #sorting the array first. All duplicates are now next to each other, therefore
    #they're easier to skip
    triplets = [] # where the triplets are going to be stored
    for i in range(len(arr) - 2): #len(arr) - 2 is the formular that finds the total number of
    #triplets(subarrays with 3 elements) that exist in an array. So this loop is going to run
    #for the total number of triplets that exist in the array.
        if i > 0 and arr[i] == arr[i - 1]: #skip same element to avoid duplicate triplets. It is
            #a given that the first element is not a duplicate ie i = 0 is not a duplicate; but
            #from  i == 1 going upwards, There's no guarantee so we have to check and remove.
            continue
        searchPair(arr, -arr[i], i + 1, triplets) # `-arr[i]` is our TargetSum, we want to
        #find two elements(Y and Z) such that Y + Z == -X(TargetSum), `i + 1` is where our left
        #pointer will start, its +1 coz we want to start finding the pair whose sum is == to -TargetSum
        #from the first element after the current element we standing in going forward.
    return triplets

def searchPair(arr, targetSum, left, triplets):
    '''Searches for the Pair whose sum == targetSum
    and assigns that pair and -targetSum as a triplet
    to our 2D array called triplets.
    '''
    right = len(arr) - 1 #end pointer initialized with the index of the last element of array
    #iterating from point where left is standing to the end of array
    while (left < right):
        currentSum = arr[left] + arr[right] #sum of any given pair of elements
        if currentSum == targetSum: # we have found our pair, so lets add them to matrix 
            #with -targetSum
            result = []
            result.append(-targetSum)
            result.append(arr[left])
            result.append(arr[right])
            triplets.append(result)
            left += 1
            right -= 1
            #skipping same element to avoid duplicate triplets or triplets that have the same 
            #elements
            while(left < right and arr[left] == arr[left - 1]): #move to the next number until u find
                left += 1 #one that is not a duplicate of the previous and loop condition becomes false
            while (left < right and arr[right] == arr[right + 1]): #move to the next number from the back
                right -= 1# or to the previous number until u find one that is not a duplicate of the 
                #previous and loop condition becomes false
        elif targetSum > currentSum:
            left += 1 # we need a bigger sum, so remove element where left is standing on 
            #as it didn't give us a biggerSum, that is closer to target(targetSum)
        else: #meaning targetSum < currentSum, we need a smaller sum so we remove element where right is
            right -= 1 #standing on as it didnt give us a smaller sum that is closer to target(targetSum)

print(searchTriplets([-5, 2, -1, -2, 3]))

'''Time Complexity: O(N2): Sorting the array will take O(N * logN)
As we are calling the searchPair for every number in the input array, 
this means that overall searchTriplets() will take O(N * log N + N2)
which is asymptotically equivalent to O(N2) 

Space Complexity: Ignoring the space required for the output array, the 
space complexity of the above algorithm will be O(N) which is
required for sorting.
'''

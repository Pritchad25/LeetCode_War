#!/usr/bin/python3
'''Given an array of unsorted numbers and a target number, find a 
triplet in the array whose sum is as close to the target number 
as possible, return the sum of the triplet. If there are more 
than one such triplet whose sum is as close to the target number
as possible, return the sum of the triplet with the 
smallest sum.

Pattern: Two Pointers Approach
Similarities: TripleSumToZero
Approach:

-we need to find a triplet or triplets(a subarray of 3 elements) with a
sum that is as close to being == to the target Number and return this sum. 
If there are more than one such triplet, return the sum of the triplet 
with the smallest sum.

Approach:
1. To follow a similar approach, first, we will sort the array and then 
iterate through it taking one number at a time.
2. 2. Let's say during our iteration we are at number 'X', so we need to 
find 'Y' and 'Z' such that X+Y+Z==target Number or is as close to being == target Number
3. At every step(ie for each iteration), we will save the difference between the sum of
triplet and the target number(which is our target Sum) (lets call 
this difference targetDiff) so that in the end, we can return the triplet with the 
closest sum


targetDiff keeps track of the number that the sum of the current triplet 
that we are standing in DIFFERS from the targetsum which is our Target Number.eg if our
targetDiff == 2, then the sum of the current triplet that we are standing 
in DIFFERS from the targetsum(TargetNumber) by 2 and in the step, 
`if abs(target_diff) < abs(smallest_difference):` we check if targetDiff is the
smallest so far and keep track of it, if it is. We use `abs` to cater for cases where
the targetDiff is negative.
'''
def search_triplet(arr, target_sum):
    arr.sort()
    smallest_difference = float('inf') #assigning positive infinity to the variable which is the
    #the largest value you can assign to a variale
    for i in range(len(arr) - 2):#len(arr) - 2 is the formular that finds the total number of
    #triplets(subarrays with 3 elements) that exist in an array. So this loop is going to run
    #for the total number of triplets that exist in the array.
        left, right = i + 1, len(arr) - 1 #assigning values via tuple assignment
        while left < right:
            # comparing the sum of three numbers to the 'target_sum' can cause overflow
            # so, we will try to find a target difference
            target_diff = target_sum - arr[i] - arr[left] - arr[right] # the above is equal to
            #target_diff = target_sum - (arr[i] + arr[left] + arr[right]) where the right part
            #of equal sign is the sum of triplet that we are currently standing in, ie
            #target_diff = target_sum (our TargetNumber)- Sum of our Triplet
            if target_diff == 0:
                # we've found a triplet with an exact sum
                return target_sum - target_diff  # return the sum of that Triplet

            if abs(target_diff) < abs(smallest_difference): 
                smallest_difference = target_diff  # save the closest difference

            if target_diff > 0: #targetDiff will be > 0 if targetSum > tripletsum
                left += 1  # we need a triplet with a bigger sum
            else: #meaning  targetDiff < 0 , targetDiff will be < 0 if targetSum < tripletsum
                right -= 1  # we need a triplet with a smaller sum
    return target_sum - smallest_difference #kufana lokuthi TripletSum = targetSum - smallest_diff,
#so in essence we are returning a triplet sum as the sum that is closest to the target number.
print(search_triplet([1, 0, 1, 1], 100))
'''Time Complexity: O(N2);Sorting the array will take O(NlogN), Overally searchTriplet
will take O(NlogN + N2) which is asymptotically equivalent to O(N2)
Space Complexity: The space complexity of the above algorithm will be O(N) which
will be required for sorting
'''

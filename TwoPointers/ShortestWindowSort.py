#!/usr/bin/python3
'''Problem Challenge 3
Given an array, find the length of the smallest subarray in it 
which when sorted, will sort the whole array.

1. From the beginning and end of the array, find the first elements that are out of the 
sorting order. The two elements will be our candidate subarray.
2. Find the maximum and minimum of this subarray.
3. Extend the subarray from beginning to include any number which is bigger than the minimum 
of the subarray.
4. Similarly, extend the subarray from the end to include any number which is smaller than 
the maximum of the subarray.

`while(low < arr.size() - 1 && arr[low] <= arr[low + 1])`
-We always look at the worst case at times when constructing loop conditions and in this case, 
the worst case is that we dont know where the first number out of sorting order occurs so 
we assume that in the worst case this loop is going to run until the end and find nothing. 

-Because, we want to find this number starting from the beginning of the array, we have to 
use the variable low. The loop will run from low==0 (index 0, which is index of first element 
of array) to low==index of last element - 1 because we are comparing 2 elements FOR EACH 
ITERATION to find the element WHICH IS OUT OF SORTING ORDER, starting this "search" from 
the beginning hence the use of the variable 'low'.

-we use low == index of last element - 1 in (low < arr.size() - 1), becoz we want to ensure that 
we dont EXCEED the maximum index of an array when comparing the two element at each iteration 
eg arr[6] <= arr[7] when the array ends at index 6 hence why we use the condition 
low < arr.size() - 1.

-in (arr[low] <= arr[low + 1]) we use <= because we taking care of the case where there are 
duplicate numbers in our array.
-`low++` (low is going to hold the index of the number that is bigger than its next neighbor, ie the
number that makes its next neighbor OUT OF SORTING ORDER!)

-the if condition means that the loop ran until yaze yafika ekucineni kwe Array and didnt
find a number that was out of sorting order which actualy means that THE ARRAY IS ALREADY 
sorted. The loop reaching the end of the array means low == index of last element 
of array. The length of the smallest subarray is 0.

-`while (high > 0 and arr[high] >= arr[high - 1])`we dont know where the first number out of 
sorting order occurs so we assume that in the worst case this loop is going to run until 
the end and find nothing. Because, we want to find this number starting from the end of the
array, we have to use the variable `high`.The loop will run from high == index of last element
of array to high == index of first element + 1, to ensure that we dont get to an index lower
than the lowest index of the array(which we know is 0), hence the condition `high > 0`.
-in arr[high] >= arr[high - 1], we use >= because we taking care of the case where there are
duplicate numbers in our array.
-`high--` (high is going to hold the index of the number that is smaller than its next neighbor
from the back, ie the number that makes its next neighbor OUT OF SORTING ORDER)

-`for (int k = low; k <= high; k++)` starting from the index of the bigger number that makes 
its next neighbor OUT OF SORTING ORDER(low) up to(<=) the index of smaller number that makes
its next neighbor from backwards(from the back) OUT OF SORTING ORDER(high), find the min and
max number of the subarray.Because we dont know where these two numbers(min & max) are in our
subarray, we use a loop that will go from low(explained above) to high because ALL WE know is
that these 2 numbers are within our subarray which starts from low to high.

-`while (low > 0 && arr[low - 1] > subarrayMin)` we dont know how many numbers there are that 
are bigger than the minimum of the subarray that we may want to use to extend our subarray 
by including them,which numbers are at the beginning of our array. All we know is that these 
numbers are standing in indices that are less than the one `low` is holding, in fact, theyre 
starting at indices low - 1 going downward. So we starting from where low is currently standing
(which is 1, ie index 1, ie low==1 IN THIS eg).Each time we decrement `low`, we are extending 
our subarray from the beginning by including a number that is bigger than the minimum of 
the subarray. We CONTINUOUSLY(ITERATION) check and extend until we reach beginning of 
array (low == 0) in which case loop exits.So in order to extend from the beginning, low has 
to be > 0 ie low has to be holding an index of number that makes its next neighbor OUT OF 
SORTING ORDER

-`while (high < arr.size() - 1 and arr[high + 1] < subarrayMax)`.we dont know how many numbers 
there are that are less than the maximum of the subarray that we may want to use to extend our 
subarray by including them,which numbers are at the end of our array. All we know is that these
numbers are standing in indices that are greater than the one `high` is holding, in fact, theyre
starting at indices high + 1 going upward. So we starting from where low is currently standing
(which high == 4,ie index4 in this eg) to index of last element of array - 1(< arr.size() - 1)
because we want to ensure that we dont EXCEED the maximum index of our array when comparing the
numbers with our `subarrayMax`. We CONTINUOUSLY(ITERATION) check and extend until we reach 
index of last element of array - 1(< arr.size() - 1) in which case loop exits.

-`return high - low + 1` return the length of this subarray. its `+1` coz we dealing with indices
where we start counting from 0, so to get a true representation of the length we say +1.
'''
def ShortestWindowSort(arr):
    '''Finds the length of the smallest subarray
    in the array which when sorted sorts the
    whole array
    '''
    low = 0 #keeps track of the index of first element of array
    high = len(arr) - 1 #keeps track of the index last element of array
    #Below we find the first number out of sorting order from the beginning
    while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
        low += 1
    
    if (low == len(arr) - 1): #if the array is sorted
        return 0
    
    #find the first number out of sorting order from the end
    while (high > 0 and arr[high] >= arr[high - 1]):
        high -= 1
    
    #find the maximum and minimum of the subarray
    subarrayMax = float('-inf') #keeps track of the maximum number of the subarray
    subarrayMin = float('inf') #keeps track of the minimum number of the subarray
    for k in range(low, high + 1):#for (int k = low; k <= high; k++)
        subarrayMax = max(subarrayMax, arr[k])
        subarrayMin = min(subarrayMin, arr[k])
    
    #extend the subarray to include any number which is bigger than the minimum of the subarray
    while (low > 0 and arr[low - 1] > subarrayMin):
        low -= 1
    
    #extend the subarray to include any number which is smaller than the maximum of the subarray
    while (high < len(arr) - 1 and arr[high + 1] < subarrayMax):
        high += 1
    
    return (high - low) + 1 #return the length of this subarray

print(ShortestWindowSort([3, 2, 1]))
'''Time Complexity: O(N)
Space Complexity: O(1)'''

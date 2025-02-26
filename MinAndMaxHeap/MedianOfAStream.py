#!/usr/bin/env python3
import heapq
'''Design a class to calculate the median of a number stream. The class 
should have the following 2 methods:
    1) insertNum(int num): stores the number in the class
    2) findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be 
the average of the middle 2 numbers.

Example 1
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2 ((3 + 1) / 2)
4. insertNum(5)
5. findMedian() -> output: 3 (Because the order of the numbers are 1,3,5; 
the middle number is 3.)
6. insertNum(4) 
7. findMedian() -> output: 3.5 (Because the order of the numbers are 1,3,4,
5; & because we have an even total of the numbers, we find the median by
finding the average of the middle numbers 3 & 4, ie (3 + 4) / 2 == 3.5)

-So, when n is even(where n is the total count of the numbers)
Median = sum of the middle numbers / the count of the middles numbers we 
just added.
-Otherwise (meaning n is odd)
Median = is the middle number

Problem Clarification
-As we know, the median is the middle value in an ordered integer list. 
-So a brute force solution could be to maintain a sorted list of all numbers
inserted in the class so that we can efficiently return the median whenever
required. Inserting a number in a sorted list will take O(N) time if there 
are N numbers in the list.
-This insertion will be similar to the `Insertion Sort`
-Can we do better than this? Can we utilize the fact that we don't need the
fully sorted list - we are only interested in finding the middle element?

-Assume 'x' is the median of a list. This means that half of the numbers in
the list will be <= 'x' and half will be >= 'x'. This leads us to an 
approach where we can divide the list into 2 halves: one half to store all 
the smaller numbers (let's call it `smallNumList`) and one half to store 
the larger numbers (let's call it `largeNumList`).The median of all the 
numbers will either be the largest number in the `smallNumList` or the 
smallest number in the `largeNumList`. If the total count of elements is 
even, the median will be the average of these 2 numbers.

-The best data structure that comes to mind to find the smallest or largest 
number among a list of numbers is a Heap. 

Let's see how we can use a heap to find a better algorithm.
1. We can store the first half of numbers (i.e `smallNumList`) in a Max Heap.
We should use a Max Heap as we are interested in knowing the largest number
in the 1st half.
2. We can store the second half of numbers (i.e `largeNumList`) in a Min Heap,
as we are interested in knowing the smallest number in the second half.
3. Inserting a number in a heap will take O(logN) which is better than the 
brute force approach.
4. At any time, the median of the current list of numbers can be calculated
from the top elements of the 2 heaps.

Example 1 above Step by Step explanation
1. `insertNum(3)`- We can insert a number in the Max Heap (i.e. first half) 
if the number is < the top (largest) number of the heap.
-After every insertion, we will balance the number of elements in both heaps, 
so that they have an equal number of elements.
-If the count of numbers is odd, let's decide to have more numbers in 
Max-heap than the Min Heap.
Max-heap      Min-Heap
   3           None

2. `insertNum(1)`- As 1 is smaller than 3, let's insert it into the Max Heap.
Max-heap      Min-Heap
   3           None
   1
-Now, we have 2 elements in the Max Heap and no elements in Min Heap. Let's
take the largest element from the Max Heap and insert it into the Min Heap,
to BALANCE the number of elements in both heaps.
Max-heap      Min-Heap
   1           3

3. `findMedian()` - As we have an even number of elements, the median will 
be the average of the top elements of both the heaps -> (1 + 3)/2 = 2.0
4. `insertNum(5)` - As 5 > 1(the top element of the Max Heap), we can 
insert it into the Min Heap. 
Max-heap      Min-Heap
   1           3
               5
-After the insertion, the total count of elements will be odd.As we had 
decided to have more numbers in the Max Heap than the Min Heap, we can take
the top (smallest) number from the Min Heap and insert it into the Max Heap.
Max-heap      Min-Heap
   3           5
   1

5. `findMedian()` - Since we have an odd number of elements, the median will
be the top element of Max Heap -> 3.
-An odd number of elements also means that the Max Heap will have one extra
element than the Min Heap.

6.`insertNum(4)` - Insert 4 into Min Heap
Max-heap      Min-Heap
   3           4
   1           5

7. `findMedian()` - As we have an even number of elements, the median will 
be the average of the top elements of both the heaps -> (3 + 4) / 2 = 3.5


-`self.max_heap = []
self.min_heap = []` - when we instantiate a new MedianOfAStream, it gets
assigned a MaxHeap and a MinHeap
-`self.max_heap = []` - we use a Max Heap to store the 1st half of the 
numbers as we are interested in knowing the largest number in the 1st half.
This largest number will always be on the top in the Max-heap(the topmost 
number/element, ie, the first element in the list).A number will only be 
inserted in this Max-heap if it is < the number ontop(the largest number).
-`self.min_heap = []`- we use a Min Heap to store the 2nd half of the 
numbers as we are interested in knowing the smallest number in the 2nd 
half.This smallest number will always be on the top in the Min-heap(the 
topmost number/element, ie the first element in the list).A number will 
only be inserted in this Min-heap if it is > the number ontop(the smallest 
number).

-`if not self.max_heap or -self.max_heap[0] >= num:
    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))` - The 
opposite of < truly and genuinely is >=.In the paragraph above, we 
mentioned that an element(a number in our case) will be inserted into the 
Max heap if its < the number ontop(the Largest number); in this condition 
we are saying if the maxHeap is empty OR the number ontop(The largest number
) is >= num(which also means num < -self.max_heap[0]), push the element onto 
the maxHeap.Now, Python's heapq module only provides a Min-heap 
implementation.In order to implement a Max-heap using the same heapq module,
we will store only negative numbers in our MaxHeap `self.max_heap`.By so 
doing, `self.max_heap[0]` returns the smallest element from `self.max_heap` 
which is actually the LARGEST value (in terms of absolute value ie
`-(-self.max_heap[0])`), since `self.max_heap` is being used as a Max-heap 
by storing negative values.This value will be at the root of the 
heap or at the top of the Max heap, which top is max_heap[0] since we 
implementing the Max heap using the list D.S.So, in `-self.max_heap[0]`, 
the `-` sign is used to negate the value of the top most element or number 
of our Max heap, so that it gives the actual maximum value in the Max heap. 
-`else: heapq.heappush(self.min_heap, num)`- The opposite of `or` truly and
genuinely is `and`.When the else part is executed, it means the maxHeap is
not EMPTY AND the element ontop in the Max heap(the LARGEST number) is 
< num; in this case, we add `num` into minHeap, hence the line 
`heapq.heappush(self.min_heap, num)`

-`if len(self.max_heap) > len(self.min_heap) + 1:
    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))`- if the 
condition is true, it means that maxHeap has 1 MORE element than the 
minHeap(maxHeap's length is > the length of the minHeap by 1) and if thats 
the case, we have to BALANCE THE HEAPS so that they have an equal number of
elements, by taking the largest element(element ontop) from the Max Heap 
and insert it into the Min Heap hence the line 
`heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))`
-`elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))`- 
This means, first of all, that we have odd total number of elements and above
we decided/chose to have more elements in the Maxheap than the MinHeap if 
that were the case and by doing this, we are also BALANCING THE HEAPS; we
are essentially deciding to have 1 MORE element in the MaxHeap than the Min
Heap.
-`def find_median(self):
    if len(self.max_heap) == len(self.min_heap):` - if the condition evaluates
    to true, it means we have an even number of elements(in total from both 
    heaps), so to find the median, we take the average of middle two elements(
    the topmost elements of both heaps) hence the line,
    `return (-self.max_heap[0] + self.min_heap[0]) / 2.0`
Otherwise, if the above if condition is false, it means max-heap will have/
has 1 more element than the min-heap which also means we have an odd number
of elements, and so the median will be the top most element of the maxheap
hence the line:`return -self.max_heap[0]` its absolute value
'''
class MedianOfAStream:
    def __init__(self):
        self.max_heap = []  # containing first half of numbers (as a max-heap)
        self.min_heap = []  # containing second half of numbers (as a min-heap)

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # either both the heaps will have equal number of elements or 
        # max-heap will have one more element than the min-heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # we have even number of elements, take the average of middle two elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # because max-heap will have one more element than the min-heap, 
        # which also means we have an odd number of elements
        return -self.max_heap[0]

#Testing
if __name__ == "__main__":
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: ", medianOfAStream.find_median())
    medianOfAStream.insert_num(5)
    print("The median is: ", medianOfAStream.find_median())
    medianOfAStream.insert_num(4)
    print("The median is: ", medianOfAStream.find_median())

'''Time Complexity: time complexity of insertNum() is O(logN) due to the 
insertion in the heap. The time complexity of findMedian() will be O(1) as 
we can find the median from the top elements of the heaps.
Space Complexity: O(N) because, as at any time, we will be storing all the 
numbers.
'''

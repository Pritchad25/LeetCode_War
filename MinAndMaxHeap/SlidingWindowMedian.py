#!/usr/bin/env python3
'''Hard
Given an array of numbers and a number K, find the median of all the 
K-sized sub-arrays (or windows) of the array.

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size 2: 
note: the windows or subarrays of size 2 are marked by quotes

[‘1, 2’, -1, 3, 5] -> median is 1.5
[1, ‘2, -1’, 3, 5] -> median is 0.5
[1, 2, ‘-1, 3’, 5] -> median is 1.0
[1, 2, -1, ‘3, 5’] -> median is 4.0

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size 3:

[‘1, 2, -1’, 3, 5] -> median is 1.0 (sort the numbers then find the median)
[1, ‘2, -1, 3’, 5] -> median is 2.0
[1, 2, ‘-1, 3, 5’] -> median is 3.0

Pattern: Two Heaps
Similarities: share similarities with `MedianOfAStream`.
Approach:
-We can follow a similar approach of maintaining a max-heap and a min-heap 
for the list of numbers to find their median.
-The only difference is that we need to keep track of a sliding window of
K numbers, meaning, in each iteration, when we insert a new number in the 
heaps, we need to remove one number from the heaps which is going out of 
the sliding window.
-After the removal, we need to rebalance the heaps in the same way that we 
did while inserting.

-The main steps of our algorithm are that `we can insert a new number in 
the heaps(our Sliding window) at ANY ITERATION, BUT when we need to remove 
one number from the heaps which is going out of the sliding window(ie when 
we need to remove 1 number from the heaps, our Sliding Window),before we do
that we need to determine the median;these 2 events are NOT MUTUALLY EXCLUSIVE,
ie they have to take place at the same time`.They can only take place at the
same time, when we have AT LEAST K ELEMENTS IN OUR SLIDING WINDOW(ie when
we have K OR MORE ELEMENTS in TOTALITY on both our heaps); ie when 
len(maxHeap) + len(minHeap) >= K.When we dont have at least K elements
in our sliding window(ie when len(maxHeap) + len(minHeap) < K AT ANY POINT
IN TIME,ie AT ANY ITERATION), THEN we cant remove an element from the sliding
window AND we cant determine the median of a subarray or window of size K.

-`PriorityQueueWithRemove` - This class will represent a priority queue that
supports removal of elements and can function as either a Min-heap or a 
Max-heap based on the `is_min_heap` flag(attribute).So, we can say this is 
a Max Heap or Min Heap implementation using a Priority Queue with remove 
functionality.

-`def __init__(self, elements=None, is_min_heap=False):`- This is the 
constructor method (__init__) for the class. It initializes an instance of 
the class, which is a priority queue with remove functionality.
-`elements=None` means that the constructor can take an optional list of 
elements to initialize the heap.If no elements are provided, it defaults to
None.

-`is_min_heap=False` is a boolean flag that indicates whether the priority 
queue should function as a Min-Heap.By default, it is set to False, meaning
the priority queue will function as a Max-heap unless specified otherwise.
-`self.is_min_heap = is_min_heap` - This line assigns the value of the 
`is_min_heap` parameter to an instance variable `self.is_min_heap`, which
attribute acts as our boolean flag to determine which type of heap we want 
to implement(Min Heap or Max Heap)using this Priority Queue.

-`self.heap = elements if elements else []` - This line initializes the 
instance variable `self.heap` with the provided elements if they are not 
None. If `elements` is None, it initializes `self.heap` as an empty list [].

-`heapq.heapify(self.heap)` - This line uses the `heapq.heapify` function to 
transform the list `self.heap` into a valid heap. The heapq module in Python 
provides an implementation of the Min-heap. If `self.is_min_heap` is True, 
this will be a Min-heap. If `self.is_min_heap` is False, the elements will 
need to be negated to simulate a Max-heap

-`def push(self, value):` - this object method define the push functionality
or mechanism for our Priority Queue.We are going to push `value` into our
Priority Queue depending on whether we are implementing a Min-Heap or a
Max-Heap using this Priority Queue.We already know that the `self.is_min_heap`
instance variable or attribute helps to determine which heap type we want
to implement, hence in this `push` method we check if this attribute's 
value is true(in which case we push `value` into our Priority Queue as is, 
as it will mean that we are implementing a Min-Heap using our Priority 
Queue) & if its not, we negate `value` as we push it into our Priority 
Queue, as it will mean that we are implementing a Max-Heap using our 
Priority Queue.
-We read the following line as follows:
`if self.is_min_heap:
            heapq.heappush(self.heap, value)` - If we are implementing a Min
            Heap, then push this value as is into our Min-Heap `self.heap` 
            which we are implementing using our Priority Queue.
-`def pop(self):`- this method defines the pop functionality of the Priority
Queue. Similar to the push method, the way we pop a value from the Priority
Queue depends on which type of heap we are implementing using our Priority 
Queue.We check which type of heap we are implementing using our attribute
`self.is_min_heap`; if it's value is true, then it means we are implementing
a Min-Heap using our Priority Queue, thus we pop the `value` as it is and if
it's value is false, then it means we are implementing a Max-Heap using our
Priority Queue and because of this, all our values in the Priority Queue were
negated or are negatives and so, when we pop them from the Priority Queue, we
want to get the absolute value, by negating them again hence the line
`-heapq.heappop(self.heap)`

-`def top(self):` this method returns the element or the value at the top
of the Heap.Since we are implementing either a Min-Heap or a Max-Heap using
a Priority Queue which is by nature structured as a list, the element ontop
of the Min-Heap/Max-Heap will be the first element in our Priority Queue(ie
the element in index 0).So, similar to the `push` & `pop` methods, we 
determine which type of heap we are implementing using the attribute
`self.is_min_heap`; if its the Min-Heap(seen by the attribute's value being
true), we return the first element(element at index 0) of the Priority Queue
as is hence the line `return self.heap[0]` and if its the Max-Heap(seen
by the attribute's value being false), we negate the first element of the
Priority Queue (which, in this case, is having all its elements as negative
values), to get the absolute(true/actual)value of the element, hence the
line `return -self.heap[0]`

-`def remove(self, value):`- this instance method removes a value from the
heap. In order for us to remove a value from the Heap, we have to first
determine which type of heap is being implemented by our Priority Queue,
so that we do appropriate adjustments before removing the value(which
appropriate adjustments are: if its a Min Heap we are implementing, then
we remove the value as is and if its a Max Heap we are implementing, then we
ensure we remove the absolute/true value of the value from the heap by
negating the value).Now, after removing the value from the heap, we need to
heapify the heap again; if we are implementing a Min Heap, then the 
function `heapify` will do as expected because by default, it produces a 
Min Heap; if its a Max-Heap we are implementing, then elements will need
to be negated to implement a Max-Heap.Then True will be returned, otherwise
False. The value we are removing may not be a value at all or may not be 
there and we want to handle such cases; hence the use of a try..catch block. 

`class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = PriorityQueueWithRemove()
        self.min_heap = PriorityQueueWithRemove(is_min_heap=True)`- Here,
we define the instantiation of a new `SlidingWindowMedian` object.Our
Sliding Window(subarray) consists or comprises of both the Max Heap and the 
Min Heap, hence why, in the instantiation, we use 2 attributes namely 
`self.max_heap` & `self.min_heap`.But,these 2 attributes are actually 
`PriorityQueueWithRemove()` objects, because, we are implementing the 
MaxHeap & the MinHeap using a Priority Queue with remove functionality.Now
because, in the definition of the instantiation of the 
`PriorityQueueWithRemove` object above, we specified that, 2 optional 
parameters can be passed, namely `elements` & the boolean flag which helps us
determine which heap we want to implement `is_min_heap`, for the 
`self.max_heap` attribute, we dont pass any parameters in 
`PriorityQueueWithRemove()` to specify that we are instantiating a MaxHeap
which will be implemented using a priority queue with remove functionality; 
for the `self.min_heap`attribute, we specify a value `True` for our boolean 
flag `is_min_heap` in `PriorityQueueWithRemove()` to specify that we are 
implementing a MinHeap using our priority queue with remove functionality

-`if self.max_heap.size() == 0 or nums[i] <= self.max_heap.top():
                self.max_heap.push(nums[i])` - ie, if the MaxHeap is empty
or if the number which we are currently standing on `nums[i]` is less or
equal to the LARGEST number(the topmost element) of the MaxHeap, then push
this current number which are currently standing on to the Max-Heap.Any one
of these propositions or (both of them) has to be true for the statement 
or,in this case, the if condition to be TRUE.Because `max_heap` is a
`PriorityQueueWithRemove()`, we use the push method of this object; this
method handles whatever appropriate adjustments are supposed to be done.
-The opposite of <= truly and genuinely is >.Above, we mentioned that this 
problem is similar to MediaOfAStream; so therefore, we know that an 
element(a number in our case) will be inserted into the Max heap if 
its <= the number/element ontop(the Largest number, at index 0); in this 
condition we are saying, if the maxHeap is empty OR the number 
ontop(The largest number) is > nums[i](which also means nums[i] <= 
maxHeap[0]), push the element `nums[i]` onto the maxHeap.

-The `else`'s execution means that the Max-Heap is not empty AND the number
on which we are currently standing `nums[i]` is > topmost number of the 
Max-Heap, therefore we have to put nums[i] in the Min-Heap.Remember, for a
number nums[i] to go into the Max-Heap, it has be <= the topmost element of
the Max-Heap. The opposite of `or` truly & genuinely is `and`.When the else 
part is executed, it means the maxHeap is not EMPTY AND the element ontop 
in the Max heap(the LARGEST number) is < nums[i]; in this case, we add 
`nums[i]` into minHeap, hence the line `minHeap.heappush(minHeap, nums[i])`.

-`for i in range(len(nums))` - ie we are iterating the whole array or list
from the beginning to the end OR we are iterating the array starting from
index i=0 up to index i=len(nums) - 1, WHICH is the whole array in actual
fact.

-`if (i - k + 1 >= 0)`- The sliding window is both of our heaps. The number
of elements in our Sliding window IS the  number of elements on both heaps.
This formular `i - k + 1` helps us to determine if we have at least K(ie K 
OR MORE) elements in the sliding window(ie if we have AT LEAST K elements 
in both our heaps).If the expression evaluates to 0, then we have exactly 
K elements in the sliding window(ie we have exactly K elements in TOTALITY
on both heaps); if it evaluates to > 0, then we have more than K elements in the 
sliding window(ie we have more than K elements in TOTALITY on both heaps).
Both of these cases(the expression evaluating to 0 OR the expression 
evaluating to > 0) are part of the `AT LEAST K ELEMENTS` group/denomination.

-Note: that when are inserting an element into our Sliding Window(ie into
either of Heaps), we have to balance our heaps(in the case of the very
first insertion of an element into our Sliding Window) or rebalance our
heaps(in the case of subsequent insertions of more elements into our
Sliding Window). Similarly, when we have determined our median and have
removed the element going out of the Sliding Window(which clearly shows that
these 2 events are NOT MUTUALLY EXCLUSIVE), we have to rebalance our heaps
as well.

If the above condition is true(meaning we have K or more elements(At
Least K elements) in the sliding window), we add the median to the the 
`result` array.Before adding the median to the result array, we have to 
check the sizes of both heaps.Hence the line:
`if self.max_heap.size() == self.min_heap.size()`.If the sizes are equal, 
we have an even number of elements in OUR SLIDING WINDOW, therefore we take 
the average of the 2 top elements of our sliding window 
`median = (self.max_heap.top() + self.min_heap.top()) / 2.0`
-`else: median = self.max_heap.top()` - the else parts means we have an odd
number of elements in OUR SLIDING WINDOW, therefore we take the topmost
element of our MaxHeap as the median.

-This formular `i - k + 1` ALSO represents the index of the element that 
should be removed from the heaps(ie represents index of the element going 
out of the sliding window).Hence in this line below, we store this element 
into a variable `element_to_remove = nums[i - k + 1]`.Now, we need to check
in which Heap `element_to_remove` is stored at before removing it. We KNOW
that every element that is in the MaxHeap has to be <= the topmost element 
of the MaxHeap, hence we use this fact to check if `element_to_remove` is in
the Maxheap in this line `if element_to_remove <= self.max_heap.top():`.If
its there then remove it from the MaxHeap. Otherwise (meaning the element
`element_to_remove` is > the topmost element/number in our Max Heap
(the largest number)), remove the element `element_to_remove` from the 
MinHeap, as, for sure its not the MaxHeap since > topmost element of MaxHeap.

-`if self.max_heap.size() > self.min_heap.size() + 1:
    self.min_heap.push(self.max_heap.pop())` if the condition is true, it 
means that maxHeap has 1 MORE element than the minHeap(maxHeap's length is 
> the length of the minHeap by 1) and if thats the case, we have to 
REBALANCE THE HEAPS so that they have an equal number of elements, by taking 
the largest element(element ontop) from the Max Heap and insert it into the 
Min Heap hence the line following the condition.

-`elif self.max_heap.size() < self.min_heap.size():
    self.max_heap.push(self.min_heap.pop())` in rebalanceHeaps(), this line 
means that the length of MaxHeap is < length of MinHeap, so if that is the 
case, then we will REBALANCE THE HEAPS BY 'deciding/choosing to have more 
numbers in Max-heap than the Min Heap'as  mentioned on `MedianOfAStream` 
hence the following line of the above else if condition.

-so with regards to the above if & elseif statements of rebalance() method,
EITHER 
    (maxHeap is 1 MORE element longer than minHeap or maxHeap's length <
    minHeap's length) in which case we have to REBALANCE THE HEAPS by taking 
    the largest element(element ontop) from the Max Heap and insert it into the
    minHeap or by 'deciding/choosing to have more numbers in Max-heap than the 
    Min Heap' respectively 
OR 
    the Heaps are BALANCED(have equal number of elements) 
'''
import heapq

class PriorityQueueWithRemove:
    def __init__(self, elements=None, is_min_heap=False):
        self.is_min_heap = is_min_heap
        self.heap = elements if elements else []
        heapq.heapify(self.heap)
    
    def push(self, value):
        if self.is_min_heap:
            heapq.heappush(self.heap, value)
        else:
            heapq.heappush(self.heap, -value)
    
    def pop(self):
        if self.is_min_heap:
            return heapq.heappop(self.heap)
        else:
            return -heapq.heappop(self.heap)
    
    def top(self):
        if self.is_min_heap:
            return self.heap[0]
        else:
            return -self.heap[0]
    
    def remove(self, value):
        try:
            if self.is_min_heap:
                self.heap.remove(value)
            else:
                self.heap.remove(-value)
            heapq.heapify(self.heap)
            return True
        except ValueError:
            return False
    
    def size(self):
        return len(self.heap)

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = PriorityQueueWithRemove()
        self.min_heap = PriorityQueueWithRemove(is_min_heap=True)
    
    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            #Insert element and Balance the Heaps
            if self.max_heap.size() == 0 or nums[i] <= self.max_heap.top():
                self.max_heap.push(nums[i])
            else:
                self.min_heap.push(nums[i])
            self.rebalance_heaps()
            
            #if we have at least K elements in Sliding window, find median,
            #remove element and rebalance heaps in that order.
            if i - k + 1 >= 0:
                if self.max_heap.size() == self.min_heap.size():
                    median = (self.max_heap.top() + self.min_heap.top()) / 2.0
                else:
                    median = self.max_heap.top()
                result.append(median)
                
                #remove element going out of Sliding Window & Balance Heaps
                element_to_remove = nums[i - k + 1]
                if element_to_remove <= self.max_heap.top():
                    self.max_heap.remove(element_to_remove)
                else:
                    self.min_heap.remove(element_to_remove)
                self.rebalance_heaps()
        return result
    
    def rebalance_heaps(self):
        if self.max_heap.size() > self.min_heap.size() + 1:
            self.min_heap.push(self.max_heap.pop())
        elif self.max_heap.size() < self.min_heap.size():
            self.max_heap.push(self.min_heap.pop())

# Testing
if __name__ == "__main__":
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: ")
    for num in result:
        print(num, end=" ")
    print("") # print an empty line

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: ")
    for num in result:
        print(num, end=" ")

'''Time Complexity: O(N*K), where N is the number of elements in our input
array and K is the size of the sliding window.This is due to the fact that 
we are going through all the N numbers and, while doing so, we are doing 2 
things:
1)Inserting/removing numbers from heaps of size K.This will take O(logK)
2)Removing the element going out of the sliding window. This will take O(K)
as we will be searching this element in an array of size K, (i.e., a heap).

Space Complexity: Ignoring the space needed for the output array, the space
complexity will be O(K) because, at any time, we will be storing all the 
numbers within the sliding window.
'''
    
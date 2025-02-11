#!/usr/bin/env python3
'''Given an array of intervals, find the next interval of each interval. In
a list of intervals, for an interval i, its next interval j will have the 
SMALLEST `start` >= end of i.(j.start >= i.end)
Write a function to return an array containing indices of the next interval
of each input interval. If there is no next interval of a given interval, 
return -1. It is given that none of the intervals have the same start 
point.

Problem Clarification: In a list of intervals, for an interval i, its next 
interval j will have the SMALLEST `start` >= end of i.(j.start >= i.end) 
meaning we can have a list of intervals; the next interval of i(which is j)
should be the one with the SMALLEST start time in that list of intervals, 
which SMALLEST start time should be >= end of i, AS we could have more than
1 interval whose start times are also >= end of i.

Example 1
Input: Intervals [[2,3], [3,4], [5,6]]
Output: [1, 2, -1]
Explanation: The next interval of [2,3] is [3,4] having index 1.Similarly, 
the next interval of [3,4] is [5,6] having index 2.There is no next interval
for [5,6] hence we have -1.

Example 2
Input: Intervals Intervals [[3,4], [1,5], [4,6]]
Output: [2, -1, -1]
Explanation: The next interval of [3,4] is [4,6] which has index 2.There is 
no next interval for [1,5] and [4,6]

Solution
-A brute force solution could be to take one interval at a time and go 
through all the other intervals to find the next interval. This algorithm 
will take O(N2), where N is the number of input intervals.
-We can utilize the Two Heaps approach.
-We can push all intervals into 2 heaps: one heap to sort the intervals on 
maximum start time (let's call it `maxStartHeap`) and the other on maximum
end time (let's call it `maxEndHeap`).
-We can then iterate through all intervals of the `maxEndHeap` to find their
next interval.
- Our algorithm will have the following steps:
1. Take out the top (having highest end time) interval from the `maxEndHeap`
to find its next interval. Let's call this interval `topEnd`. `topEnd`'s
next interval's start time, will always be >=  `topEnd`'s end time.
2. Find an interval in the `maxStartHeap`(where top is having highest start
time) with the closest start >= to the end of `topEnd`.Since `maxStartHeap`
is sorted by `start` of intervals, it is easy to find the interval with the
highest `start`. Let's call this interval `topStart`.
3. Add the index of `topStart`in the result array as the next interval of
`topEnd`.If we can't find the next interval, add -1 in the result array.
4. Put the `topStart` back in the `maxStartHeap`, as it could be the next 
interval of other intervals.
5. Repeat the steps 1-4 until we have no intervals left in `maxEndHeap`.

-`result = [-1] * n` - ie, fill the list or array `result` with -1, n times
eg if n=3, then fill -1 inside the `result` 3 times.
-`heapq.heappush(max_start_heap, (-intervals[i].start, i))` - we pushing
a tuple comprising of the start time AND the index or position of this start
time in the original `intervals` array.
-`if -max_start_heap[0][0] >= -top_end[0]:`- So, here we are saying if 
j.start is >= i.end (the end time of interval which we are currently standing
in which is represented by `top_end`) then we have found the current 
interval `top_end`'s next interval. If the condition is false, then it means
the current interval which we are standing on `top_end` doesnt have a next
interval AS its(top_end's) END TIME is > the HIGHEST START TIME that we have
in the `intervals` list. So, -1 will stand in the index or position that 
represents `top_end`'s index or position in the original `intervals` list. 
-`end_index` represents the position or index in the `result` list, in which
the location or position or index of `top_end`'s next interval is located in
the ORIGINAL `intervals` list.
-`start_index` represents the position or index of `top_end`'s next interval
in the ORIGINAL `intervals` list.
-Note that all the individual intervals whose next interval we want to find
are in the array or list `max_end_heap`.That's why we are popping the top
elements of `max_end_heap` and not returning them to the heap `max_end_heap`.
-`while max_start_heap and -max_start_heap[0][0] >= -top_end[0]:` - here, we
are determining if there is a CLOSER or SMALLER start time(which is also
>= top_end's end time) than the one that we currently have. If the condition
above is true, it means we do, so we make adjustments to `top-start` &
`start_index`. If the condition is false, then it means the START TIME  that
we currently have IS the SMALLEST or CLOSEST we will EVER have.
-`result[end_index] = start_index` - assigning the position or index of 
`top_end`'s next interval in the ORIGINAL `intervals` list TO `result` list.
'''
import heapq

class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end

class NextInterval:
    '''Next Interval'''
    @staticmethod
    def findNextInterval(Intervals):
        '''Finds the next interval of each interval 
        in a list of intervals
        '''
        n = len(Intervals)
        max_start_heap = []
        max_end_heap = []
        result = [-1] * n

        #push all intervals into 2 heaps: `max_start_heap` to sort the 
        #intervals on maximum start time; `max_end_heap` to sort the 
        #intervals on maximum end time
        for i in range(n):
            heapq.heappush(max_start_heap, (-Intervals[i].start, i))
            heapq.heappush(max_end_heap,(-Intervals[i].end, i))
        
        #iterate `total number of intervals in `intervals`` times, going 
        #through each interval of `max_end_heap` to find its next interval
        for _ in range(n):
            #Take out the top item from the `maxEndHeap` to find its next 
            #interval.lets call it `top_end`
            top_end = heapq.heappop(max_end_heap)
            end_index = top_end[1]

            if -max_start_heap[0][0] >= -top_end[0]:
                top_start = heapq.heappop(max_start_heap)
                start_index = top_start[1]

                #Determine if there is a CLOSER or SMALLER start time(which
                #is also >= top_end's end time) than the one that we 
                #currently have above
                while max_start_heap and -max_start_heap[0][0] >= -top_end[0]:
                    top_start = heapq.heappop(max_start_heap)
                    start_index = top_start[1]

                result[end_index] = start_index
                heapq.heappush(max_start_heap, top_start)
        return result

# Testing
if __name__ == "__main__":
    Intervals = [Interval(2, 3), Interval(3, 4), Interval(5, 6)]
    result = NextInterval.findNextInterval(Intervals)
    print("Next Interval Indices are: ", result)

    Intervals = [Interval(3, 4), Interval(1, 5), Interval(4, 6)]
    result = NextInterval.findNextInterval(Intervals)
    print("Next Interval Indices are: ", result)

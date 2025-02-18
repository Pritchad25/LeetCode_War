#!/usr/bin/env python3
from heapq import *

'''Given a list of intervals, find the point where the maximum number of intervals overlap

Question Clarification:
-`find the point` - find the point where the maximum overlap occurs
-`maximum number of intervals overlap` - this number or this maximum overlap is the point where 
the HIGHEST number of intervals overlap, meaning it is common amongst these OVERLAPPING intervals

Approach
1. Sort all the intervals on their start time.(our intervals would now be in ascending order of 
start time).
2. Create a Min-Heap to STORE all the OVERLAPPING intervals. When we have stored all the
OVERLAPPING intervals in the Min Heap, the total count of all those intervals is the maximum or
HIGHEST number or amount of OVERLAPPING intervals in our list of intervals.This total count is 
also the size of the Min-Heap
- This Min-Heap will also be used to FIND the interval with the SMALLEST END TIME(after storing 
ALL the OVERLAPPING intervals) and return that SMALLEST END TIME because it would be the point 
where the HIGHEST number of intervals OVERLAP, meaning its common amongst ALL the overlapping 
intervals.
3. Iterate through all the intervals one by one to ADD or STORE them in the min-heap. Let's say 
we are trying to store interval m1.
4. Since the min-heap contains ONLY ALL the OVERLAPPING intervals, so before adding or storing 
m1, we can remove all intervals from the heap that DONT OVERLAP with m1, ie, remove all intervals 
from the heap that have an end time <= to the start time of m1(ie remove ALL intervals that TRULY 
& GENUINELY DO NOT OVERLAP with interval m1 or are MUTUALLY EXCLUSIVE to interval m1). Another 
way of saying this or putting this is, we want to remove all intervals from the heap where the 
start time of m1 >= end time of all those other intervals(because this also means ALL intervals 
TRULY & GENUINELY DO NOT OVERLAP with interval m1 or are MUTUALLY EXCLUSIVE to interval m1))
-when we remove an interval, the variable `maxOverlapPoint` in this line 
`maxOverlapPoint = max(maxOverlapPoint, (int)minHeap.size());`remains the same, meaning either
we are removing an interval and the variable remains the same OR we adding an interval into the
Min-Heap and the value of the variable increments, ie, these 2 events are Mutually Exclusive 
5. Now ADD or STORE interval m1 to the Min-Heap. (because we said Min-Heap will store ALL 
OVERLAPPING intervals)
6. The heap will ALWAYS have all the OVERLAPPING intervals, so we will need to keep track of the 
total count of ALL OF THEM(ie ALL THE OVERLAPPING intervals).So, we will keep a counter to 
remember the maximum size of the heap at any time(ie for every iteration of outer for-loop)& this 
will be the point where the HIGHEST number of intervals OVERLAP OR the common number between all
the OVERLAPPING intervals
-step 3 clarity - `Iterate through all the intervals one by one` this is the outer For loop
-then we remove all the intervals in the Min-Heap that are Mutually Exclusive to the one
we are currently standing in, which we want to add to our Min-Heap.We then add the one we are 
currently standing in to the Min Heap.After removing all those other intervals and adding the 
one we are currently standing in, in the Min-Heap, we are only left with intervals that Overlap 
with the one we are currently standing in and all of these ARE OUR OVERLAPPING intervals, so we 
need rooms for all of them.
'''
class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        # Less than operator for priority queue, based on interval end time
        return self.end < other.end

class MaxIntervalsOverlap:
    '''Max Intervals Overlap'''
    @staticmethod
    def IntervalsOverlapPoint(intervals):
        '''Finds the Actual point where the
        maximum number of intervals overlap
        '''
        if not intervals:
            return 0
        
        #Sort the intervals by start time
        intervals.sort(key=lambda x: x.start)

        max_overlap = 0 #keeps track of the max number of overlapping intervals
        overlap_point = 0 #keeps track of the point where the max number of intervals overlap
        min_heap = []
        for interval in intervals:
            # Remove all intervals that have ended or finished
            while min_heap and interval.start >= min_heap[0].end:
                heappop(min_heap)
            # Add the current interval into min_heap
            heappush(min_heap, interval)
            # All Overlapping intervals are in min_heap, so we need to keep track of their total 
            #count
            if len(min_heap) > max_overlap:
                max_overlap = len(min_heap) #keep track of the size of the min-heap if its greater
                overlap_point = min_heap[0].end #keeping track of the interval with the smallest
                #end time in the Min-Heap; that end time is our maximum overlap point
        return overlap_point

# Testing
if __name__ == "__main__":
    input = [Interval(4, 5), Interval(2, 3), Interval(2, 4), Interval(3, 5)]
    result = MaxIntervalsOverlap.IntervalsOverlapPoint(input)
    print("Point where Highest number of intervals overlap is: ", result)
#!/usr/bin/python3
'''Given a list of non-overlapping intervals sorted by their start time, insert a given interval
at the correct position and merge all necessary intervals to produce a list that has only 
mutually exclusive intervals.

-`non-overlapping intervals` means Mutually Exclusive Intervals
-`sorted by their start time` means for any 2 intervals 'a'&'b' a.start is ALWAYS <= b.start
-`correct position` means this interval(lets call it 'x') should be inserted in a place such that
its start time(x.start) is in the CORRECT SORTING ORDER in the resultant list of mutually 
exclusive intervals.
-`all necessary intervals` the necessary intervals are the OVERLAPPING intervals.

Approach:
-If the given list was not sorted, we could have simply appended the new interval to it and used
the merge() function from `Merge Intervals`. But since the given list is sorted, we should try to 
come up with a solution better than O(NlogN).

-When inserting a new interval in a sorted list, we need to first find the correct index where 
the new interval can be placed meaning we need to skip all the intervals which end before the 
start of the new interval. So, we can iterate through the given sorted list of intervals and 
skip ALL the intervals which fulfill the following condition: `intervals[i].end < newInterval.start`,
where `intervals[i]` is an interval which we will be standing in at each iteration of the loop,
`intervals[i].end` is an interval's end.

-`intervals[i].end < newInterval.start` means the current interval's(on which we standing on) end
is less than the start of the new Interval which we want to insert into the sorted list of
intervals, we want to skip this interval. intervals is the list of sorted intervals

-Once we have found the correct place, we can follow an approach similar to `Merge Intervals` to 
insert and/or merge the new interval. Let's call the new interval 'a' and the first interval 
that does not satisfy the above condition , 'b'.  There are 5 possibilities(as shown in picture 
of question) in which 'a' & 'b'. 2-5 are possibilities in which intervals 'a' & 'b' overlap
1. 'a' & 'b' dont OVERLAP meaning b.start > a.end ie start of interval 'b' > end of interval 'a',
so we simply insert interval 'a' before interval 'b'.
2-5. intervals 'a' & 'b' overlap and the start time of the new merged interval `interval c` will
vary on which interval has the minimum start between the two. The end time of the new merged
interval `interval c` will vary on which interval has the maximum start between the two. So, to
handle that "variance" for the start time and end time of `interval c`, we will use `min` &
`max` respectively.
-Note that the merging scenarios are represented by the condition:`b.start <= a.end`

-The diagram in question clearly shows the merging approach. To handle all 4 merging 
scenarios, we need to do something like this:
c.start = min(a.start, b.start)
c.end = max(a.end, b.end)

Our overall algorithm will look like this:
1. Skip all intervals which end before the start of the new interval, i.e., skip all intervals
that fulfill the following condition: `intervals[i].end < newInterval.start`
2. Let's call the last interval that does not satisfy the above condition, interval 'b'. If 'b'
overlaps with the new interval 'a',(i.e. b.start <= a.end), we need to merge them into a 
new interval 'c': 
c.start = min(a.start, b.start)
c.end = max(a.end, b.end)
3. We will repeat the above two steps to merge 'c' with the next overlapping interval.

-`(i < len(intervals) and intervals[i].end < newInterval)` loop runs from the first element
of the list of sorted intervals to the last element(last interval). Loop will skip and add to
output (mergedIntervals) ALL intervals that come before `newInterval` ie all intervals that
end before the start of `newIntervals`. When this loop exits, we will be holding the index of
the interval which doesnt fulfil the above condition.
-`mergedIntervals` is our list of MUTUALLY EXCLUSIVE intervals

-`while (i < len(intervals) and intervals[i].start <= newInterval.end)` Here, we're merging all 
intervals that overlap with `newInterval`. `i` is holding the index of the first interval that
didnt fulfill the condition in the first loop, which interval we want to check if its overlapping 
with `newInterval`. If it does, then we merge it with `newInterval`.*Now, starting from this 
current interval we're standing in (which is in index `i`) going forward(to all other intervals 
AFTER this current one UNTIL the last interval in the `intervals` list) ie ``i < len(intervals)``, 
we want to check if they also overlap with this `newInterval` ie 
``intervals[i].start <= newInterval.end`` and if they do, MERGE them with this newInterval ie
``newInterval.start = min(intervals[i].start, newInterval.start)
newInterval.end = max(intervals[i].end, newInterval.end)
``* 
So, to AUTOMATE the above statements denoted by asterisk characters in code, we use a while loop
and ensure that it moves to the next interval AUTOMATICALLY by including `i += 1` at the end.
The loop will exit when we have reached the last interval in the `intervals` list OR the one
that we're currently standing in doesnt OVERLAP with the new interval `newInterval`. Either way,
when it exits, we want to add this new Interval `newInterval` onto our list of MUTUALLY EXCLUSIVE
intervals `mergedIntervals` ie next step, `mergedIntervals.append(newInterval)`

-`while (i < len(intervals)):`
Now, lets consider the 2 cases above that will cause the loop to exit:
>Case 1 `when we have reached the last interval in the `intervals` list` we are going to simply
add this last interval AFTER our newInterval `newInterval` to `mergedIntervals`
>Case 2 (Higher Chances of Occuring) `the one that we're currently standing in doesnt OVERLAP 
with the new interval `newInterval` 
For both the above cases, we're going to use a loop to AUTOMATICALLY start from that last interval
(case1)or from that current interval(case2) UNTIL the last interval, to add all the remaining
intervals to `mergedIntervals` as they are MUTUALLY EXCLUSIVE.
'''
class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end

class InsertInterval:
    '''Modification of a list of Intervals'''
    @staticmethod
    def insert(intervals, newInterval):
        '''Insert a new Interval into a sorted list
        of Intervals
        
        Args:
            intervals - list of sorted intervals
            newInterval - the new Interval to insert at the correct position
        '''
        #if the `intervals` is empty, return the new Interval
        if len(intervals) < 1:
            return newInterval
        mergedIntervals = []
        i = 0

        #skip (and add to output) all intervals that come before the `newInterval`
        while(i < len(intervals) and intervals[i].end < newInterval.start):
            mergedIntervals.append(intervals[i])
            i += 1
        
        #merge all intervals that overlap with `newInterval`
        while (i < len(intervals) and intervals[i].start <= newInterval.end):
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(intervals[i].end, newInterval.end)
            i += 1
        
        #insert the newInterval
        mergedIntervals.append(newInterval)

        #add all the remaining intervals to the output
        while (i < len(intervals)):
            mergedIntervals.append(intervals[i])
            i += 1
        
        return mergedIntervals

#Testing
if __name__ == "__main__":
    input_intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    print("Intervals after inserting new Interval: ", end=" ")
    for interval in InsertInterval.insert(input_intervals, Interval(4, 6)):
        print(f"[{interval.start}, {interval.end}]", end=" ")
    
    print("\nIntervals after inserting the new interval: ", end=" ")
    for interval in InsertInterval.insert(input_intervals, Interval(4, 10)):
        print(f"[{interval.start}, {interval.end}]", end=" ")
    
    input_intervals = [Interval(2, 3), Interval(5, 7)]
    print("\nIntervals after inserting the new interval: ", end=" ")
    for interval in InsertInterval.insert(input_intervals, Interval(1, 4)):
        print(f"[{interval.start}, {interval.end}]", end=" ")

        
        

        
'''Time Complexity: O(N), where N is the total number of intervals, as we are iterating through 
all the intervals only once
Space Complexity: O(N) as we need to return a list containing all the merged intervals.
'''
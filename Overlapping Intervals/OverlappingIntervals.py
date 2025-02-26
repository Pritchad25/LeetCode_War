#!/usr/bin/python3
'''Given a set of intervals, find out if any two intervals overlap.
Example
Intervals: [[1,4], [2,5], [7,9]]
Output: true

Similarities: Merge Intervals
Approach:
-We can follow the same approach as discussed in MergeIntervals to find if any two intervals 
overlap. The approach goes as follows:
-Let's take the example of two intervals('a'&'b') such that a.start <= b.start .There are 4 
possible scenarios:
1. 'a' and 'b' DO NOT OVERLAP, ie they're MUTUALLY EXCLUSIVE intervals 'a' is followed by 'b'
2. 'a' and 'b' OVERLAP, 'b' ends after 'a'
3. 'a' COMPLETELY OVERLAPS 'b'.
4. 'b' COMPLETELY OVERLAPS 'a', but both have same start time.
-Our algorithm will look like this:
1. Sort the intervals on the start time to ensure that for any 2 intervals 'a'& 
'b' a.start <= b.start
2. if 'a' overlaps 'b' (i.e. b.start <= a.end) we return true.

-`b.start <= a.end` means the start of interval 'b' is less or equal to the start of interval
'a'; if that is the case then that means the two intervals OVERLAP, therefore we will return
True.
-note also that this condition `b.start <= a.end` means that the two intervals OVERLAP ONLY IF
we have sorted the intervals 'a' & 'b' such that a.start <= b.start
'''
class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end

class SameMergeIntervals:
    '''Overlapping Intervals'''
    @staticmethod
    def OverlappingIntervals(intervals):
        '''Determines if there is an overlapping intervals
        in the list of intervals
        
        Args:
        intervals - the list of intervals
        '''
        if len(intervals) < 2:
            return False #There's no overlapping intervals because there is only 1 interval or
        #at the very worst, no intervals is the list of intervals

        # Sort the intervals by start time
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end #storing the start & end of 1st interval
        for interval in intervals[1:]:
            if interval.start <= end: #Overlapping intervals, adjust the 'end'
                return True
            else: # Non-overlapping interval, add the previous interval and reset
                start, end = interval.start, interval.end #making the current one, the first one
        return False

if __name__ == "__main__":
    input_intervals = [Interval(1, 4), Interval(5, 8)]
    print("Has Overlapping intervals:", end=" ")
    print(SameMergeIntervals.OverlappingIntervals(input_intervals))
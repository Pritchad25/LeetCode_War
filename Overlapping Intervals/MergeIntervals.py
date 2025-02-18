#!/usr/bin/python3
'''Given a list of intervals, MERGE ALL the OVERLAPPING INTERVALS to produce a list that has 
only MUTUALLY EXCLUSIVE intervals (Intervals that do not occur at the same time) intervals.

MUTUALLY EXCLUSIVE intervals - intervals that do not start at the same time or place and
that do not end at the same time or place meaning they dont occur at the same time or place
and HAVE NO COMMON numbers.
Example
Intervals: [[1,4], [2,5], [7,9]]
-The OVERLAPPING INTERVALS in the above list of intervals are the intervals [1,4] & [2,5].So, we
we have to MERGE the OVERLAPPING INTERVALS to produce a list of intervals that only has intervals
that do not occur at the same time and HAVE NO COMMON numbers. So, we're going to merge the above
intervals into one and get the interval [1,5]. The intervals [1,5] & [7,9] are MUTUALLY EXCLUSIVE.
Output: [[1,5], [7,9]]

Example 2
Intervals: [[1,4], [2,6], [3,5]]
All the intervals in the above list OVERLAP. Therefore, we will MERGE them into one INTERVAL.That
interval is going be our output.
Output[[1,6]]

Approach:
-Let's take the example of two intervals('a'&'b') such that a.start <= b.start .There are four 
possible scenarios:
1. 'a' and 'b' DO NOT OVERLAP, ie they're MUTUALLY EXCLUSIVE intervals 'a' is followed by 'b'
2. 'a' and 'b' OVERLAP, 'b' ends after 'a'
3. 'a' COMPLETELY OVERLAPS 'b'.
4. 'b' COMPLETELY OVERLAPS 'a', but both have same start time.

The diagram above (in question )clearly shows a merging approach. Our algorithm will look like 
this:
1. Sort the intervals on the start time to ensure that for any 2 intervals 'a'& 
'b' a.start <= b.start
2. if 'a' overlaps 'b' (i.e. b.start <= a.end) we need to merge them into a new interval 'c'
such that:
c.start = a.start
c.end = max(a.end, b.end)
3. We will keep repeating the above two steps to merge 'c' with the next interval if it overlaps 
with 'c'.

`b.start <= a.end` means the start of interval 'b' is less or equal to the end of interval
'a'; if that is the case then that means the two intervals OVERLAP, therefore we want to merge
them into 1 interval called interval 'c'. The start of interval 'c'(c.start) will always be the 
start of interval 'a' (since start of 'a' is always less or equal to) and the end of interval 
'c' will be the max between the end of interval 'a' and end of interval 'b' because in our 3 
cases where 'a' & 'b' overlap, the one whose end is highest changes or varies in all 3 cases; 
so to handle that "VARIANCE", we use max.
-note also that this condition `b.start <= a.end` means that the two intervals OVERLAP ONLY IF
we have sorted the intervals 'a' & 'b' such that a.start <= b.start

-`if len(intervals) < 2` ie if the number of intervals in this list of intervals is < 2, return
the that interval because it is Mutually Exclusive in and of itself.
-`intervals.sort(key=lambda x: x.start)` here, sort is implementing the lambda function(an
anonymous throw-away function without a name, that is needed exactly where its been created) to
firstly get 1 interval at time(represented by the argument `x`) and return the start time of that
interval `x.start`; then `sort` will sort the individual intervals in the `intervals` list in 
ASCENDING ORDER of start time. So, basically, `lambda` takes individual intervals and returns
their start times then `sort` sorts those intervals in ASCENDING ORDER of start time.
- `for interval in intervals[1:]:` iterating through the intervals starting from interval in
index 1 up to interval at index `size of the list`` EXCLUDED eg is size of `intervals` list is
3, then loop starts at interval at index 1 up to interval at index 2
-`if interval.start <= end:` ie, if the start of the interval that we're currently standing(b.start) in
is less or equal to the end of the first interval whose values we stored(a.end), then the 2 
intervals(the first one, `interval a` & `interval b`) OVERLAP, so we have to MERGE them together
into 1 interval lets call it `interval c`; we already know that the start
of  `interval c` is going to be a.start as it is ALWAYS <= b.start. The end of `interval c` is
going to be the max of a.end & b.end because in our 3 cases where 'a' & 'b' overlap, the one 
whose end is highest changes or varies in all 3 cases;so to handle that "VARIANCE", we use max,
hence the statement that follows the if statement `end = max(interval.end, end)`, where
`interval.end` is the end of the current interval that we're standing in and `end` is the end
of the first interval(`interval a`) which we stored. So, by adjusting the end of `interval c`
we're essentially MERGING the 2 intervals into 1.
-`else` meaning the 2 intervals(the one which we are currently standing in & the first one dont
OVERLAP) so that makes the one which we are currently standing a `non-overlapping interval`, so
we have to store the first one (`interval a`) or in this case `the previous one` into the list
of MUTUALLY EXCLUSIVE intervals `merged_intervals` and then make the one which we are currently 
standing in, the first one (`interval a`). This `Interval(start, end)` is the interval object or
in Python we say, IT IS AN interval.
-In the steps following the comment `# add the last interval`, when the loop exits we will be 
standing in the last interval of the list of intervals,which by default becomes MUTUALLY 
EXCLUSIVE as there is no first interval to compare it against, so we add it to our list of 
MUTUALLY EXCLUSIVE intervals.
'''
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class MergedIntervals:
    @staticmethod
    def merge_intervals(intervals):
        if len(intervals) < 2:
            return intervals #that interval is Mutually Exclusive so return it

        # Sort the intervals by start time
        intervals.sort(key=lambda x: x.start)

        merged_intervals = [] #will hold only Mutually Exclusive Intervals
        start, end = intervals[0].start, intervals[0].end #storing the start & end of 1st interval
        for interval in intervals[1:]:
            if interval.start <= end:  # Overlapping intervals, adjust the 'end'
                end = max(interval.end, end)
            else:  # Non-overlapping interval, add the previous interval and reset
                merged_intervals.append(Interval(start, end)) #adding the first one or the previous one 
                start, end = interval.start, interval.end #making the current one, the first one
                #for comparison with the next interval

        # Add the last interval
        merged_intervals.append(Interval(start, end))
        return merged_intervals

if __name__ == "__main__":
    input_intervals = [Interval(1, 3), Interval(2, 5), Interval(7, 9)]
    print("Merged intervals:", end=" ")
    for interval in MergedIntervals.merge_intervals(input_intervals):
        print(f"[{interval.start},{interval.end}]", end=" ")

    input_intervals = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
    print("\nMerged intervals:", end=" ")
    for interval in MergedIntervals.merge_intervals(input_intervals):
        print(f"[{interval.start},{interval.end}]", end=" ")

    input_intervals = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
    print("\nMerged intervals:", end=" ")
    for interval in MergedIntervals.merge_intervals(input_intervals):
        print(f"[{interval.start},{interval.end}]", end=" ")

'''Time Complexity: O(N*logN) where 'N' is the total number of intervals. We are iterating the 
intervals only once which will take O(N) in the beginning though, since we need to sort the 
intervals our algorithm will take O(N*logN)

Space Complexity: O(N) as we need to return a list containing all the merged intervals. We will 
also need O(N) space for sorting 

SIMILAR PROBLEMS
Given a set of intervals, find out if any two intervals overlap.
Example
Intervals: [[1,4], [2,5], [7,9]]
Output: true
-The Intervals [1,4] and [2,5] overlap
Solution:
-We can follow the same approach as discussed above to find if any two intervals overlap.
'''
#!/usr/bin/env python3
'''Given an array of intervals representing 'N'appointments, find out if a person can attend 
all the appointments.

Question Clarification
`find out if a person can ATTEND ALL APPOINTMENTS` - meaning find out or determine if there are
no OVERLAPPING intervals or APPOINTMENTS OR determine if ALL the intervals or APPOINTMENTS are
MUTUALLY EXCLUSIVE.
-the words `find out` or `determine` means your algorithm has to return true or false.

Pattern: Merge Intervals 
Approach:
-The problem follows the Merge Intervals pattern. We can sort all the intervals by start time 
and then check if any 2 intervals overlap.
-A person will not be able to attend ALL APPOINTMENTS if any 2 appointments overlap.
-` if (intervals[i].start < intervals[i - 1].end)` `intervals[i]` represents the interval that we
are currently standing in and the `intervals[i - 1]` represents the immediate previous interval
from the one currently standing in ie its previous neighbor. Now that the intervals are sorted
and are in Ascending order of start time, for any 2 intervals to be Mutually exclusive, the
start time of the interval we are currently standing in `intervals[i].start` has to be >= the
end time of the previous neighbor of the interval we're currently standing in which is 
`intervals[i - 1].end`.That is, for any 2 intervals to be Mutually exclusive,
`intervals[i].start >= intervals[i - 1].end` Otherwise, if the above condition is false, it means
`intervals[i].start < intervals[i - 1].end` and this means the 2 intervals OVERLAP.Therefore,
we return false. If this condition `if (intervals[i].start < intervals[i - 1].end)` is false,
then we will move on to the next inteval `intervals[i + 1]`(this will be the new interval in 
which we will be stand in) and `intervals[i]` will be the previous neighbor of this new interval
we will be standing in `intervals[i + 1]`.

please note the comparison above, it is "<" and not "<=" while merging we needed "<=" 
comparison, as we will be merging the 2 intervals having condition "intervals[i].start == 
intervals[i - 1].end" but such intervals don't represent conflicting appointments as one starts 
right after the other.

-When the loop exits, we would've reached the end of the list of intervals and compared the last
one with its immediate previous neighbor and found that they're Mutually Exclusive, thus, when
the loop exits, we have to written `True` which will mean, all intervals in the list are
non-overlapping or are Mutually Exclusive, therefore the person can attend all Appointments
'''
class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end

class ConflictingAppointments:
    '''Overlapping Intervals Class'''
    @staticmethod
    def canAttendAllAppointments(intervals):
        '''Determines if a person can attend
        ALL Appointmnets
        Args:
            interval - list of intervals not in any sorting order
        '''
        #sort the intervals by start time
        intervals.sort(key=lambda x: x.start)

        #find any overlapping appointment
        for i in range(1, len(intervals)):
            if (intervals[i].start < intervals[i - 1].end):
                return False
        return True

#Testing
if __name__ == "__main__":
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    result = ConflictingAppointments.canAttendAllAppointments(intervals)
    print("Can attend all appointments: ", result)

    intervals = [Interval(6, 7), Interval(2, 4), Interval(8, 12)]
    result = ConflictingAppointments.canAttendAllAppointments(intervals)
    print("\nCan attend all appointments: ", result)

    intervals = [Interval(4, 5), Interval(2, 3), Interval(3, 6)]
    result = ConflictingAppointments.canAttendAllAppointments(intervals)
    print("\nCan attend all appointments: ", result)

    intervals = [Interval(1, 4), Interval(4, 8), Interval(9, 12)]
    result = ConflictingAppointments.canAttendAllAppointments(intervals)
    print("\nCan attend all appointments: ", result)

'''Time Complexity: O(N*logN), where N is the total number of intervals or appointments.
Though we are iterating the intervals only once, the algorithm will take O(N*logN) since we 
need to sort them in the beginning
Space Complexity: O(N), which we need for sorting.
'''



#!/usr/bin/python3
'''Given a list of appointments, find all the conflicting appointments.

Question Clarification:
-`find all the conflicting appointments` - means find (and return) all the overlapping
appointments or intervals

Pattern: Merge Interval
Similarities: Conflicting Appointments

Approach
-We can sort all the intervals by start time & then check if any 2 intervals overlap
-If they do, we return these Overlapping Intervals or appointments
'''
class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end

class ConflictingAppointments:
    '''Overlapping Intervals'''
    @staticmethod
    def OverlappingAppointments(intervals):
        '''Finds and returns the overlapping or
        conflicting appointments
        '''
        #Firstly, sort the intervals in ascending order of start time
        intervals.sort(key=lambda x: x.start)

        result = []
        #find and return the overlapping intervals or appointments
        for i in range(1, len(intervals)):
            if (intervals[i].start < intervals[i - 1].end):
                result.append(Interval(intervals[i - 1].start, intervals[i -1].end))
                result.append(Interval(intervals[i].start, intervals[i].end))
        return result

#Testing
if __name__ == "__main__":
    intervals = [Interval(4,5), Interval(2,3), Interval(3,6), Interval(5,7), Interval(7,8)]
    for interval in ConflictingAppointments.OverlappingAppointments(intervals):
        print(f"[{interval.start}, {interval.end}]", end=" ")
'''Time Complexity and Space Complexity same as Conflicting Appointments.py'''
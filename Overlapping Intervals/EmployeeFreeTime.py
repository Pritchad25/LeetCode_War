#!/usr/bin/env python3
from heapq import *
'''For 'K'employees, we are given a list of intervals representing the working hours of each 
employee. Our goal is to find out if there is a free interval that is common to all employees.You
can assume that each list of employee working hours is sorted on the start time.

Question Clarification:
-`a free interval that is common to all employees` - lets take the following list of intervals of
employee working hours [[[1,3], [9,12]], [[2,4]], [[6,8]]]. This list shows intervals of working
hours of 3 employees. Employee 2 starts work at hour 2 and ends work at hour 4; this means from
hour 4 going upwards, this employee is free(they are not at work). Employee 3 starts work at hour 
6 and ends work at hour 8; this means from the hours prior to & leading UP TO hour 6 and the 
hours from hour 8 going upwards, this employee is free. Employee 1 is free from Hour 3 UP TO hour 
9. The free interval COMMON TO ALL EMPLOYEES is [4, 6] and [8, 9]

Approach:
Using a Min-Heap to Sort the Intervals
-We should utilize the fact that each employee list is individually sorted!
1. We will take the first interval of each employee and insert it in a Min Heap.This Min Heap can
always give us the interval with the smallest start time.
2. Once we have the interval with the smallest start time, we can then compare it with the next
interval with the smallest start time (which we will also take from the Min-Heap) to find the gap.
The gap will only occur when the 2 intervals are COMPLETELY & TOTALLY MUTUALLY EXCLUSIVE. So if
the 2 intervals are COMPLETELY & TOTALLY MUTUALLY EXCLUSIVE, then we calculate the gap, which
is a free interval COMMON between the 2 employees
3. Whenever we take an interval of a certain employee out of the Min Heap, we can insert the next
interval of the SAME employee into the Min Heap.This also means that we need to know which 
interval belongs to which employee.

`def __lt__(self, other) return self.start < other.start` - min-heap is a heap where the smallest
element is at the top of the heap.The`__lt__` is a special magic method used in the priority
queue (heapq) to determine the order of the Interval objects.It emulates the behaviour of the <
operator, so it means, `less than`. This `self.start < other.start` means that an Interval 
object with a smaller start time will be considered less than an Interval object with a larger 
start time, and thus the Interval object with the smallest start time will be at the top of the 
heap.

-`if not schedule:`- this line `if schedule` reads like,'if schedule is not empty, then do this';
if we put the `not` logical operator, the `not` means negation or opposite, so this line 
`if not schedule` would read like, 'if schedule is empty'.

-`for i, employee_schedule in enumerate(schedule):` -
enumerate is used to loop over `schedule` which is our iterable. `enumerate(schedule)` provides 
2 values on each iteration of the loop: 
1) `i` is the index (or counter) of the current iteration ie it is the index of this current 
employee `employee_schedule`, which `employee_schedule` we are currently standing in within 
`schedule`
2) `employee_schedule` is the value from`schedule` at the current index ie it is the actual
employee SCHEDULE
The function `enumerate` is particularly useful when we need access to both the index and the 
value at that index while looping through a list.

-`if employee_schedule:` checks if the current `employee_schedule` is not empty,that is, if there
is an actual schedule (WORKING HOURS) of an employee. In Python, an empty list is considered 
false. If its there, then we add `employee_schedule[0]` which is the first interval of this 
current employee `employee_schedule` or working hours, which `employee_schedule` we're currently 
standing in, `i` the index of this employee's schedule `employee_schedule` so that we know which 
employee this first interval belongs to(so the index `i` acts like a location of 
`employee_schedule`) and `0` a counter indicating that the first interval from the 
`employee_schedule` which we are currently standing in, is being added to the Min-heap.

-`previous_interval = min_heap[0][0]` - here, we are accessing the first element of the tuple 
which is the top of the heap, which is the Interval object or interval with the smallest start
time and assigning that interval to `previous_interval`.So, this variable now holds the interval
with the smallest start time.The first item in a min-heap is the smallest item and this item is
at the top of the min-heap and is by default at index 0.

-`interval, emp_index, interval_index = heappop(min_heap)` - Here, we conjure the Pythonic power 
of Tuple Unpacking, by unpacking the tuple that is at the top of the min-heap. We assign the
interval in this tuple to `interval`, the index or location of the `employee_schedule` TO WHICH
this interval in the tuple belongs, to `emp_index` and the counter that indicates that the first
interval (which is the interval in this tuple) from an `employee_schedule` was added to the 
Min-heap, to `interval_index` 

-`if len(schedule[emp_index]) > interval_index + 1:` that is, if the length of this current
employee `employee_schedule`(number of intervals associated with this current employee) is > the
actual count/actual number of the first interval of this current employee `employee_schedule`
(WHICH WILL ALWAYS BE 1), which in short, is actually saying, if the length of this current 
employee `employee_schedule` is > 1, then do this.We used `emp_index` here 
`len(schedule[emp_index])` because it is keeping track of the location or index of this current 
employee `employee_schedule`. So, if that is true, then we perform the following lines:
-`next_interval = schedule[emp_index][interval_index + 1]` - store the next interval of this 
current employee `employee_schedule` to the variable `next_interval`
-`heappush(min_heap, (next_interval, emp_index, interval_index + 1))` - we then add this 
`next_interval`, the current or the same `emp_index` (because we still in the current or the
same `employee_schedule`) & `interval_index + 1` as the counter that NOW indicates that the
second interval from the `employee_schedule` which we are currently standing in, has been added 
to the Min-heap, to the min heap.

-`if previous_interval.end < interval.start:` this line means if the 2 intervals(the one with the
smallest time `previous_interval` and the immediate next one with the next smallest start time 
`interval`) are COMPLETELY & TOTALLY MUTUALLY EXCLUSIVE, then add or store the gap between them
which is a free interval COMMON between the 2 employees. The gap or free interval is 
`previous_interval.end` and `interval.start` and it should be an interval, hence what we append
is `Interval(previous_interval.end, interval.start)`

-`previous_interval = interval` here we make this immediate next one with the next smallest start 
time `interval`, the new `previous_interval` meaning we making it (`interval`) the interval
with the smallest start which interval we are going to compare to the immediate next one with the 
next smallest start time in the Min-heap, IN THE NEXT ITERATION of the while loop.

-`[i.__dict__ for i in result]` - result is an array of Interval objects; so here we're output
each the dictionary representation of each Interval object and put these dictionary 
representations in a list.
'''
class Interval:
    '''Defines an Interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    # Less than operator for priority queue(heapq), based on employee's start time
    def __lt__(self, other):
        return self.start < other.start

class EmployeeFreeTime:
    @staticmethod
    def find_employee_free_time(schedule):
        if not schedule:
            return []
        
        result = []
        min_heap = []

        # Insert the first interval of each employee to the queue
        for i, employee_schedule in enumerate(schedule):
            if employee_schedule:
                heappush(min_heap, (employee_schedule[0], i, 0))

        previous_interval = min_heap[0][0]

        while min_heap:
            interval, emp_index, interval_index = heappop(min_heap)

            # If previous_interval is not overlapping with the next interval, insert a free interval
            if previous_interval.end < interval.start:
                result.append(Interval(previous_interval.end, interval.start))
                previous_interval = interval
            else:
                #meaning theyre Overlapping intervals, so update the previous_interval if needed
                if previous_interval.end < interval.end:
                    previous_interval = interval

            # If there are more intervals available for the same employee, add their next interval
            if len(schedule[emp_index]) > interval_index + 1:
                next_interval = schedule[emp_index][interval_index + 1]
                heappush(min_heap, (next_interval, emp_index, interval_index + 1))

        return [i.__dict__ for i in result]

# Example usage:
schedule = [
    [Interval(1, 3), Interval(5, 6)],
    [Interval(2, 3), Interval(6, 8)]
]
print(EmployeeFreeTime.find_employee_free_time(schedule))

schedule = [
    [Interval(1, 3), Interval(9, 12)], 
    [Interval(2, 4)],
    [Interval(6, 8)]
]
print(EmployeeFreeTime.find_employee_free_time(schedule))

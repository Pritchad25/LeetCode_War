#!/usr/bin/env python3

from heapq import *
'''Given a list of intervals representing the start and end time of 'N' meetings, find the 
minimum number of rooms required to hold all the meetings.

Question Clarification
`minimum number of rooms`- the smallest number of rooms
`hold all the meetings` - 2 meetings can use the same room, ie, meeting m1 can use room r1
and when m1 ends, meeting m2 can use r1 since r1 is now free, as long as meeting m1 & m2 are
Mutually Exclusive
Example:
-[[4,5], [2,3], [2,4], [3,5]] - As we can clearly see, some meetings are mutually exclusive.
[2,3] and [3,5] do not OVERLAP and can happen in 1 room. [2,4] and [4,5] do not OVERLAP and can
happen in 1 room. So, to solve our problem, we need to keep track of the MUTUAL EXCLUSIVENESS of 
the OVERLAPPING meetings.

Strategy:
1. We will sort the meetings based on start time.
2. We will schedule the first meeting (let's call it m1) in 1 room(let's call it r1).
3. If the next meeting m2 isn't overlapping with m1,we can safely schedule it in the same room(r1)
4. If the next meeting m3 is overlapping with m2, then we can't use r1.So, we will schedule 
it in another room (let's call it r2)
5. Now if the next meeting m4 is overlapping with m3, we need to see if the room r1 has become 
free. In order to see if room r1 is free, we need to keep track of the end time of the meeting 
happening in it(which is meeting m2).If the end time of m2 is before the start time of m4
(m2.end <= m4.start) we can use that room r1 otherwise((else) meaning m2.end > m4.start ), we 
need to schedule m4 in another room r3
- We can conclude that we need to keep track of the ending time of all the meetings currently 
happening so that when we try to schedule a new meeting, we can see what meetings have already 
ended (meaning, when we try to schedule a new meeting `n`, we need to find a meeting `m` whose end
time <= the start time of meeting `n` which we are trying to schedule, which means we need to 
find a meeting `m` which TRULY & GENUINELY DOESNT OVERLAP with meeting `n` which we are trying 
to schedule).We need to put this information in a data structure that can easily give us the 
SMALLEST ENDING TIME of a meeting OUT OF ALL the N meetings we have and this data structure 
is a Min Heap.

Approach
1. Sort all the meetings on their start time.(our meetings would now be in ascending order of 
start time).
2. Create a Min-Heap to STORE all the active meetings. This Min-Heap will also be used to FIND 
the ACTIVE MEETING with the SMALLEST END TIME.
3. Iterate through all the meetings one by one to ADD or STORE them in the min-heap. Let's say 
we are trying to schedule the meeting m1.
4. Since the min-heap contains all the active meetings, so before scheduling m1, we can remove 
all meetings from the heap that have ended before m1, ie, remove all meetings from the heap that 
have an end time <= to the start time of m1(ie remove ALL meetings that TRULY & GENUINELY DO NOT 
OVERLAP with meeting m1 or are MUTUALLY EXCLUSIVE to meeting m1). Another way of saying this or 
putting this is, we want to remove all meetings from the heap where the start time of m1 >= end 
time of all those meetings(because this also means ALL meetings TRULY & GENUINELY DO NOT 
OVERLAP with meeting m1 or are MUTUALLY EXCLUSIVE to meeting m1))
5. Now ADD or STORE meeting m1 to the Min-Heap. (because we said Min-Heap will store ALL ACTIVE 
MEETINGS, ie all meetings that are OVERLAPPING with the one which we are currently standing in,
which we want to add or store in to our Min-Heap). This means that at ANY time or at every 
iteration of the outer for loop, Min-Heap is holding the MAXIMUM or HIGHEST Number of Active
meetings.
6. The heap will ALWAYS have all the OVERLAPPING MEETINGS, so we will need rooms for ALL OF THEM(
ie ALL THE OVERLAPPING MEETINGS, which are our ACTIVE MEETINGS).So, we will keep a counter to 
remember the maximum size of the heap at any time(meaning for every iteration of outer for loop) 
which will be the MINIMUM NUMBER OF ROOMS needed.
-`!minHeap.empty() ` that is, if the Min-Heap is not empty 
-`meeting.start >= minHeap.top().end` that is, the start time of this meeting we are currently
standing on `meeting` is >= the end time of a meeting in the Min-Heap which is ontop, we want to
remove that meeting from the Min-Heap.Now, because we want to remove all such meetings from the
Min-Heap, we will automate this removal using a while loop hence
while (!minHeap.empty() && meeting.start >= minHeap.top().end)
When the loop exits, in the Min-Heap, we would have meetings that ARE NOT mutually exclusive 
to `meeting` which is the meeting which we are currently standing on, which we want to schedule, 
meaning we would have meetings that OVERLAP with `meeting`.
-`minRooms = max(minRooms, (int)minHeap.size())` - `minRooms` keeps track of the minimum number 
of rooms to hold all meetings. When we reach this step in our algorithm, Min-Heap ONLY has
OVERLAPPING meetings, which are our ACTIVE MEETINGS, so we will need rooms for ALL of these
ACTIVE MEETINGS. So, to get the SMALLEST number of rooms to hold ALL these ACTIVE MEETINGS, for
each iteration of the outer FOR loop, we will use `minRooms` to remember the MAXIMUM size of the
heap (ie minRooms = max(minRooms, (int)minHeap.size()))and this will be the MINIMUM NUMBER OF
ROOMS needed.

-step 3 clarity - `Iterate through all the meetings one by one` this is the outer For loop
-then we remove all the meetings in the Min-Heap that are Mutually Exclusive to the one
we are currently standing in, which we are trying to schedule.We then add the one we are 
currently standing in, which we are trying to schedule to the Min Heap.After removing all 
those other meetings and adding the one we are currently standing in, in the Min-Heap, we are 
only left with meetings that Overlap with the one we are currently standing in, which we are 
trying to schedule and all of these ARE OUR ACTIVE MEETINGS, so we need rooms for all of them.
Then we determine the minimum number of rooms needed as explained in the previous step.
-min-heap is a heap where the smallest element is at the top of the heap.The first item in a 
min-heap is the smallest item and this item isat the top of the min-heap and is by default at 
index 0.
'''
class Meeting:
    '''Defines a meeting'''
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        #Less than operator for priority queue, based on meeting end time
        return self.end < other.end
    
class MinimumMeetingRooms:
    '''Minimum Meeting Rooms'''
    @staticmethod
    def findMinimumMeetingRooms(meetings):
        '''Finds the minimum meeting rooms required
        to hold all meetings
        '''
        if not meetings:
            return 0
        
        #sort the meetings by start time
        meetings.sort(key=lambda x: x.start)

        minRooms = 0 #keeps track of the minimum number of rooms to hold all meetings
        min_heap = []
        for meeting in meetings:
            #Remove all meetings that have ended
            while min_heap and meeting.start >= min_heap[0].end:
                heappop(min_heap)
            # Add the current meeting into min_heap
            heappush(min_heap, meeting)
            # All active meetings are in min_heap, so we need rooms for all of them
            minRooms = max(minRooms, len(min_heap))
        return minRooms

#Testing
if __name__ == "__main__":
    input = [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
    result = MinimumMeetingRooms.findMinimumMeetingRooms(input)
    print("Minimum meeting rooms required: ", result)

    input = [Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]
    result = MinimumMeetingRooms.findMinimumMeetingRooms(input)
    print("\nMinimum meeting rooms required: ", result)

    input = [Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]
    result = MinimumMeetingRooms.findMinimumMeetingRooms(input)
    print("\nMinimum meeting rooms required: ", result)

    input = [Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]
    result = MinimumMeetingRooms.findMinimumMeetingRooms(input)
    print("\nMinimum meeting rooms required: ", result)

'''The __lt__ is one of the special magic methods in Python which stands for "less than".You can
define it in your Python Classes. These special magic methods allow you to emulate the behavior 
of built-in types.
The __lt__ method is used to compare two Interval objects. When you use the < operator between 2
Interval objects, Python will call this method. This method returns True if the end time of the 
current Interval object(self.end) is less than the end time of the other Interval object. This is 
used in the priority queue (heapq) to determine the order of the Interval objects. The Interval 
object with the smallest end time will be considered the smallest and will be at the top of the 
heap.
'''
'''Time Complexity: O(NlogN), where N is the total number of meetings. This is due to the 
sorting that we did in the beginning. Also, while iterating the meetings we might need to poll
or offer meeting to the priority queue. Each of these operations can take O(logN), so overally,
our algorithm will take O(NlogN).
Space Complexity: O(N) which is required for sorting. Also, in the worst case scenario, we'll 
have to insert all the meetings into the Min-Heap (when ALL MEETINGS OVERLAP) which will also 
take O(N) space, so overally our algorithm will take O(N)
'''

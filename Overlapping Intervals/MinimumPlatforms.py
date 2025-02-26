#!/usr/bin/env python3

from heapq import *
'''Given a list of intervals representing the arrival and departure times of trains to a train 
station, our goal is to find the minimum number of platforms required for the train station so 
that no train has to wait.

Question Clarification:
-`list of intervals representing the arrival and departure times of trains` - an example of this
list can be this one: [[4,5], [2,3], [2,4], [3,5]]
-`the minimum number of platforms` - the smallest number of platforms
-`no train has to wait` - 2 trains can use the same platform ie, train t1 can use platform p1
and when t1 leaves the station, train t2 can use p1 since p1 is now free, as long as train t1 
& t2 are Mutually Exclusive(ie, as long as they dont have any OVERLAPPING timeslots)

Approach
1. Sort all the trains on their arrival time.(our trains would now be in ascending order of 
arrival time).
2. Create a Min-Heap to STORE all the ACTIVE/OVERLAPPING trains. This Min-Heap will also be used 
to FIND the ACTIVE TRAIN with the SMALLEST departure TIME.
3. Iterate through all the trains one by one to ADD or STORE them in the min-heap. Let's say 
we are trying to schedule the arrival of TRAIN t1 at a platform.
4. Since the min-heap contains all the ACTIVE/OVERLAPPING trains, so before scheduling t1, we 
can remove all trains from the heap that have left before the arrival of train t1, ie, remove all 
trains from the heap that have a departure time <= to the arrival time of t1(ie remove ALL trains 
that TRULY & GENUINELY DO NOT OVERLAP with TRAIN t1 or are MUTUALLY EXCLUSIVE to TRAIN t1).
Another way of saying this or putting this is, we want to remove all trains from the heap where 
the arrival time of t1 >= departure time of all those other trains(because this also means ALL 
trains TRULY & GENUINELY DO NOT OVERLAP with TRAIN t1 or are MUTUALLY EXCLUSIVE to TRAIN t1))
5. Now ADD or STORE TRAIN t1 to the Min-Heap. (because we said Min-Heap will store ALL ACTIVE 
trains)
6. The heap will ALWAYS have all the OVERLAPPING trains(trains that have OVERLAPPING arrival &
departure times), so we will need platforms for ALL OF THEM(ie ALL THE OVERLAPPING trains, which 
are our ACTIVE trains).So, we will keep a counter to remember the maximum size of the heap at 
any time(ie for every iteration of the outer for loop) which will be the MINIMUM NUMBER OF 
platforms needed.
-we will need platforms for all these OVERLAPPING trains because according to question `no train
has to wait`, so each of these OVERLAPPING trains has to have a platform of their so no one train
has to wait for the other train, which some how it has found at a platform, still loading 
passengers.

-`minHeap[0].end` - this is the interval at the top of the Min Heap
-`train.arrival >= minHeap[0].end` that is, the arrival time of this train we are currently
standing on `train` is >= the end time of a train in the Min-Heap which is ontop, we want to
remove that train from the Min-Heap.Now, because we want to remove all such trains from the
Min-Heap, we will automate this removal using a while loop hence
while (trains and train.arrival >= min_heap[0].end)
-When the loop exits, in the Min-Heap, we would have trains that ARE NOT mutually exclusive 
to `train` which is the train which we are currently standing on, which we want to schedule, 
meaning we would have trains that OVERLAP with `train`.
-`minPlatforms = max(minPlatforms, (int)minHeap.size())` - `minPlatforms` keeps track of the 
minimum number of platforms to hold all trains. When we reach this step in our algorithm, Min-Heap 
ONLY has OVERLAPPING trains, which are our ACTIVE trains, so we will need platforms for ALL of 
these ACTIVE trains. So, to get the SMALLEST number of platforms to hold ALL these ACTIVE trains, 
for each iteration of the outer FOR loop, we will use `minPlatforms` to remember the MAXIMUM size 
of the heap (ie minPlatforms = max(minPlatforms, (int)minHeap.size()))and this will be the 
MINIMUM NUMBER OF platforms needed.
'''

class Trains:
    '''Defines a train & initializes it with
    its arrival and departure times.
    '''
    def __init__(self, arrival, departure):
        self.arrival = arrival
        self.departure = departure
    
    def __lt__(self, other):
        #Less than operator for priority queue, based on meeting end time
        return self.departure < other.departure

class MinimumPlatforms:
    '''Minimum Platforms'''
    @staticmethod
    def findMinimumPlatforms(trains):
        '''Finds the minimum number of platforms for the
        train station so that no train has to wait

        Args:
            trains - the list of arrival & departure times of 
            different trains
        '''
        if not trains:
            return 0
        
        #Sort the trains in ascending order of their arrival times
        trains.sort(key=lambda x: x.arrival)

        minPlatforms = 0 #keeps track of the minimum number of platforms needed
        min_heap = []
        for train in trains:
            #Remove all trains that have left before arrival of `train`
            while (min_heap and train.arrival >= min_heap[0].departure):
                heappop(min_heap)
            #Add current `train` to the heap
            heappush(min_heap, train)
            # All active trains are in the min_heap, so we need platforms for all of them
            minPlatforms = max(minPlatforms, len(min_heap))
        return minPlatforms

#Testing
if __name__ == "__main__":
    input = [Trains(4, 5), Trains(2, 3), Trains(2, 4), Trains(3, 5)]
    result = MinimumPlatforms.findMinimumPlatforms(input)
    print("Minimum train platforms required: ", result)

    input = [Trains(1, 4), Trains(2, 5), Trains(7, 9)]
    result = MinimumPlatforms.findMinimumPlatforms(input)
    print("\nMinimum train platforms required: ", result)

    input = [Trains(6, 7), Trains(2, 4), Trains(8, 12)]
    result = MinimumPlatforms.findMinimumPlatforms(input)
    print("\nMinimum train platforms required: ", result)

    input = [Trains(1, 4), Trains(2, 3), Trains(3, 6)]
    result = MinimumPlatforms.findMinimumPlatforms(input)
    print("\nMinimum train platforms required: ", result)
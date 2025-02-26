#!/usr/bin/env python3
from heapq import *
'''We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is
running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the 
same machine.

Question Clarification
-`Each job has a Start time, an End time, and a CPU load when it is running` - the start time of 
of that job, end time of that job & the CPU load it takes when it is running RESPECTIVELY.
-`CPU load when it is running` - the amount of CPU space it uses when the job is running.
- `the maximum CPU load` - the HIGHEST CPU load time
-`maximum CPU load at any time if all the jobs are running on the same machine.` - we have 2 
possible scenarios in which the maximum/highest CPU load occurs IF ALL THE JOBS ARE RUNNING ON
THE SAME MACHINE; 1) when 2 jobs OVERLAP, the maximum CPU load occurs within the actual OVERLAP 
interval, and we get this maximum CPU load by adding the CPU loads of the 2 OVERLAPPING jobs.
2) when there are no OVERLAPPING jobs, ie, when all job are MUTUALLY EXCLUSIVE; in this case, it
means all jobs are going to run and finish 1 after the other INDIVIDUALLY in the same machine,
meaning the maximum CPU load is the highest CPU load of any job within the list of jobs.

Pattern: Merge Intervals
Similarities: Minimum Meeting Rooms
Approach:
-The problem follows the Merge Intervals Pattern and can easily be converted to Minimum Meeting 
Rooms.
-Similar to 'Minimum Meeting Rooms' where we were trying to find the maximum or Highest number of
meetings happening at any time(Highest number of ACTIVE meetings happening at every iteration of
outer for loop), for 'Maximum CPU Load' we need to find the maximum number of jobs running at any 
time (meaning we need to find the HIGHEST number of jobs running at every iteration of the outer
for loop, ACTIVE jobs that is). We will need to keep a running count of the maximum CPU load at 
any time to find the overall maximum load.
-`maxCPULoad` - keep track of the highest or maximum CPU load at ANY TIME(meaning for every 
iteration of outer for-loop). At every iteration of the for-loop, we always have running jobs or
ACTIVE jobs in the Min-Heap meaning at every iteration of the for-loop, Min-Heap is holding the 
MAXIMUM or HIGHEST Number of Active jobs and their total CPU load, is the maximum or HIGHEST so 
far, therefore, we will keep track of this total in this variable `maxCPULoad`
-`currentCPULoad` - keeps track of the total CPULoad currently present in the Min-Heap for the
ACTIVE or running jobs. When we remove a job(s) in the Min-heap that COMPLETELY DOES NOT OVERLAP 
with the one we're currently standing in (which we want put inside the Min-Heap), we have to 
adjust this variable as well by removing the CPU load(s) of this job(s) we're removing from the 
Min-Heap through decrementing this variable. I say job(s) because they can be 1 up to many jobs 
that need to be removed,so to automate this removal, we use a while loop. After adding the job 
we're currently standing in into the Min-Heap, we have to increment this variable with the job's 
CPU load, as a way of keeping track of the total CPU load of the jobs that are running or are 
ACTIVE which are in the Min-Heap.
-`job.start > minHeap.top().end` - that is, if the job which we're currently standing in `job`
COMPLETELY & TOTALLY DOES NOT OVERLAP with the job at the top of the Min-Heap, then remove this
(minHeap.top().end) job's CPU load from the total CPU load (currentCPULoad) of the jobs that are 
currently running or from the ACTIVE jobs which are in the Min-Heap and then remove this 
(minHeap.top().end) job from the Min-Heap. They are COMPLETELY & TOTALLY Mutually Exclusive.
'''
class Job:
    '''Defines a Job'''
    def __init__(self, start, end, cpuLoad):
        self.start = start
        self.end = end
        self.cpuLoad = cpuLoad
    
    def __gt__(self, other):
        #Greater than operator for priority queue(heapq), based on job end time
        return self.end > other.end

class MaximumCPULoad:
    '''Maximum CPU Load'''
    @staticmethod
    def findMaxCPULoad(jobs):
        '''Finds the maximum CPU Load at any time if 
        all the jobs are running on the same machine.
        '''
        if not jobs:
            return 0
        
        # Sort the jobs in ascending order of start time
        jobs.sort(key=lambda x: x.start)

        maxCPULoad = 0 # keeps track of the maximum CPU load at any time
        currentCPULoad = 0 # keeps track of the total CPU load amongst the ACTIVE jobs
        min_heap = [] 
        # Iterate through the jobs 1 at a time
        for job in jobs:
            # Remove jobs that have ended
            while (min_heap and job.start > min_heap[0].end):
                currentCPULoad -= min_heap[0].cpuLoad
                heappop(min_heap)
            #add the current job to our Min Heap of active jobs
            heappush(min_heap, job)
            currentCPULoad += job.cpuLoad
            maxCPULoad = max(maxCPULoad, currentCPULoad)
        return maxCPULoad

#Testing
if __name__ == "__main__":
    input = [Job(1, 4, 3), Job(7, 9, 6), Job(2, 5, 4)]
    result = MaximumCPULoad.findMaxCPULoad(input)
    print("Maximum CPU load at any time: ", result)

    input = [Job(6, 7, 10), Job(8, 12, 15), Job(2, 4, 11)]
    result = MaximumCPULoad.findMaxCPULoad(input)
    print("\nMaximum CPU load at any time: ", result)

    input = [Job(1, 4, 2), Job(3, 6, 5), Job(2, 4, 1)]
    result = MaximumCPULoad.findMaxCPULoad(input)
    print("\nMaximum CPU load at any time: ", result)
'''Time Complexity: O(NlogN) where N is the total number of jobs. This is due to the sorting that
we did in the beginning. Also, while iterating the jobs, we might need to poll/offer jobs to the 
priority queue. Each of these operations can take O(logN).Overall our algorithm will take O(NlogN)
Space Complexity: O(N), which is required for sorting. Also, in the worst case, we have to insert 
all the jobs into the priority queue (when all jobs overlap) which will also take O(N) space. The
overall space complexity of our algorithm is O(N)
'''

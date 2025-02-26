#!/usr/bin/python3
'''Given two lists of intervals, find the intersection of these two lists. Each list consists of 
disjoint intervals sorted on their start time.

`intersection of these two lists`- this means you should return a list of common intervals 
between the two lists.
`disjoint intervals` means the intervals in both lists are MUTUALLY EXCLUSIVE
Pattern: Merge Intervals

Approach:
-As we have discussed under Insert Interval, there are 5 overlapping possibilities between two 
intervals 'a' & 'b'
-A close observation will tell us that whenever the 2 intervals overlap, one of the interval's 
start time lies within the other interval. This rule can help us identify if any 2 intervals 
overlap or not.
-Now, if we have found that the 2 intervals overlap, how can we find the overlapped part?
-Again from the above diagram(in question), the overlapping interval(the overlapped part) will 
be equal to:
start = max(a.start, b.start)
end = min(a.end, b.end) That is, the highest start time and the lowest end time will be the
OVERLAPPING PART or the overlapping interval

1. So our algorithm will be to iterate through both the lists together to see if any 2 intervals 
overlap
2. If 2 intervals overlap, we will insert the OVERLAPPED part into a result list and 
3. move on to the next interval which is finishing early.

-`i < arr1.size() && j < arr2.size()` loop will run from for the first element(first interval) of
the both lists to the last element(last interval). The loop will exit when we've reached the end
of ANY the lists.
-`if ((arr1[i].start >= arr2[j].start && arr1[i].start <= arr2[j].end) ||
          (arr2[j].start >= arr1[i].start && arr2[j].start <= arr1[i].end))`
for our 4 cases of overlapping intervals, the 4 can be divided into 2 main types which are
demonstrated in notebook and also in the propositions of the above if statement. The 1st type
is represented by the proposition `arr1[i].start >= arr2[j].start`(check notebook for a
visual representation). In this type, we firstly check if the start time of interval `arr[i]`
`arr1[i].start` lies within the interval `arr2[j]` and the proposition is 
`arr1[i].start >= arr2[j].start`; we also check if the 2 intervals overlap and the proposition 
is `arr1[i].start <= arr2[j].end)`.If both these propositions are true, then both of these 
intervals intersect and so we have to add the OVERLAPPED part to our list of OVERLAPPED parts.

The 2nd type is represented by the proposition `arr2[j].start >= arr1[i].start`.In this type also
we firstly check if the start time of interval `arr2[j]` `arr2[j].start` lies within the interval 
`arr1[i]`and the proposition is `arr2[j].start >= arr1[i].start`;we also check if the 2 intervals 
overlap and the proposition is `arr2[j].start <= arr1[i].end`.If both these propositions are true, then both of these 
intervals intersect and so we have to add the OVERLAPPED part to our list of OVERLAPPED parts.

Either one of the type's propositions(plural meaning both of them) have to be true in order for
us to add the OVERLAPPED part to our list of OVERLAPPED parts, hence the use of the OR `||` 
logical operator
-` if (arr1[i].end < arr2[j].end)` After we have put the overlapped part into the list of 
overlapped parts, we have to move on to the next interval in the list of the one which is 
finishing early between the 2 intervals that we are currently standing on on both lists
arr1 and arr2. We doing this so that we compare the interval which didnt finish early on the 1 
list, (which interval we are still standing on) with the "new" interval of the other list.See
notebook for clarification
'''
class Interval:
    '''Defines an interval'''
    def __init__(self, start, end):
        self.start = start
        self.end = end

class IntervalsIntersection:
    @staticmethod
    def merge(intervals1, intervals2):
        '''Finds the intersection of 2 lists of
        Mutually Exclusive intervals
        
        Args:
            intervals1 - a list of Mutually Exclusive intervals
            intervals2 - another list of Mutually Exclsuive intervals
        '''
        result = [] # will hold the Overlapped parts
        i = 0 #variable that'll help us loop through intervals1
        j = 0 #variable that'll help us loop through intervals2
        while (i < len(intervals1) and j < len(intervals2)):
            #check if the intervals1[i] intersects with intervals2[j]
            #check if one of the interval's start time lies within the other interval
            if ((intervals1[i].start >= intervals2[j].start and intervals1[i].start <= intervals2[j].end) or 
                (intervals2[j].start >= intervals1[i].start and intervals2[j].start <= intervals1[i].end)):
                #store the intersection part
                Overlapped_start = max(intervals1[i].start, intervals2[j].start)
                Overlapped_end = min(intervals1[i].end, intervals2[j].end)
                result.append(Interval(Overlapped_start, Overlapped_end))
            # move next from the interval which is finishing first
            if (intervals1[i].end < intervals2[j].end):
                i += 1
            else:
                j += 1
        return result

#Testing
if __name__ == "__main__":
    input1 = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
    input2 = [Interval(2, 3), Interval(5, 7)]
    result = IntervalsIntersection.merge(input1, input2)
    print("Intervals Intersection: ", end=" ")
    for interval in result:
        print(f"[{interval.start}, {interval.end}]", end=" ")
    
    input3 = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
    input4 = [Interval(5, 10)]
    result = IntervalsIntersection.merge(input3, input4)
    print("\nIntervals Intersection: ", end=" ")
    for interval in result:
        print(f"[{interval.start}, {interval.end}]", end=" ")

'''Time Complexity: O(M + N), where M and N are the total number of intervals in the input 
arrays respectively. 
Space Complexity: O(1), Ignoring the space needed for the result list, the algorithm runs in 
constant space
'''
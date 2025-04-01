#!/usr/bin/python3
'''Given the head of a LinkedList with a cycle, find the length of the cycle.

Similarities: LinkedListCycle
Approach:
1. We can firstly find the cycle in the LinkedList.
2. Once the fast and slow pointers meet, we can save the slow pointer 
and iterate the whole cycle with another pointer until we see the slow 
pointer again to find the length of the cycle.
'''
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListCycle:
    @staticmethod
    def hasCycle(head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:# found the cycle
                return LinkedListCycle.calculateLength(slow) #saving `slow` and using another method
                #`calculateLength` to iterate the whole cycle with another pointer `current` that
                # starts where slow is to calculate the length of cycle until we see or reach
                # the slow pointer again
        return 0 #linkedlist doesnt have a cycle so length of non existent cycle is 0
    
    @staticmethod
    def calculateLength(slow):
        current = slow #uCurrent uqalisela ku Slow esimSevileyo in the above method
        cycleLength = 0
        while True: #the loop should only run if current != slow. So, while that condition is
            # True, do this below.
            current = current.next #we counting the pointers. So this line says`move to the next 
            #pointer and count this pointer that youre now standing in.`
            cycleLength += 1#count this pointer that youre now standing in
            if current == slow: #ie, if our loop condition has become false,break out of the loop,
                #where `current == slow` means we've reached the point where we started to calculate
                #our length, which point is `slow`.
                break
        return cycleLength


'''Time Complexity: O(N)
Space Complexity: O(1)
'''

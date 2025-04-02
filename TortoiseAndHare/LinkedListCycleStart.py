#!/usr/bin/python3
'''Given the head of a Singly LinkedList that contains a cycle, write a function 
to find the starting node of the cycle.

Pattern: LinkedList Cycle
Similarities: LinkedList Cycle
Approach:
-If we know the length of the LinkedList cycle, we can find the start of the cycle through 
the following steps:
1. Take two pointers. Let's call them pointer1 & pointer2.
2. Initialize both pointers to point to the start of the LinkedList.
3. We can find the length of the LinkedList cycle using the approach discussed in
LinkedList Cycle. Let's assume that the length of the cycle is K nodes.
4. Move pointer2 ahead by K nodes.
5. Now, keep incrementing both pointers pointer1 & pointer 2 UNTIL they both meet.
6. As pointer2 is K nodes ahead of pointer1, when both pointers meet, pointer2 must have 
completed one loop IN THE CYCLE or will have completed one loop IN THE CYCLE. Their meeting point 
will be the start of the cycle. So we will return pointer1
'''
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListCycleStart:
    @staticmethod
    def findCycleStart(head):
        cycleLength = 0
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleLength = LinkedListCycleStart.calculateCycleLength(slow)
                break

        return LinkedListCycleStart.findStart(head, cycleLength)

    @staticmethod
    def calculateCycleLength(slow):
        current = slow
        cycleLength = 0
        while True:
            current = current.next
            cycleLength += 1
            if current == slow:
                break

        return cycleLength

    @staticmethod
    def findStart(head, cycleLength):
        pointer1 = head
        pointer2 = head
        while cycleLength > 0:
            pointer2 = pointer2.next
            cycleLength -= 1

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: ", LinkedListCycleStart.findCycleStart(head).value)

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: ", LinkedListCycleStart.findCycleStart(head).value)

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: ", LinkedListCycleStart.findCycleStart(head).value)



''' Time Complexity:
As we know, finding the cycle in a LinkedList with N nodes and also finding the length of the 
cycle requires O(N). Also, as we saw in the above algorithm, we will need O(N) to find the start 
of the cycle. Therefore, the overall time complexity of our algorithm will be O(N).
Space Complexity: O(1)
'''

#!/usr/bin/python3
'''Given the head of a Singly LinkedList, write a function to determine if the LinkedList has 
a cycle in it or not.

Approach
-Imagine we have a slow and a fast pointer to traverse the LinkedList. In each iteration, the 
slow pointer moves one step and the fast pointer moves two steps. This gives us two conclusions:
1. If the LinkedList doesn't have a cycle in it, the fast pointer will reach the end of the 
LinkedList(ie it will be pointing to the Null pointer which in essence means it will be a Null 
pointer) before the slow pointer to reveal that there is no cycle in the LinkedList.
2. The slow pointer will never be able to catch up to the fast pointer if there is no cycle in 
the LinkedList meaning the fast pointer will ALWAYS be ahead of the slow pointer.
-If the LinkedList has a cycle, the fast pointer enters the cycle first, followed by the slow 
pointer. After this, both pointers will keep moving in the cycle INFINITELY. If at any stage 
both of these pointers meet, we can conclude that the LinkedList has a cycle in it.
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
            fast = fast.next.next #enters the cycle first & will keep moving twice as quick as slow
            slow = slow.next #enters the cycle second
            if slow == fast: #ie, the two pointers have met; they are pointing to the same value.
                #meaning the LinkedList has a cycle.
                return True  #found the cycle
            #otherwise, both pointers will keep moving in the cycle INFINITELY till they meet 
        return False #the two pointer didnt meet; slow pointer wasnt able to catch up to fast
        #or fast reached the end of the LinkedList

#Testing
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print("LinkedList has cycle: " + str(LinkedListCycle.hasCycle(head)))#will return False coz
    #fast reached the end of the LinkedList first; slow pointer wasnt able to catch up

    head.next.next.next.next.next.next = head.next.next #next pointer of last node(the node with
    #value 6) is set to point to the third node (the node with value 3), in essence, this is us
    #creating a cycle in a LinkedList
    print("LinkedList has cycle: " + str(LinkedListCycle.hasCycle(head)))

    head.next.next.next.next.next.next = head.next.next.next#next pointer of last node(the node with
    #value 6) is set to point to the fourth node (the node with value 4), in essence, this is us
    #creating a cycle in a LinkedList
    print("LinkedList has cycle: " + str(LinkedListCycle.hasCycle(head)))
'''Time Complexity:
O(N), where N is the number of nodes in the Linked List
Space Complexity:
O(1), Algorithm runs in constant space
'''

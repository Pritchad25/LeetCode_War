#!/usr/bin/python3
'''Given the head of a Singly LinkedList, write a method to return the
middle node of the LinkedList. If the total number of nodes in the LinkedList 
is even, return the second middle node.

Approach:
-We can use the Fast & Slow pointers method such that the fast pointer is always twice the nodes 
ahead of the slow pointer.
-This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be 
pointing at the middle node.
'''
class ListNode:
    '''Defines a LinkedList Node'''
    def __init__(self, value):
        self.value = value
        self.next = None
    
class MiddleOfLinkedList:
    '''finds the middle of the Linked List Node'''
    @staticmethod
    def findMiddle(head):
        '''helps find the middle node of a linked list'''
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

#Testing
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Middle Node: ", MiddleOfLinkedList.findMiddle(head).value)

    head.next.next.next.next.next = ListNode(6)
    print("Middle Node: ", MiddleOfLinkedList.findMiddle(head).value)

    head.next.next.next.next.next.next = ListNode(7)
    print("Middle Node: ", MiddleOfLinkedList.findMiddle(head).value)
'''Time Complexity: O(N), where N is the number of nodes in the Linked List
Space Complexity: O(1)
'''

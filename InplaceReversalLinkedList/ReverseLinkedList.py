#!/usr/bin/env python3
'''Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the 
new head of the reversed LinkedList.

Pattern: In-PlaceLinkedListReversal

Approach
-To reverse a LinkedList, we need to reverse one node at a time.
-We will start with a variable `current` which will initially point to the head of the LinkedList 
and a variable `previous` which will point to the previous node that we have processed; initially
`previous` will point to `null`.
-In a stepwise manner, we will reverse the `current` node by pointing it to the `previous` before 
moving on to the next node. Also, we will update the `previous` to always point to the previous 
node that we have processed. 

The summary of the core steps of our algorithm is:
-store the next node - `next = current.next`,
-reverse the node that we're currently standing on - `current.next = previous`,
-point `previous` to this current node that we just reversed (or just processed) as
the `previous` node - `current = previous`, 
-then move on to the next node `current = next`.
'''
class ListNode:
    '''Defines a node of a
    Singly Linked List
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class ReverseLinkedList:
    '''Singly Linked List Reversal
    '''
    @staticmethod
    def reverse(head):
        '''Reverses a Singly Linked
        List In-Place
        
        Args:
            head - pointer to the start of the
            Linked List.
        '''
        current = head #current node that we're processing
        previous = None # previous node that we have processed

        while (current is not None):
            next_node = current.next #temporarily store the next node
            current.next = previous # reverse this node that we're currently standing on
            previous = current #point `previous` to this node we're currently standing on,
            #that we just reversed or that we just processed.
            current = next_node # move on to the next node
        #when the loop exits, `current` will be pointing to null & `previous` will be the new head.
        return previous # the new `head` or head node

# Testing
if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)

    result = ReverseLinkedList.reverse(head)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end = " ")
        result = result.next
    
'''Time Complexity: O(N) where N is the total number of nodes in the LinkedList.
Space Complexity: O(1), we only used constant space.
'''
    
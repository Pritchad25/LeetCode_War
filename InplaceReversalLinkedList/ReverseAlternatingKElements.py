#!/usr/bin/env python3
'''Given the head of a LinkedList and a number k, reverse every alternating `K` sized sub-list 
starting from the head.
If, in the end, you are left with a sub-list with < 'K' elements, reverse it too.

Pattern: In-Place LinkedList Reversal
Similarities: Reverse every K-element Sub-list. 

- The only difference is that we have to skip 'K' alternating elements. We can follow a similar 
approach, and in each iteration after reversing 'K' elements, we will skip the next 'K'
elements.
-`previous = current` in the loop that skips the 'K' nodes, this line has the exact same 
description as this line  `previous = lastNodeOfSubList` of `ReverseEveryKElements, ie prepare 
for the next sublist's reversal by keeping track of `current` as the previous node for the next 
sublist that is going to be reversed.
'''
class Node:
    '''Defines a Node of a
    Singly Linked List
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class ReverseAlternatingKElements:
    '''Linked List reversal'''
    @staticmethod
    def reverse(head, k):
        ''''Reverses Alternating K elements'''
        if (k <= 1 or not head):
            return head
        
        current = head
        previous = None

        while(True):
            lastNodeOfPreviousPart = previous
            # after reversing the linkedlist, `current` will become the last node of the sub-list
            lastNodeOfSubList = current
            next = None # will be used to temporarily store the next node
            # reverse 'k' nodes

            i = 0
            while (current and i < k):
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
            
            # connect with the previous part
            if (lastNodeOfPreviousPart):
                lastNodeOfPreviousPart.next = previous #previous is now the first of the sublist
            else: 
                head = previous
            
            #connect with the next part
            lastNodeOfSubList.next = current

            # skip 'k' nodes
            i = 0
            while (current and i < k):
                previous = current
                current = current.next
                i += 1
            
            if not current: #break out of loop if we've reached end of linked list
                break
        
        return head

# Testing
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    result = ReverseAlternatingKElements.reverse(head, 2)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end=" ")
        result = result.next
'''Time Complexity: O(N)
Space Complexity: O(1)
'''
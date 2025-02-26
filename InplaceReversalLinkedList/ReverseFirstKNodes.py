#!/usr/bin/env python3
'''Given the head of a LinkedList, reverse the first 'k' elements.

Pattern: In-Place Reversal Of A Linked List
Similarities: Very Similar to ReverseSubList

Approach:
-This problem can be easily converted to ReverseSubList - to reverse the first 'k' elements, we 
need to pass p=1, q=k
-then we follow the exact process of ReverseSubList to solve the problem.

1. Traverse the linked list until the k-th node or the qth node
2. Break the linked list into 2 parts: the first k nodes and the remaining nodes.
3. Reverse the first part of the linked list.
4. Join both parts of the linked list.

`we are interested at the part at index 'p'`, ie we are interested at the node that is 
standing at position p=1, because we want to use it later to connect to the rest of the 
Linkedlist. When the loop below exits, this node (which is pointed to by `head` as `head` never
changes to another node in this algorithm) is at the end of the reversed SUBLIST, having its
`next` pointer pointing to None but we dont want that; we want to join this reversed part with 
the rest of the linked list, so we use this `head` node by assigning the K + 1 node to 
its(`head` node) `next` pointer hence, `head.next = current` and then we return `previous` as 
the NOW head of the linkedlist.

-`we are interested at the part between 'p=1' and 'K' because thats the part we want to reverse
and then reconnect back to the Linkedlist after reversing.

-`we are interested at the part after index K or position K` ie we are interested at the node 
that is standing at position K + 1, because we want to use it later to connect the reversed 
sublist to the rest of the Linkedlist. When the loop below exits, `current` is pointing to
this node at position K + 1 hence we connect the reversed part to the rest of the linkedlist
using this node (`current`), thus `head.next = current` as explained above.


-`i < k` - this `k` is the ACTUAL number of nodes in the Linkedlist that we want to reverse; i is
a counter that is going to ensure we reverse the ACTUAL number of nodes in the Linkedlist we want
to reverse, which is k nodes.So, the loop is going to run, WHILE, we havent reversed K nodes 
BECAUSE it means we have reversed less than K nodes.When the loop exits, we will have reversed 
the ACTUAL number of nodes we want to reverse, which is K nodes and `previous` will be pointing 
to the start of the reversed part or start of the reversed sublist AND this start is now the
head of the linkedlist, so in essence, `previous` is now the head of the linkedlist. 
'''
class ListNode:
    '''Defines a LinkedList Node.
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class ReverseFirstKNodes:
    '''LinkedList Reversal.'''
    @staticmethod
    def reverse(head, k):
        '''reverses the first k nodes of
        a singly linked list.
        '''
        if not head or k <= 1:
            return head #return the linked list as it is
        
        # Traverse the Linked list and reverse the nodes while traversing
        # until we reach the kth node
        current = head
        previous = None
        i = 0

        while (current and i < k):
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        # Connect the reversed part with the rest of the LinkedList
        head.next = current

        return previous

#Testing
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result = ReverseFirstKNodes.reverse(head, 3)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end=" ")
        result = result.next
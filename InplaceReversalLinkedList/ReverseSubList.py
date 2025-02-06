#!/usr/bin/env python3
'''Given the head of a LinkedList and 2 positions `p` & `q` reverse the LinkedList from position
p to position q.

Problem Clarification:
Say we are given the following linked list: head->1->2->3->4->5->Null, p = 2, q = 4,
so we are supposed to reverse this part 2->3->4

Pattern: In-Place Linked List Reversal
Approach:
-We can use a similar approach as discussed in `ReverseLinkedList`. Here are the steps we need 
to follow:
1. Skip the first `p - 1` nodes to reach the node at position p or at the pth position.
2. Remember the node at position `p - 1` to be used later to connect with the reversed sublist.
3. Next, reverse the nodes from p to q using the same approach discussed in `ReverseLinkedList`.
4. Connect the `p - 1` and `q + 1` nodes to the reversed sub-list, ie, connect the node at 
position `p - 1` and the node at position `q + 1` to the reversed sub-list

-`if (p == q): return head` - return the Singly Linked list as it is, because there's nothing
to reverse.
- `previous = current`, ie, keep track of this current node that we're standing on as one that 
we have processed(that is, as one that we have skipped) by assigning it to `previous`, 
`current = current.next` then move on to the next node. When the loop exits, it means we are 
now standing on the node at position p, ie `current` will be standing at or pointing to the 
`pth` node or the node at the position p.
-`i < p - 1` - we want to skip 'p - 1' nodes, starting from the head node.So, the loop is going
to run while i is < THE NUMBER OF NODES that we want to skip.When the loop exits, it means we
have skipped THE NUMBER OF NODES that we want to skip AND we are now standing at the pth node or
at the node at position p, ie these 2 events are not MUTUALLY EXCLUSIVE.So, if the current value
of i < THE NUMBER OF NODES that we want to skip, it means we havent skipped THE NUMBER OF NODES 
that we want to skip yet, so we need to keep looping.
-`we are interested at the part before index 'p'`, ie we are interested at the node that is 
standing at position p - 1, because we want to use it later to connect with the reversed sublist.
When the first loop above exits, `previous` is standing at this node or is pointing to this node,
so we have to keep track of this node or store/SAVE `previous` by assigning it to a variable 
hence `lastNodeOfFirstPart = previous`
-`we are interested at the part between 'p' and 'q' because thats the part we want to reverse
and then reconnect back to the Linkedlist after reversing.
-`we are interested at the part after index q` ie we are interested at the node that is standing
at position q + 1, because we want to use it later to connect with the reversed sublist so we 
have to keep track of this node; we know that, after reversing the LinkedList, `current` (which,
at this STAGE in our algorithm, is currently standing on or pointing to the `pth` node or the 
node at position p) will become the last node of the SUB-LIST, so we will store
or SAVE `current` by assigning it to a variable hence, `lastNodeOfSubList = current`
-`i < q - p + 1` - this `q - p + 1` is the ACTUAL number of nodes in the sublist that we want to
reverse; i is a counter that is going to ensure we reverse the ACTUAL number of nodes in the
sublist.so the loop is going to run, WHILE, we havent reversed the ACTUAL number of nodes in the
sublist BECAUSE it means we have reversed a less number of nodes in the sublist than we want.When
the loop exits, we will have reversed the ACTUAL number of nodes in the sublist and `previous` 
will be pointing to the start of the reversed sub list.
-`lastNodeOfFirstPart->next = previous` -ie when the 2nd loop exits, `previous` is pointing to 
the first node of the reversed sublist. So, we connect this reversed sublist to the first part
-`lastNodeOfSubList->next = current` - ie when the 2nd loop exits, `current` is pointing to the 
last node of the linkedlist. 
'''
class ListNode:
    '''Defines a node of a
    Singly Linked List
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class ReverseSubList:
    '''Reversed Sublist'''
    @staticmethod
    def reverse(head, p, q):
        if (p == q):
            return head # return the Singly Linked List as it is
        
        # after skipping 'p - 1' nodes, current will point to the 'p'th node
        current = head
        previous = None
        i = 0
        while (current and i < p - 1):
            previous = current
            current = current.next
            i += 1
        
        # we are interested in 3 parts of the LinkedList, part before
        #index 'p', part between 'p' and 'q' and the part after index 'q'
        lastNodeOfFirstPart = previous # points to the node at index 'p - 1'

        # after reversing the LinkedList 'current' will become the last node of the sub-list
        lastNodeOfSubList = current
        next = None # will be used to temporarily store the next node

        # reverse nodes between 'p' and 'q'
        i = 0
        while (current and i < q - p + 1):
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        
        # connect with the first part
        if (lastNodeOfFirstPart):
            lastNodeOfFirstPart.next = previous # 'previous' is now the first node of the sub list
        else: # meaning p == 1, ie we are changing the first node (head) of the LinkedList
            head = previous

        # connect with the last part
        lastNodeOfSubList.next = current

        return head

# Testing
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result = ReverseSubList.reverse(head, 2, 4)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end=" ")
        result = result.next
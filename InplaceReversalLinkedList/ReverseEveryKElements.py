#!/usr/bin/env python3
'''Given the head of a LinkedList and a number K, reverse every K sized sub-list starting from 
the head. If, in the end, you are left with a sub-list with less than K elements, reverse it too.

Pattern: In-Place LinkedList Reversal
Similarities: Reverse a Sub-List

- The only difference is that we have to reverse all the sub-lists. We can use the same approach,
starting with the first sub-list, (ie, p=1, q=k) and keep reversing all the sublists of size K.
-Most of the code is the same as `ReverseSublist`, with a few majority changes.

-`if (k <= 1 or not head)`, ie if k is 1 or less(we cant reverse every 1 sized sublist, coz an 
element is NOT a sublist) or the list is empty, then return the list as it is.

-`if (lastNodeOfPreviousPart):
    lastNodeOfPreviousPart.next = previous
  else:
    head = previous`
In the above conditional control structure, we are connecting the reversed sublist with the 
previous part.If `lastNodeOfPreviousPart` (which keeps track of or stores the node pointed to by
`previous`) is NOT NULL, then it means `lastNodeOfPreviousPart` is pointing to an actual node, so
we assign to the `next` pointer of  `lastNodeOfPreviousPart` the reversed sublist which is 
pointed to by `previous` when the inner while loop exits (previous will be pointing to the start
of the reversed sublist). Otherwise(the else part), we make the start of the reversed sublist
the new head node(this else part is executed once on the first iteration of the outer while loop,
then in further iterations, the if part is the one executed.)

-`lastNodeOfSublist.next = current` in this part we are connecting the reversed sublist to the
start of the next sublist that needs to be reversed.`lastNodeOfSublist` keeps track of the last
node of the reversed sublist. So, we assign to the `next` pointer of `lastNodeOfSublist` the
start of the next sublist that needs to be reversed(which is pointed to by `current`)
-`previous = lastNodeOfSubList` ie prepare for the next sublist's reversal by keeping track of
`lastNodeOfSubList` as the previous node for the next sublist that is going to be reversed.
'''

class Node:
    '''Defines a Node of a Singly Linked List.
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class ReverseEveryKElements:
    '''Reversal of a Linked List'''
    @staticmethod
    def reverse(head, k):
        '''Reverses every K elements of a
        Singly Linked List.
        
        Args:
            head - the start of the Linked List
            k - the number of nodes to iteratively reverse.
        '''
        # Base Case: if k is 1 or less or list is empty
        if (k <= 1 or not head):
            return head
        
        current = head
        previous = None

        while(True):
            lastNodeOfPreviousPart = previous
            # after reversing the LinkedList `current` will become the last node of the sublist
            lastNodeOfSubList = current
            next = None # will be used to temporarily store the next node
            
            # reverse `K` nodes
            i = 0
            while (current and i < k):
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
            
            # Connect with the previous part
            if (lastNodeOfPreviousPart):
                lastNodeOfPreviousPart.next = previous # `previous` is now the first node of the sublist
            else:
                head = previous
            
            # Connect with the next part
            lastNodeOfSubList.next = current

            if current is None: # break, if we've reached the end of the LinkedList
                break

            # prepare for the next sublist
            previous = lastNodeOfSubList
        
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

    result = ReverseEveryKElements.reverse(head, 3)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end=" ")
        result = result.next

'''Time Complexity: O(N)
Space Complexity: O(1), we only used constant space.
'''

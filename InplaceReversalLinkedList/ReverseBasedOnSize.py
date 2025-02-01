#!/usr/bin/env python3
'''Given a LinkedList with 'n' nodes, reverse it based on its size in the following way:
    1. If 'n' is even, reverse the list in a group of n/2 nodes.
    2. If n is odd, keep the middle node as it is, reverse the first 'n/2' nodes and reverse 
    the last 'n/2' nodes.

Pattern: InPlaceLinkedListReversal
Similarities: ReverseSubList

Approach:
-When 'n' is even we can perform the following steps:
1. Reverse first 'n/2' nodes: head = reverse(head, 1, n/2), so, this will be implemented 
similarly to `ReverseFirstKNodes`
2. Reverse last 'n/2' nodes: head = reverse(head, n/2 + 1, n),ie reverse from position p=n/2 + 1, to
q = n(the end of linked list)  

-When 'n' is odd, our algorithm will look like:
1. Reverse first 'n/2' nodes: head = reverse(head, 1, n/2) so, this will be implemented 
similarly to `ReverseFirstKNodes`
2. Reverse the last 'n/2' nodes: head = reverse(head, n/2 + 2, n), ie reverse from position 
p=n/2 + 2, to q = n(the end of linked list). Its `n/2 + 2` because we are skipping the middle
node also (which is standing at position `n2 + 1`), keeping it where it is.

==========================='n' IS EVEN =======================================
-`if not skipMiddle:
    head.next = ReverseSubList.reverseSizeBy2Util(curr, k, False)`
 ie if we shouldnt skip the middle node, then reverse the next block too.
In the case 'n' is even, when the loop in `reverseSizeBy2Util` exits in its first iteration, 
`curr` is pointing to the start of the next SUBLIST that we should reverse, ie, `curr` is 
pointing to the node at position `k + 1`; so,to reverse this next SUBLIST, we just pass the 
current position of `curr`, the current value of k(coz we still reverse the same number of 
nodes like in the first iteration) and the current of value of `skipMiddle` which is False(coz we 
still not skipping the middle node even in this second iteration and FURTHER iterations).

-When the loop in `reverseSizeBy2Util` exits in its 1st iteration, the node pointed to by `head` 
never changes to another node and is NOW at the end of the reversed SUBLIST, having its
`next` pointer pointing to None but we dont want that; we want to use this node to join to the
next SUBLIST after reversing it, hence the line 
`head.next = ReverseSubList.reverseSizeBy2Util(curr, k, False)`. Note that in the previous
paragraph, I said, `FURTHER iterations` because this method `reverseSizeBy2Util` uses the classic
programming construct, called RECURSION, see notes on how Recursion occurs in this case of n
being even.
============================'n' IS ODD =========================================
-`else:
    head.next = curr
    if curr:
        curr.next = ReverseSubList.reverseSizeBy2Util(curr.next, k, True)
`the else part of `reverseSizeBy2Util` means we should skip the middle node, which insinuates 
that our 'n' (the size of our linkedlist) is odd.When the loop in `reverseSizeBy2Util` exits in 
its first iteration, the node pointed to by `head` never changes to another node and is NOW at 
the end of the first reversed SUBLIST, having its `next` pointer pointing to None but we dont 
want that; we want to use this node to join to the middle node(which we should skip), hence the 
line `head.next = curr`. When the loop in `reverseSizeBy2Util` exits in its first iteration also,
`curr` is pointing to the middle node that we should skip.If the middle node(`curr`) is not None,
we want to use this middle nodeto join to the next SUBLIST after reversing it, hence the lines:
`if curr:
        curr.next = ReverseSubList.reverseSizeBy2Util(curr.next, k, True)`
to reverse this next SUBLIST, we just pass the next element after the middle element(ie, we pass 
`curr.next`), the current value of k(coz we still reverse the same number of nodes like in the 
first iteration) and the current of value of `skipMiddle` which is True(coz we are still skipping
the middle node even in this second iteration and FURTHER iterations).Note that in the previous
paragraph, I said, `FURTHER iterations` because this method `reverseSizeBy2Util` uses the classic
programming construct, called RECURSION, see notes on how Recursion occurs in this case of n
being odd.
'''
class Node:
    '''Defines a Node of a Linked List
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class ReverseSubList:
    '''Reverse the Singly Linked List
    according to its size.
    '''
    @staticmethod
    def reverseBySize(head): 

        # Get the size of list. 
        n = ReverseSubList.getSize(head) 

        # If the size is even, no need to skip middle Node. 
        if n % 2 == 0: 
            return ReverseSubList.reverseSizeBy2Util(head, n//2, False) 

        # If size is odd, the middle node has to be skipped. 
        else:
            return ReverseSubList.reverseSizeBy2Util(head, n//2, True)     
    # Returns size of the Singly linked list.
    @staticmethod
    def getSize(head):
        '''Returns the size of the LinkedList
        '''
        curr = head 
        count = 0
        while curr: 
            curr = curr.next
            count += 1
        
        return count 
    
    @staticmethod
    def reverseSizeBy2Util(head, k, skipMiddle): 
        # Base case: if list is empty
        if not head:
            return None

        count = 0
        curr, prev = head, None
        
        # Reverse current block of list. ie, reverse the first k nodes
        while curr and count < k:
            next = curr.next
            curr.next = prev 
            prev = curr 
            curr = next
            count += 1
        
        # If size is even, reverse next block too. 
        if not skipMiddle: 
            head.next = ReverseSubList.reverseSizeBy2Util(curr, k, False) 

        else:

            # if size is odd, skip next element and reverse the block after that. 
            head.next = curr
            if curr: 
                curr.next = ReverseSubList.reverseSizeBy2Util(curr.next, k, True) 
        
        return prev 

# Testing
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    result = ReverseSubList.reverseBySize(head)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end=" ")
        result = result.next
'''Problem is similar to Reverse a linkedlist in group of size k
Time Complexity: O(N + k), where N is number of nodes in the Linked List.The algorithm traverses
the linked list once to compute its size (which takes O(n) time, where n is the number of nodes).
After that, it reverses the first k nodes (where k is the size divided by 2) using a helper 
function.The helper function also reverses a portion of the list, which takes O(k) time.
Overall, the time complexity is O(n + k), which is asymptotically equivalent to O(N).
Space Complexity: O(1), The algorithm uses a constant amount of extra space, for variables like
`curr`, `prev` and `count`. It does not create any additional data structures or allocate memory
dynamically.'''
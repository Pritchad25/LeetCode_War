#!/usr/bin/env python3
'''Given the head of a Singly LinkedList and a number K, rotate the LinkedList to the right by 
K nodes.

Approach:
- Another way of defining the rotation is to take the sub-list of K ending nodes of the 
LinkedList and connect them to the beginning. Other than that we have to do 3 more things:

1. Connect the last node of the LinkedList to the head, because the list will have a different 
tail after the rotation.
2. The new head of the LinkedList will be the node at the beginning of the sublist.
3. The node right before the start of sub-list will be the new tail of the rotated LinkedList.

-`if (head == None or head->next == None or rotations <= 0){ return head } ie if the list is 
empty or theres only 1 element in the list or the number of rotations to be are 0 or less, return
the Linked list as it is.
-`#find the length and the last node of the list`, the steps of the loop reads as follows: while
next is not Null, store the next, then count it.While next is not Null, store the next, then 
count it.When the loop exits, `lastNode` is pointing to the last node and the actual length of 
the list has been found.
-`lastNode.next = head` connect the last node with the head to make it a circular list.We're
doing this because the list will have a different tail after the rotation.
-`rotations %= listLength` we are calculating the ACTUAL number of rotations that we are supposed
to do using modulo. This statement can be rewritten as rotations = rotations % listLength. Modulo
will also ensure we dont do rotations more than the length of the list.
-`skipLength = listLength - rotations` determining the number of nodes we would have to skip, 
before getting to the start of the sublist which will be our new head
-`lastNodeOfRotatedList = head` the current `head` node will be the last node of rotated list,
so here we storing in said variable

-In the loop for skipping, we say `skipLength - 1` because we've already kept track of one of the 
nodes that we were supposed to skip in this line `lastNodeOfRotatedList = head`.Doing this will
allow us to skip the required number of nodes(skipLength).When the loop exits, 
'lastNodeOfRotatedList.next' is pointing to the start of the sub-list of 'k' ending nodes.So we
make this start (lastNodeOfRotatedList.next) the new head hence the line 
head = lastNodeOfRotatedList.next; also, when the loop exits, `lastNodeOfRotatedList` is pointing 
to the new tail/last node of the linkedlist, so we ensure that it is the tail by assigning Null 
to its next pointer hence the line `lastNodeOfRotatedList.next = Null`
'''
class Node:
    '''Defines a Singly Linked List Node'''
    def __init__(self, value):
        self.value = value
        self.next = None

class RotateList:
    '''Defines a Rotated Linked List'''
    @staticmethod
    def reverse(head, rotations):
        '''Rotates a Linked list K nodes
        to the right.
        
        Args:
            head - the start of the list to be rotated
            k - the number of nodes to rotate the linked list
            to the right by
        '''
        # Base Cases
        if not head or not head.next or rotations <= 0:
            return head
        
        #find the length of the list and also the last node of list
        lastNode = head
        listLength = 1
        while (lastNode.next):
            lastNode = lastNode.next
            listLength += 1
        
        lastNode.next = head #connect the lastNode with the head to make a circular list
        rotations %= listLength
        skipLength = listLength - rotations
        lastNodeOfRotatedList = head
        i = 0
        while (i < skipLength - 1):
            lastNodeOfRotatedList = lastNodeOfRotatedList.next
            i += 1
        
        # lastNodeOfRotatedList.next is pointing to the sublist of 'K' ending nodes
        head = lastNodeOfRotatedList.next
        lastNodeOfRotatedList.next = None
        return head

#Testing
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    result = RotateList.reverse(head, 3)
    print("Nodes of the reversed LinkedList are: ", end=" ")
    while (result):
        print(result.value, end=" ")
        result = result.next
'''Time Complexity: O(N)
Space Complexity: O(1)'''
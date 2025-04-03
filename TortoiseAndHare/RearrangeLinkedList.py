#!/usr/bin/python3
'''Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the 
nodes from the second half of the LinkedList are inserted alternately to the nodes from the 
first half in reverse order.
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should 
return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
Your algorithm should not use any extra space and the input LinkedList should be modified 
in-place.

Question Clarification
-So, if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, inserting the nodes of the
second half of the LinkedList(4 -> 5 -> 6) ALTERNATELY to the nodes from the first half in 
reverse order means we are inserting the nodes of the second half in REVERSE, inter-changing
(Sintshintshanisa) between a node of the first half FIRST and a node of the second half SECONDLY,
which will give us this: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Similarities: Palindromic LinkedList & Middle Of The LinkedList
Approach:
-This problem shares similarities with Palindrome LinkedList.To rearrange the given LinkedList 
we will follow the following steps:
1. We can use the Fast & Slow pointers method similar to MiddleOfTheLinkedList to find the 
middle node of the LinkedList.
2. Once we have the middle of the LinkedList, we will reverse the second half of the LinkedList.
3. Finally, we'll iterate through the first half and the reversed second half to produce a 
LinkedList in the required order.

`while (headFirstHalf != nullptr && headSecondHalf != nullptr)` ie the loop condition becomes 
false when 1 of the propositions becomes false.The steps of this algorithm in the loop reads as
follows:
    *store the pointer to next node of current node we're standing in ON THE ORIGINAL LIST(first half)
    *assign the current node on the Reversed list(secondhalf) as the next node of the current
    node of the OriginalList(first half)
    *make the pointer we stored the new head of the ORIGINAL list(firsthalf)
    
    *store the pointer to next node of current node we're standing in ON THE REVERSED LIST(second half)
    *assign the current node on the ORIGINAL LIST(first half) as the next node of the current node
    of the Reversed list(secondhalf)
    *make the pointer we stored the new head of the Reversed list(secondhalf)
`if (headFirstHalf != nullptr)` ie, we have cases where the loop above this if condition will
run until the end(ie, until it exits) but the modified LinkedList will have no Null pointer
at the end, which Null pointer shouldve been assigned by the `headFirstHalf` variable IDEALLY
or PRESUMABLY at the last iteration of the while loop. 
'''
class ListNode:
    '''Defines a LinkedList Node'''
    def __init__(self, value):
        self.value = value
        self.next = None

class RearrangeList:
    '''Rearranges a LinkedList according to
    above specifications
    '''
    @staticmethod
    def reorder(head):
        '''Method that reorders the linkedlist
        
        Args:
        head - the start or the pointer of a linkedlist
        '''
        #if the linkedlist is empty or has exactly 1 node, then return nothing
        if (head is None or head.next is None):
            return
        
        #find the middle of the LinkedList
        slow = head #the slow pointer
        fast = head #the fast pointer that moves twice as fast as the slow pointer
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        #when above loop exits, slow will pointing to the middle node
        headSecondHalf = RearrangeList.reverse(slow) #reverse the second half
        headFirstHalf = head

        #rearrange to produce the LinkedList in the required order
        while(headFirstHalf is not None and headSecondHalf is not None):
            temp = headFirstHalf.next
            headFirstHalf.next = headSecondHalf
            headFirstHalf = temp

            temp = headSecondHalf.next
            headSecondHalf.next = headFirstHalf
            headSecondHalf = temp
        
        #set the next of the last node to Null
        if (headFirstHalf is not None):
            headFirstHalf.next = None
    
    @staticmethod
    def reverse(head):
        '''Reverses the Second Half of the linkedlist
        Args:
        head - the start of the second half of the linkedlist
        '''
        prev = None
        while(head is not None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

#Testing
if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)
    head.next.next.next.next.next = ListNode(12)
    RearrangeList.reorder(head)
    while (head is not None):
        print(head.value, end=" ")
        head = head.next


'''Time Complexity: O(N), where N is the number of nodes in the LinkedList.
Space Complexity: O(1)
'''

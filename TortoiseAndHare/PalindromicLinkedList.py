#!/usr/bin/python3
'''Given the head of a Singly LinkedList, write a method to check if the LinkedList is a 
palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original 
form once the algorithm is finished.
The algorithm should have O(N) time complexity where 'N' is the number of nodes in the linked
list

Approach:
-a palindrome LinkedList will have nodes values that read the same backward or forward. This
means that if we divide the LinkedList into two halves, the node values of the first half in the 
forward direction should be similar to the node values of the second half in the backward 
direction.
-As we have been given a Singly LinkedList, we can't move in the backward direction.To handle 
this, we will perform the following steps:
1. We can use the Fast & Slow pointers method similar to MiddleOfLinkedList to find the middle 
node of the LinkedList.
2. Once we have the middle of the LinkedList, we will reverse the second half.
3. Then, we will compare the first half with the reversed second half to see if the LinkedList 
represents a palindrome.
4. Finally, we will reverse the second half of the LinkedList again to revert and bring the 
LinkedList back to its original form.

-`if (head is None or head.next is None)` we already know if one or all of the propositions are
true then the if condition is true. The proposition `head is None` mean if the LinkedList is
empty, then it is a Palindromic Linked List and the proposition `head.next is None` mean if
there is only 1 element in our Linked List, then this particular list is also Palindromic.So,
in summary if the linked list is empty or it has only 1 element,then its a Palindromic LinkedList
and hence return True.
-So, if both propositions are false it means there is more than 1 element in the Linked List, so
we proceed with the steps after this if statement
`while (head != nullptr && headSecondHalf != nullptr)` The loop condition becomes false when one
of the propositions becomes false, ie, when one of the head pointers becomes NULL. I think
the first head pointer (head) is the one that becomes NULL as it reaches the end of the first
half of the Linked List before the head of the secondhalf does.
` if (head == nullptr || headSecondHalf == nullptr)` ie if one or all of the head pointers is
NULL, then this LinkedList is a palindromic.
-`headSecondHalf = reverse(slow)`#From MiddleOfLinkedList solution, we know that where slow will 
be pointing when fast reaches the end of the LinkedList that is our middle node. So, we want to 
reverse all nodes from where slow is standing to the last node of the LinkedList.So, use a 
separate function called reverse to do this, passing in the current position of slow as an 
argument to that function. The pointer returned by this function(called prev) will be the head of the Secondhalf, ie, the start of the second half of our linkedList
which is reversed.
-`while (head is not None and headSecondHalf is not None)` ie, the linkedlist must not be empty(
linked list should have more than 1 element) and headSecondHalf is pointing to an actual node; this
is because we are trying to determine if an ACTUAL linkedlist(linkedlist with more than 1 element)
is a palindrome, so all the above propositions have to be true(fulfilled) for the condition to 
be true. 
-`headSecondHalf = PalindromicLinkedList.reverse(slow)` eg if our original list was
2->4->6->4->2->Null. After, applying the reverse function on the above linkedlist, the linked 
list will now look like this:2->4->2->4->6->Null. The pointer `headSecondHalf` will point to 
the third node with value 2 and `copySecondHalf` will hold a copy of `headSecondHalf` for 
reverting back to the original list. The original list now looks like this: 2->4->6->Null because
6 now points to Null and `headSecondHalf` points to ->2->4->6->Null.
-``while (head is not None and headSecondHalf is not None)`` when this loop exits, both pointers
will be pointing to Null and that means the linked list is palindromic. We immediatley reverse
the list back to its original state and then say if either of the head pointers is null or both
are pointing to Null then return true using this if condition `if (head == nullptr || headSecondHalf == nullptr)` otherwise 
return false
'''
class ListNode:
    '''Defines a node of a Linked List'''
    def __init__(self, value):
        self.value = value
        self.next = None

class PalindromicLinkedList:
    '''Determines whether or not a Linked List is Palindromic'''
    @staticmethod
    def isPalindrome(head):
        '''Determines whether or not a Linked List is Palindromic'''
        #if the LinkedList is empty or has only 1 element, it is Palindromic
        if(head is None or head.next is None):
            return True
        
        #find the middle of the LinkedList
        slow = head
        fast = head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        headSecondHalf = PalindromicLinkedList.reverse(slow) #reverse the second half; the return 
        #pointer of reverse is going to be the head pointer of the second half of the linkedlist 
        #or the start of the second half of the linkelist.
        copyHeadSecondHalf = headSecondHalf #store the head of reversed part to revert back to the
        #original linkedlist later

        #compare the first half to the second half
        while (head is not None and headSecondHalf is not None):
            if (head.value != headSecondHalf.value):
                break #not a palindrome
            head = head.next
            headSecondHalf = headSecondHalf.next
        
        PalindromicLinkedList.reverse(copyHeadSecondHalf) #revert the reverse of the second half
        if (head is None or headSecondHalf is None): #if both halves
            return True
        return False
    
    @staticmethod
    def reverse(head):
        '''Reverses the second half of the LinkedList
        for determining if its Palindromic or not
        '''
        prev = None
        while (head is not None):
            next = head.next #store the pointer to next node of current node
            head.next = prev #assign the node we dealt with in the previous iteration(called prev) as the next node of this current node we're standing in
            prev = head #make current node that we're standing in, the previous node of next node we will deal with in next iteration.
            head = next #move on to the next node, whose pointer we stored or saved in first step.
        return prev

#Testing
if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(2)
    print("Is palindrome: ", PalindromicLinkedList.isPalindrome(head))

    head.next.next.next.next.next = ListNode(2)
    print("Is palindrome: ", PalindromicLinkedList.isPalindrome(head))

'''Time Complexity: O(N), where N is the number of nodes in the Linked List
Space Complexity: O(1)
'''

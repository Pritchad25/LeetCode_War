#!/usr/bin/env python3
'''Given a binary tree and a number sequence, find if the sequence is 
present as a root-to-leaf path in the given tree.

Problem Clarificaton:
-`find if` - meaning we're returning true or false.

Pattern:  Binary Tree Path Sum 
Approach:
-We can follow the same DFS approach and additionally, track the element 
of the given sequence that we should match with the current node. Also, we 
can return `false` as soon as we find a mismatch between the sequence and 
the node value.

-`if (sequenceIndex >= len(sequence) or currentNode.val != sequence[sequenceIndex]):`
that is, the above if statement will only be executed if the condition is
true.The condition will be true if one of the propositions is true; if both
propositions are false, the condition will be false.Now, here, we will
return false IF the index `sequenceIndex` is out of range (ie if its equal 
to length of sequence or greater) OR value of node that we're currently
standing on `currentNode.val` IS NOT EQUAL TO the element that is standing
on index `sequenceIndex` sequence[sequenceIndex], ie we found a mismatch 
between the sequence and the node value.
-`if (currentNode.left is None and currentNode.right is None and
        sequenceIndex == sequence.size() - 1)` ie is the node a leaf AND is
        it at the end of a sequence(shown by its index in the sequence
        `sequenceIndex` being equal to length of sequence - 1), is it the 
        last element of sequence?If so, we've found the path so we return
        True
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class PathWithGivenSequence:
    @staticmethod
    def findPath(root, sequence):
        '''finds the path'''
        # Base case: the tree is empty
        if not root:
            return len(sequence) < 0
        return PathWithGivenSequence.findPathRecursive(root, sequence, 0)
    
    @staticmethod
    def findPathRecursive(currentNode, sequence, sequenceIndex):
        if currentNode is None:
            return False
        
        if (sequenceIndex >= len(sequence) or currentNode.value != sequence[sequenceIndex]):
            return False
        
        # if the current node is a leaf AND it is at the end of the sequence, we have found a path!
        if (currentNode.left is None and currentNode.right is None and sequenceIndex == len(sequence) - 1):
            return True
        
        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return PathWithGivenSequence.findPathRecursive(currentNode.left, sequence, sequenceIndex + 1) or PathWithGivenSequence.findPathRecursive(currentNode.right, sequence, sequenceIndex + 1)

# Testing
if __name__ == "__main__":
    root =  TreeNode(1)
    root.left =  TreeNode(0)
    root.right =  TreeNode(1)
    root.left.left =  TreeNode(1)
    root.right.left =  TreeNode(6)
    root.right.right =  TreeNode(5)

    print("Tree has path sequence: ", PathWithGivenSequence.findPath(root, [1, 0, 7]))
    print("Tree has path sequence: ", PathWithGivenSequence.findPath(root, [1, 1, 6]))

'''Time Complexity: O(N), where N is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.
Space Complexity: O(N), in the worst case. This space will be used to store 
the recursion stack. The worst case will happen when the given tree is a 
linked list (i.e., every node has only one child).'''

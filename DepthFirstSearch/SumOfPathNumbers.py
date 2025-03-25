#!/usr/bin/env python3
'''Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. Find the total sum of all 
the numbers represented by all paths.

Problem Clarification:
-`root-to-leaf path will represent a number` - say we have the number 112;
this number represents a root-to-leaf path. So, we are supposed to find the
sum of all the numbers that represent root-to-leaf paths eg 115 + 171 + 96

Pattern: Binary Tree Path Sum problem
Approach:
-We can follow the same DFS approach. The additional thing we need to do is 
to keep track of the number representing the current path.
-How do we calculate the path number for a node? Taking the first example
as shown in problem page, say we are at node 7. As we know, the path number
for this node is 17, which was calculated by: 1 * 10 + 7 => 17.
-We will follow the same approach to calculate the path number of each node.

-To calculate the path number for a node we're currently standing in, we 
multiply the current path number `pathSum` by 10 and then add product to 
the current node's value and finally assign the result to `pathSum` again 
hence the line `pathSum = 10 * pathSum + currentNode.value;`.This new 
`pathSum` will be used to determine the `pathSum` or the path number of 
this current node's children in a recursive manner, see notes for how the 
recursive structure proceeds.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SumOfPathNumbers:
    '''Sums the Root-To-Path Numbers'''
    @staticmethod
    def findSumOfPathNumbers(root):
        '''returns the sum of path numbers'''
        return SumOfPathNumbers.findRootToLeafPathNumbers(root, 0)
    
    @staticmethod
    def findRootToLeafPathNumbers(currentNode, pathSum):
        '''Recursively determines the path numbers'''
        # Base case: the binary tree is empty
        if not currentNode:
            return 0
        
        # calculate the path number of the current node
        pathSum = 10 * pathSum + currentNode.value

        #if the current node is a leaf, return the current path sum
        if (currentNode.left is None and currentNode.right is None):
            return pathSum
        
        # recursively traverse the left and right subtrees
        return SumOfPathNumbers.findRootToLeafPathNumbers(currentNode.left, pathSum) + SumOfPathNumbers.findRootToLeafPathNumbers(currentNode.right, pathSum)

# Testing
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Total Sum of Path Numbers: ", SumOfPathNumbers.findSumOfPathNumbers(root))

'''Time Complexity: O(N), where N is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.
Space Complexity: O(N), in the worst case. This space will be used to store
the recursion stack. The worst case will happen when the given tree is a 
linked list (i.e., every node has only one child).
'''

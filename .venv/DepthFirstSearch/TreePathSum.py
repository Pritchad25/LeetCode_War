#!/usr/bin/env python3
'''Given a binary tree and a number S, find if the tree has a path from root-to-leaf such that 
the sum of all the node values of that path equals S.

`find if` - implies that the algorithm should return true or false.

Approach:
- As we are trying to search for a root-to-leaf path, we can use the Depth First Search (DFS) 
technique to solve this problem.
- To recursively traverse a binary tree in a DFS fashion, we can start from the root and at every
step, make two recursive calls one for the left child and one for the right child.
The following are the steps for our Binary Tree Path Sum problem:
1. Start DFS with the root of the tree.
2. If the current node is not a leaf node && its value != sum, do 2 things:
    i) Subtract the value of the current node from the given number to get a new 
    sum => S = S - node.value
    ii) Make two recursive calls for both the children of the current node with the new number 
    calculated in the previous step.
3. At every step, see if the current node being visited is a leaf node AND if its value is equal 
to the given number S. If both these conditions are true, we have found the required root-to-leaf
path, therefore return `true`.
4. If the current node is a leaf but its value is not equal to the given number S, return false.(
we didnt include this step in our algorithm though.)
-see notes on how the 2 way Recursion Structure of this algorithm proceeds.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreePathSum:
    '''Tree path from root-to-leaf'''
    @staticmethod
    def hasPath(root, sum):
        '''Determines if the tree has a path
        from root-to-leaf such that the sum of all 
        the node values of that path == sum

        Args:
            root - the root node of the tree
            sum - the Sum
        '''
        #Base Case: the binary tree is empty
        if not root:
            return False
        
        # If the current node's value == sum AND is a leaf, we've found the path
        if (root.value == sum and root.left is None and root.right is None):
            return True
        
        # recursively call to traverse the left and right sub-tree
        # return true if EITHER of the two recursive calls return True
        return TreePathSum.hasPath(root.left, sum - root.value) or TreePathSum.hasPath(root.right, sum - root.value)

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: ", TreePathSum.hasPath(root, 23))
    print("Tree has path: ", TreePathSum.hasPath(root, 16))

'''Time Complexity: O(N), where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.

Space Complexity: O(N) in the worst case. This space will be used to store the recursion stack.
The worst case will happen when the given tree is a linked list (i.e., every node has only one 
child).
'''

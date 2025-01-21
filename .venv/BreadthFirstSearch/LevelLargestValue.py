#!/usr/bin/env python3
'''Given a binary tree, populate an array to represent the largest value on each level of a 
binary tree.

Pattern: Binary Tree Level Order Traversal
Approach: the EXACT SAME approach as `LevelAverages`.
-instead of having a running sum we will track the maximum value of each level.So, where there's
`levelSum += currentNode.val`, we put `maxValue = max(maxValue, currentNode.val)` and at the end
we just put `result.append(maxValue)`.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

'''Time Complexity: O(N), where N is the number of nodes in the tree.This is due to the fact that
we traverse each node once.
Space Complexity: O(N), which is required for the queue. Since we can have a maximum of N/2 nodes
at any level (this could happen only at the lowest level), therefore we will need O(N) space to 
store them in the queue.
'''

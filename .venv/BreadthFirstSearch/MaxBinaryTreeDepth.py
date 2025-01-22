#!/usr/bin/env python3
'''Given a binary tree, find its maximum depth (or height).

Pattern: Binary Tree Level Order Traversal
Similarities: MinBinaryTreeDepth

Approach:
-We will follow a similar approach. 
-Instead of returning as soon as we find a leaf node, we will keep traversing for all the levels
until we reach the last level, incrementing `maximumDepth` each time we complete a level or
encounter a level. 
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
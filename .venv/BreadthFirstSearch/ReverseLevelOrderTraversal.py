#!/usr/bin/env python3
from collections import deque
'''Given a binary tree, populate an array to represent its level-by-level traversal in reverse 
order, i.e., the lowest level comes first. You should populate the values of all nodes in each 
level from left to right in separate sub-arrays.

Pattern: Binary Tree Level Order Traversal

Approach:
-We can follow the same BFS approach. The only difference will be that, instead of appending the 
current level at the end, we will append the current level at the beginning of the result list.ie
say we already have a level called x1 in the result(resultList=[x1]) & want to append level `x2`
we append `x2` at the beginning of the `resultList` like this (resultList=[x2, x1]) INSTEAD of
appending it at the end of resultList(like we usually do and like how we did in 
`LevelOrderTraversal` where resultList=[x1, x2]).

-Since we need to append the level array at the beginning of the result list, we will use a 
double-ended queue (deque)
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ReverseLevelOrderTraversal:
    '''ReverseLevelOrderTraversal'''
    @staticmethod
    def traverse(root):
        '''Populates an array to represent the binary
        tree level-by-level traversal in reverse order
        
        Args:
            root - the root node of the tree
        '''
        result = deque()
        # Base Case: The tree is empty
        if not root:
            return result
        
        queue = [root]
        while (queue):
            levelSize = len(queue)
            currentLevel = []

            i = 0
            while (i < levelSize):
                currentNode = queue.pop(0)
                # add the node to the current level
                currentLevel.append(currentNode.value)
                # insert the children of current node to the queue
                if (currentNode.left):
                    queue.append(currentNode.left)
                if (currentNode.right):
                    queue.append(currentNode.right)
                i += 1
            # append the current level at the beginning
            result.appendleft(currentLevel)
        return result

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = ReverseLevelOrderTraversal.traverse(root)

    print("Reverse level order traversal: ")
    for que in result:
        for num in que:
            print(num, end=" ")
        print("")# print an empty line

'''Time Complexity: O(N), where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.
Space Complexity: O(N) as we need to return a list containing the level order traversal. We will 
also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this 
could happen only at the lowest level), therefore we will need O(N) space to store them in the 
queue.
'''
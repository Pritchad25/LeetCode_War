#!/usr/bin/env python3
from collections import deque
'''Given a binary tree, populate an array to represent its level-by-level traversal. You should 
populate the values of all nodes of each level from left to right in separate sub-arrays.

Pattern: Breadth First Search
-Since we need to traverse all nodes of each level before moving onto the next level, we can use
the Breadth First Search (BFS) technique to solve this problem.

Approach:
We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:
1. Start by pushing the `root` node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue(lets call it `levelSize`).We will 
have these many nodes in the current level that we are standing on. 
4. Next, remove `levelSize` nodes from the queue and push their `value` in an array that 
represents the current level that we're standing on.
5. After removing each node from the queue, insert both of its children into the queue.
6. If the queue is not empty, repeat from step 3 for the next level.

-`levelSize` is the number of nodes in the current level that we are standing on.
-`currentNode = queue.front()` we storing the node first before removing it from the queue, so 
that we can push its value to the list of the current level that we are standing on `currentLevel`
and so that we can be able to insert both of its children into the queue.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LevelOrderTraversal:
    '''Level Order Traversal'''
    @staticmethod
    def traverse(root):
        # Base Case: the tree is empty
        result = []
        if not root:
            return result
        
        queue = [root]
        while queue:
            levelSize = len(queue)
            currentLevel = []

            i = 0
            while i < levelSize:
                currentNode = queue.pop(0)
                # add the node to the current level
                currentLevel.append(currentNode.value)
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                i += 1
            result.append(currentLevel)
        return result

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = LevelOrderTraversal.traverse(root)
    print("Level order traversal: ")
    for array in result:
        for num in array:
            print(num, end=" ")
        print()
           
'''Time Complexity: O(N) where N is the total number of nodes in the tree. This is due to the fact
that we traverse each node once.

Space Complexity: O(N), as we need to return a list containing the level order traversal. We will
also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this 
could happen only at the lowest level), therefore we will need O(N) space to store them in the 
queue.
'''
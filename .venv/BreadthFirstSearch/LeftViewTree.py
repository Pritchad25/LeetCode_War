#!/usr/bin/env python3
'''Given a binary tree, return an array containing nodes in its left view.

The left view of a binary tree is the set of nodes visible when the tree is seen from the left 
side.

Approach:
-We will be following a similar approach, but instead of appending the last element of each level
we will be appending the first element of each level to the output array.
-`i == 0` - since we are storing our nodes in a queue, the indexes of a queue start from 0 going 
upwards. We did keep track of the size or the length of the queue in `levelSize`.So,
the first node of the queue or the first node of the level that we're currently standing in, will
stand on index 0.Think of the queue as a list in python; in lists, It is a given 
that the first element of the list will be standing at index 0 of the list. So, i keeps track of
the position or the index of `currentNode` which is the node we pop off the queue.If this 
position or index (i) is == 0, then we standing on the first node of the current level, which 
node is `currentNode`. `currentNode` is where we temporarily store nodes before we pop them off 
from the queue.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LeftViewTree:
    '''Right View of Binary Tree'''
    @staticmethod
    def traverse(root):
        '''Returns an array of nodes in its
        right view
        '''

        result = []
        #Base case: the Binary tree is empty
        if not root:
            return result
        
        queue = [root]
        while (queue):
            levelSize = len(queue)
            for i in range(levelSize):
                currentNode = queue.pop(0)

                # If it is the first node of this level, add it to the array
                if (i == 0):
                    result.append(currentNode)
                
                # insert the children of current node in the queue
                if (currentNode.left):
                    queue.append(currentNode.left)
                if (currentNode.right):
                    queue.append(currentNode.right)
        
        return result

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.left.left = TreeNode(3)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    result = LeftViewTree.traverse(root)
    for node in result:
        print(node.value, end=" ")

'''Time Complexity: O(N), where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.
Space Complexity: The space complexity of the above algorithm will be O(N) as we need to return a
list containing the level order traversal. We will also need O(N) space for the queue. Since we 
can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
therefore we will need O(N) space to store them in the queue.
'''
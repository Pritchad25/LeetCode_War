#!/usr/bin/env python3
'''Given a binary tree and a node, find the level order successor of the given node in the tree.

Problem Clarification
The level order successor is the node that appears right after the given node in the level order
traversal eg if given node has value 3, then its level order successor is node with value 4. If
given node is the root node, then its level order successor is its left child.

Pattern: Binary Tree Level Order Traversal
Approach:

-We can follow the same BFS approach.
-The only difference will be that, we will not keep track of all the levels.Instead, we will 
keep inserting child nodes to the queue. As soon as we find the given node, we will return the 
next node from the queue as the level order successor.
-When we find the given node `key`, ie when `if(currentNode.value == key)` returns true, we will
break out of the while loop, HAVING ALREADY removed or pop'ed out the given node from the queue
beforehand in the self-same iteration of the while loop in `queue.pop()`, making the level order
successor of `key` take the front position of the queue, hence when we break out of the while
loop, we return `queue.front()`
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LevelOrderSuccessor:
    '''Level Order Successor'''
    @staticmethod
    def findSuccessor(root, key):
        '''finds the level order successor of key'''
        
        #Base case/edge case: the binary tree is empty
        if not root:
            return None
        
        queue = [root]
        while(queue):
            currentNode = queue.pop(0)

            #insert the children of the current node in the queue
            if (currentNode.left):
                queue.append(currentNode.left)
            if (currentNode.right):
                queue.append(currentNode.right)
            
            # break if we have found the key
            if (currentNode.value == key):
                break
        
        return queue.pop(0)

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = LevelOrderSuccessor.findSuccessor(root, 12)
    if result:
        print(result.value, end=" ")
    result = LevelOrderSuccessor.findSuccessor(root, 9)
    if result:
        print(result.value, end=" ")


'''Time Complexity: O(N), where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.
Space Complexity: O(N), which is required for the queue. Since we can have a maximum of N/2 nodes
at any level (this could happen only at the lowest level), therefore we will need O(N) space to 
store them in the queue.
'''
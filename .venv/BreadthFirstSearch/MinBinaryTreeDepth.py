#!/usr/bin/env python3
'''Find the minimum depth of a binary tree.

-The minimum depth is the number of nodes along the shortest path from the root node to the 
nearest leaf node.
-A leaf node is a node with no children.Its standing on its own.

Pattern:  Binary Tree Level Order Traversal
Approach:
-We can follow the same BFS approach.
-The only difference will be, instead of keeping track of all the nodes in a level, we will only
track the depth of the tree.As soon as we find our first leaf node, that level will represent the
minimum depth of the tree.

-`minimumTreeDepth` on the surface, its clear that this variable keeps track of the minimum depth
of the binary tree, which is the NUMBER of nodes on the shortest path from the root node to the
leaf node. But, behind the scenes, as mentioned in the previous sub-paragraph, this variable
keeps track of the NUMBER OF LEVELS we HAVE encountered before reaching our first leaf node.
-a leaf node is a node with no children; hence 
if (currentNode->left == nullptr && currentNode->right == nullptr) { return minimumTreeDepth;}
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MinimumBinaryTreeDepth:
    '''Minimum Binary Tree Depth'''
    @staticmethod
    def findDepth(root):
        # Base Case or edge case: the binary tree is empty
        if not root:
            return 0
        
        queue = [root]
        minimumTreeDepth = 0
        while(queue):
            minimumTreeDepth += 1
            levelSize = len(queue)

            for i in range(levelSize):
                currentNode = queue.pop(0)

                # check if this is a leaf node
                if (currentNode.left is None and currentNode.right is None):
                    return minimumTreeDepth
                
                # insert the children of current node in the queue
                if (currentNode.left):
                    queue.append(currentNode.left)
                if (currentNode.right):
                    queue.append(currentNode.right)
        
        return minimumTreeDepth


# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: ", MinimumBinaryTreeDepth.findDepth(root))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: ", MinimumBinaryTreeDepth.findDepth(root))

'''Time Complexity: O(N), where is the total number of nodes in the tree. This is due to the fact
that we traverse each node once.
Space Complexity : O(N), which is required for the queue. Since we can have a maximum of N/2 nodes
at any level (this could happen only at the lowest level), therefore we will need O(N) space to 
store them in the queue.
'''
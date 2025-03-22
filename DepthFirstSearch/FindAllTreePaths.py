#!/usr/bin/env python3
'''Given a binary tree and a number 'S', find all paths from root-to-leaf such that the sum of 
all the node values of each path equals 'S'.

Pattern: Binary Tree Path Sum pattern
Approach: We can follow the same DFS approach.

-There will be 2 differences:
1. Every time we find a root-to-leaf path, we will store it in a list.
2. We will traverse all paths and will not stop processing after finding the first path.

'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class FindAllTreePaths:
    '''Find All Tree Paths'''
    @staticmethod
    def findPaths(root, sum):
        '''Finds all root-to-leaf paths
        in which sum of node values == sum
        '''
        allPaths = []
        currentPath = []
        FindAllTreePaths.findPathsRecursive(root, sum, currentPath, allPaths)
        return allPaths
    
    @staticmethod
    def findPathsRecursive(currentNode, sum, currentPath, allPaths):
        # Base case: the binary tree is empty
        if not currentNode:
            return
        
        # add the current node to the path
        currentPath.append(currentNode.value)

        #if the current node is a leaf & its value is == to sum, save the current path
        if (currentNode.value == sum and currentNode.left is None and currentNode.right is None):
            allPaths.append(currentPath)
        else:
            # traverse the left sub-tree
            FindAllTreePaths.findPathsRecursive(currentNode.left, sum - currentNode.value, currentPath, allPaths)
            # traverse the right sub-tree
            FindAllTreePaths.findPathsRecursive(currentNode.right, sum - currentNode.value, currentPath, allPaths)
        
        # remove the current node from the path to backtrack
        # we need to remove the current node while we are going up the recursive call stack.
        currentPath.pop()


# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    sum = 23
    result = FindAllTreePaths.findPaths(root, sum)
    print(f"Tree paths with sum {sum} : ")
    for array in result:
        for num in array:
            print(num, end=" ")
        print("")

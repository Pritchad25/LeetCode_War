#!/usr/bin/env python3
'''Given a binary tree, populate an array to represent the averages of all of its levels.

Average = the addition of all items divided by the total number of those items

Pattern: Binary Tree Level Order Traversal
Approach:
-We can follow the same BFS approach.
-The only difference will be that instead of keeping track of all nodes of a level, we will only 
track the running sum of the values of all nodes in each level. In the end, we will append the 
average of the current level to the result array.

-when the inner for loop exits, we would have calculated the total sum of the values of all the
nodes in the the currentlevel we are standing; outside of the loop, we then take this total sum
`levelSum` and divide it by the number of nodes in the current level we are standing on 
`levelSize` and append the result to the `result` list hence the line 
`result.append(levelSum / levelSize)` outside of the for loop
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LevelAverage:
    '''Level Averages'''
    @staticmethod
    def findLevelAverages(root):
        '''Finds average of each level'''
        result = []
        # Base case/edge case: the binary tree
        if not root:
            return root
        
        queue = [root]
        while (queue):
            levelSize = len(queue)
            levelSum = 0
            
            for i in range(levelSize):
                currentNode = queue.pop(0)
                # add the node's value to the running sum
                levelSum +=  currentNode.value
                # insert the children of current node to the queue
                if (currentNode.left):
                    queue.append(currentNode.left)
                if (currentNode.right):
                    queue.append(currentNode.right)
            # append the current level's average to the result array
            result.append(levelSum / levelSize)
        
        return result

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = LevelAverage.findLevelAverages(root)
    print("Level averages are: ")
    for num in result:
        print(num, end=" ")
    

'''Time Complexity: O(N), where N is the number of nodes in the tree.This is due to the fact that
we traverse each node once.
Space Complexity: O(N), which is required for the queue. Since we can have a maximum of N/2 nodes
at any level (this could happen only at the lowest level), therefore we will need O(N) space to 
store them in the queue.
'''
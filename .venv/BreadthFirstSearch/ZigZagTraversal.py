#!/usr/bin/env python3
'''Given a binary tree, populate an array to represent its zigzag level order traversal. You 
should populate the values of all nodes of the first level from LEFT TO RIGHT, then RIGHT TO 
LEFT for the NEXT LEVEL and keep alternating in the same manner for the following levels.

Pattern: Binary Tree Level Order Traversal
Similarities: ReverseLevelOrderTraversal

-We can follow the same BFS approach. The only additional step we have to keep in mind is to 
alternate the level order traversal meaning that for every other level we will traverse similar 
to
-`if (leftToRight): currentLevel[i] = currentNode.value;` ie if the direction in which we should
populate the array representing the currentlevel we are standing on, is STANDARD(LEFT to RIGHT),
then populate the array or append the elements to it in the same way elements are appended to
traditional lists, which is appending at the "back" of whatever element is currently present in
the list, ie append elements at the end of the list(which is `currentLevel`).
-`else` ie REVERSE the direction in which we should populate the array representing the 
currentlevel we are standing on, ie populate the array or append the elements to it RIGHT to LEFT
-`currentLevel[levelSize - 1 - i]` this entire structure represents an index, in which we should
assign `currentNode.value`We can re-write the above structure as 
`currentLevel[levelSize - (i + 1)]`. The formular shouldve been `levelSize - i` but this formular
wouldve resulted in an `Index Out of range` error right from the start of the iteration of the 
loop. So to prevent this from happening and of couse, to get the correct result, we say
levelSize - (i + 1), hence the above structure.
-When the inner for loop exits, we add the `currentLevel` list to our matrix `result` and reverse
the direction in which we should populate the array representing the next level we will be
standing in via `leftToRight = !leftToRight`.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ZigZagTraversal:
    '''Zigzag Traversal'''
    @staticmethod
    def traverse(root):
        result = []
        # Base case/edge case: the binary tree is empty
        if not root:
            return result
        
        queue = [root]
        leftToRight = True
        while(queue):
            levelSize = len(queue)
            currentLevel = [0] * levelSize
            
            for i in range(levelSize):
                currentNode = queue.pop(0)

                # add the node to the current level based on the trverse direction
                if (leftToRight):
                    currentLevel[i] = currentNode.value
                else:
                    currentLevel[levelSize - 1 - i] = currentNode.value

                # insert the children of current node in the queue
                if (currentNode.left):
                    queue.append(currentNode.left)
                if (currentNode.right):
                    queue.append(currentNode.right)
            result.append(currentLevel)
            # reverse the traversal direction
            leftToRight = not leftToRight

        return result
 
# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)

    result = ZigZagTraversal.traverse(root)
    print("Zigzag Traversal: ")
    for array in result:
        for num in array:
            print(num, end=" ")
        print("") # Note that print() & print("") are the same; they print a new/empty line

'''Time Complexity: O(N) where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.
Space Complexity: O(N), as we need to return a list containing the level order traversal. We 
will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need O(N).
'''
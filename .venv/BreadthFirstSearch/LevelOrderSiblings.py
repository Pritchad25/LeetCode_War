#!/usr/bin/env python3
'''Given a binary tree, connect each node with its level order successor. The last node of each 
level should point to a null node.

Pattern:  Binary Tree Level Order Traversal
Approach:
- We can follow the same BFS approach.
- The only difference is that while traversing A LEVEL, we will remember the previous node to 
connect it with the current node.
-the code in `ConnectLevelOrderSiblings` will connect all LEVEL ORDER SIBLINGS, ie all siblings
that are in the same level; but with the requirement that `the last node of each level should 
point to a null node.`, when we define a Binary Tree Node, we have to put a 3rd pointer, the 
`next` pointer and initialise it to None
-`previousNode = currentNode` this is us remembering the `currentNode` as the previous node, so
that we connect it(previousNode) with the next `currentNode` which is in the same level as 
`previousNode`.When we have connected all LEVEL ORDER SIBLINGS, the structure of the Binary Tree
still remains the same, ie each node still has a left child pointer, a right child pointer and
a next node pointer, and the parent nodes still maintain their children as originally, leaf nodes
still remain childless; the only thing that changes is the fact that siblings in the same level
are now connected.
-`printLevelOrder()` just prints the values of the nodes after connecting all LEVEL ORDER 
SIBLINGS.  See notes for detailed practical explanation
'''

class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None
    
    def printLevelOrder(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(current.value, end=" ")
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

class ConnectLevelOrderSiblings:
    @staticmethod
    def connect(root):
        # Base case/edge case: if the tree is empty
        if not root:
            return
        
        queue = [root]
        while queue:
            previousNode = None
            levelSize = len(queue)

            # connect all nodes of this level
            i = 0
            while i < levelSize:
                currentNode = queue.pop(0)
                if previousNode:
                    previousNode.next = currentNode
                previousNode = currentNode

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                i += 1

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    ConnectLevelOrderSiblings.connect(root)
    print("Level order traversal using 'next' pointer:")
    root.printLevelOrder()

'''Time Complexity: O(N), where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.
Space Complexity: O(N), which is required for the queue. Since we can have a maximum of N/2 nodes
at any level (this could happen only at the lowest level), therefore we will need O(N) space to 
store them in the queue.
'''
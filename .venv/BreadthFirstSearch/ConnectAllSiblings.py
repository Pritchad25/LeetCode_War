#!/usr/bin/env python3
'''Given a binary tree, connect each node with its level order successor. The last node of each 
level should point to the first node of the next level.

Pattern:  Binary Tree Level Order Traversal
Approach:
-We can follow the same BFS approach.
-The only difference will be that, while traversing, we will remember (IRRESPECTIVE OF THE LEVEL)
the previous node to connect it with the current node.
-`previousNode = currentNode` - this is us remembering the `currentNode` as the previous node, so
that we connect it(previousNode) with the next `currentNode` which EITHER might be in the same
level as `previousNode` OR might be in a different level as `previousNode`, therefore, with this
line, we are remembering the `currentNode` we are standing on as the previous node 
IRRESPECTIVE OF THE LEVEL so that we connect it(previousNode) with the next `currentNode`.Hence
why we didnt traverse each level individually as in `LevelOrderSiblings`
-the code in `ConnectAllSiblings` will connect all LEVEL ORDER SIBLINGS, ie all siblings
that are in the same level; but with the requirement that `the last node of each level should 
point to the first node of the next level.`; when we define a Binary Tree Node, we have to put a 
3rd pointer, the `next` pointer and initialise it to None. When the loop in `ConnectAllSiblings`
exits, `previousNode` will be pointing to the last node of the Binary Tree in terms of 
`level-order-traversal, connecting each node with its level order successor` and because each 
Binary Tree node is defined as having 3 pointers(the `left` child pointer, the `right` child 
pointer and the `next` node pointer), its `next` node pointer will be pointing to NULL which 
makes sense since each node is defined with its  `next` node pointer pointing to NULL AND also 
the fact that, thats what the problem specified as the expected output.

-`printTree()` this method will just traverse the Binary Tree using the `next` pointers of
each node and print the values of each node of the Binary Tree.The loop will exit when its `current`
is now pointing to NULL`
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None
    
    def printTree(self):
        '''Prints the tree using the next pointer'''
        current = self
        print("Traversal using 'next' pointer: ")
        while (current):
            print(current.value, end=" ")
            current = current.next

class ConnectAllSiblings:
    '''Connects level order siblings'''
    @staticmethod
    def connect(root):
        #Base case: the binary tree 
        if not root:
            return
        
        previousNode = None
        currentNode = None
        queue = [root]
        while (queue):
            currentNode = queue.pop(0)
            if (previousNode):
                previousNode.next = currentNode
            previousNode = currentNode
            
            # insert the children of current node in the queue
            if (currentNode.left):
                queue.append(currentNode.left)
            if (currentNode.right):
                queue.append(currentNode.right)

# Testing
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    ConnectAllSiblings.connect(root)
    root.printTree()


'''Time Complexity: O(N), where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.
Space Complexity: O(N), which is required for the queue. Since we can have a maximum of N/2 nodes
at any level (this could happen only at the lowest level), therefore we will need O(N) space to 
store them in the queue.
'''
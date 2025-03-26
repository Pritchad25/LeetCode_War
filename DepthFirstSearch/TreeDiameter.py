#!/usr/bin/env python3
'''Given a binary tree, find the length of its diameter. 

The diameter of a tree is the number of nodes on the longest path between 
any two leaf nodes. The diameter of a tree may or may not pass through the 
root.
Note: You can always assume that there are at least two leaf nodes in the 
given tree.

Pattern: Binary Tree Path Sum 
Approach
-We can follow the same DFS approach. There will be a few differences:
1. At every step, we need to find the height of both children of the current
node. For this, we will make 2 recursive calls similar to DFS.Hence the
lines:
`leftTreeHeight = calculateHight(currentNode.left, treeDiameter)
rightTreeHeight = calculateHight(currentNode.right, treeDiameter)`

2. The height of the current node will be equal to the maximum of the heights
of its left or right children, plus 1 for the current node.Hence the lines:
`return max(leftTreeHeight, rightTreeHeight) + 1`

3. The tree diameter at the current node will be equal to the height of the 
left child plus the height of the right child plus 1 for the current node:
diameter = leftTreeHeight + rightTreeHeight + 1

-To find the overall tree diameter, we will use a class level variable. This
variable will store the maximum diameter of all the nodes visited so far,
hence, eventually, it will have the final tree diameter. Hence the line:
`treeDiameter[0] = max(treeDiameter[0], diameter)`
-we initialise the variable `treeDiameter` to a list with 1 element (0),like
so: `treeDiameter = [0]`.So, in the above line, for every node we visit,
we check if the diameter at the current node that we're standing on is >
than the first element of `treeDiameter`, which is `treeDiameter[0]`;if so,
we update this first element hence we say 
`treeDiameter[0] = max(treeDiameter[0], diameter)`.So, in essence, we're
always checking (and possibly updating) the first element of `treeDiameter`
and at the end of the entire recursion, returning this first element as
the actual length of diameter of the tree.
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeDiameter:
    @staticmethod
    def find_diameter(root):
        tree_diameter = [0]
        TreeDiameter.calculate_height(root, tree_diameter)
        return tree_diameter[0]

    @staticmethod
    def calculate_height(current_node, tree_diameter):
        if current_node is None:
            return 0

        left_tree_height = TreeDiameter.calculate_height(current_node.left, tree_diameter)
        right_tree_height = TreeDiameter.calculate_height(current_node.right, tree_diameter)

        # diameter at the current node will be equal to the height of left subtree +
        # the height of right sub-trees + '1' for the current node
        diameter = left_tree_height + right_tree_height + 1

        # update the global tree diameter
        tree_diameter[0] = max(tree_diameter[0], diameter)

        # height of the current node will be equal to the maximum of the heights of
        # left or right subtrees plus '1' for the current node
        return max(left_tree_height, right_tree_height) + 1

# Testing
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Diameter of Binary Tree is: ", TreeDiameter.find_diameter(root))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Diameter of Binary Tree is: ", TreeDiameter.find_diameter(root))

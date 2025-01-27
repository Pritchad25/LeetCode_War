#!/usr/bin/env python3
import sys
'''Write a function that finds the path with the maximum sum in a given 
binary tree.The function returns the maximum sum. 

A path can be defined as a sequence of nodes between any 2 nodes and doesn't
necessarily pass through the root(meaning if the path passes through the
root, we will consider that path AND if it doesnt, we will consider it as
well).

Pattern:  Binary Tree Path Sum pattern; shares the algorithmic logic with
Tree Diameter.
Approach:
-We can follow the same DFS approach.
-The only difference will be to ignore the paths with negative sums.Since 
we need to find the OVERALL maximum sum, we should ignore any path which has
an OVERALL negative sum.

-`maxPathSumFromLeft = max(maxPathSumFromLeft, 0)
maxPathSumFromRight = max(maxPathSumFromRight, 0)` - since we need to find 
the maximum sum, we want to or we should ignore ANY path which has an 
overall negative sum.So we ignore the sum from left subtree 
`maxPathSumFromLeft` if it is an OVERALL negative sum by re-assigning to 
the variable `maxPathSumFromLeft` the MAXIMUM between the sum from left 
subtree & 0, hence `maxPathSumFromLeft = max(maxPathSumFromLeft, 0)`
Similarly, we ignore the sum from right subtree `maxPathSumFromRight` if it
is an OVERALL negative sum by re-assigning to  the variable 
`maxPathSumFromRight` the MAXIMUM between the sum from right subtree & 0, 
hence `maxPathSumFromRight = max(maxPathSumFromRight, 0)` as shown above.
-`localMaximumSum = maxPathSumFromLeft+maxPathSumFromRight+currentNode.value`
In the above line, we are calculating the MAXIMUM PATH SUM at the current
node that we are standing in(ie, the HIGHEST SUM of the path at the current
node that we are standing in; it will be == the sum of the left subtree of
the current node + the sum of the right subtree of the current node + value
of the current node)
-`global_maximum_sum[0] = max(global_maximum_sum[0], local_maximum_sum)`-
-we initialise the variable `global_maximum_sum` to a list with 1 element
(-sys.maxsize, which im assuming is negative infinity),like so: 
`global_maximum_sum = [-sys.maxsize]`.So, in the above line, for every node 
we visit, we check if the MAXIMUM PATH SUM at the current node that we 
are standing in(ie, the HIGHEST SUM of the path at the current node that 
we're standing on `local_maximum_sum`) > than the first element of 
`global_maximum_sum`, which is `global_maximum_sum[0]`;if so,
we update this first element hence we say 
`global_maximum_sum[0] = max(global_maximum_sum[0], local_maximum_sum)`.So,
in essence, we're always checking (and possibly updating) the first element
of `global_maximum_sum` and at the end of the entire recursion, returning 
this first element as the maximum sum
-`max(maxPathSumFromLeft, maxPathSumFromRight) + currentNode.val` Here, we
are determining the MAXIMUM SUM of ANY path from the current node that we
are standing in (ie, HIGHEST SUM of ANY path from the current node that we
are standing in; it will be == the MAXIMUM between the sum from left subtree
`maxPathSumFromLeft` & sum from right subtree `maxPathSumFromRight` + value
of current node)
'''
class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MaximumPathSum:
    @staticmethod
    def find_maximum_path_sum(root):
        global_maximum_sum = [-sys.maxsize]
        MaximumPathSum.find_maximum_path_sum_recursive(root, global_maximum_sum)
        return global_maximum_sum[0]

    @staticmethod
    def find_maximum_path_sum_recursive(current_node, global_maximum_sum):
        if current_node is None:
            return 0

        max_path_sum_from_left = MaximumPathSum.find_maximum_path_sum_recursive(current_node.left, global_maximum_sum)
        max_path_sum_from_right = MaximumPathSum.find_maximum_path_sum_recursive(current_node.right, global_maximum_sum)

        # ignore paths with negative sums
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)

        # maximum path sum at the current node
        local_maximum_sum = max_path_sum_from_left + max_path_sum_from_right + current_node.value

        # update the global maximum sum
        global_maximum_sum[0] = max(global_maximum_sum[0], local_maximum_sum)

        # maximum sum of any path from the current node
        return max(max_path_sum_from_left, max_path_sum_from_right) + current_node.value

# Testing
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Maximum Path Sum: ", MaximumPathSum.find_maximum_path_sum(root))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: ", MaximumPathSum.find_maximum_path_sum(root))

'''Time Complexity: O(N), where N is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.
Space Complexity: O(N), in the worst case. This space will be used to store
the recursion stack. The worst case will happen when the given tree is a 
linked list (i.e., every node has only one child).
'''
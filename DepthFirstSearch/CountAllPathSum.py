#!/usr/bin/env python3
'''Given a binary tree and a number 'S' find all paths in the tree such 
that the sum of all the node values of each path equals 'S'.
Please note that the paths can start or end at any node but all paths must 
follow direction from parent to child (top to bottom).

Problem Clarification:
`find all paths` - we're returning the number of those paths

Pattern:  Binary Tree Path Sum
Approach:
-We can follow the same DFS approach.But there will be 4 differences:
1. We will keep track of the current path in a list(called `currentPath`) 
which will be passed to every recursive call. 
-this first step is shown by this code:`currentPath.append(currentNode.val)`

2. Whenever we traverse a node we will do 2 things:
   i) Add the current node to the current path.
   ii) As we added a new node to the current path, we should find the sums 
   of all sub-paths of this current path `currentPath`ENDING at the current 
   node. If the sum of any sub-path is equal to 'S' we will increment our 
   path count `pathSum`.
-this second step is shown by all the code marked by comment that starts
with `find the sums of all sub-paths`

3. We will traverse all paths and will not stop processing after finding the
first path.
-this third step is shown by the code where we are Recursively traversing
the left and right sub-trees of `currentPath`.

4. Remove the current node from the current path before returning from the 
function. This is needed to Backtrack while we are going up the recursive 
call stack to process other paths.
-this 4th step is shown by all the code marked by comment that starts with
`remove the current node from the path to backtrack`

-`reversed` returns a reverse iterator over the values of the given sequence.
'''

class TreeNode:
    '''Defines a Binary Tree Node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class CountAllPathSum:
    @staticmethod
    def count_paths(root, S):
        current_path = []
        return CountAllPathSum.count_paths_recursive(root, S, current_path)

    @staticmethod
    def count_paths_recursive(current_node, S, current_path):
        if current_node is None:
            return 0

        # add the current node to the path
        current_path.append(current_node.value)
        path_count = 0
        path_sum = 0

        # find the sums of all sub-paths in the current path list
        for value in reversed(current_path):
            path_sum += value
            # if the sum of any sub-path is equal to 'S' we increment our path count.
            if path_sum == S:
                path_count += 1

        # traverse the left sub-tree
        path_count += CountAllPathSum.count_paths_recursive(current_node.left, S, current_path)
        # traverse the right sub-tree
        path_count += CountAllPathSum.count_paths_recursive(current_node.right, S, current_path)

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        current_path.pop()

        return path_count
# Testing
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Tree has path: ", CountAllPathSum.count_paths(root, 12))

'''Time Complexity: O(N2), in the worst case, where N is the total number 
of nodes in the tree. This is due to the fact that we traverse each node 
once, but for every node, we iterate the current path. The current path, 
in the worst case, can be O(N) (in the case of a skewed tree). But, if the 
tree is balanced, then the current path will be equal to the height of the 
tree, i.e., O(logN). So the best case of our algorithm will be O(NlogN)

Space Complexity: O(N), where N is the total number of nodes in the tree.
This space will be used to store the recursion stack. The worst case will 
happen when the given tree is a linked list (i.e., every node has only one 
child). We also need O(N) space for storing the `currentPath` in the worst 
case.Overall, space complexity of our algorithm is O(N).
'''

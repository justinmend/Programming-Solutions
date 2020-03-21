'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Implement using DFS
        # Assumptions:
        # 1. Are we given a tree with a height greater than 0? No, the given input
        # can have empty nodes.

        # Brute Force:
        # Use a stack - LIFO?
        # How should we add the nodes to our stack?
        # How do we keep track of the max depth?

        # 1. Initially check if given input is empty, if so return 0
        # 2. Use two stacks. First stack is used to add nodes from the tree in depth first search order. The second stack is used to keep track of the height of the nodes in the first stack respectively.
        # 3. Initially add root node to first stack and also give it a height of 1 using the second stack.
        # 4. Keep track of the global max. Take the max between the current node's height and current max value.
        # 5. Push in the current node's left and right children if they are not null while also keeping track of their height. Push the children of the current node from right to left order into the stack since stack is LIFO. When a node is popped of from the stack it will then be the left child first. Left to right or right to left order shouldn't matter since we will still iterate in DFS order no matter what.
        # 6. Continue adding children of nodes in DFS order to our stack along with their respective height until the stack is empty.
        # 7. Return max value as our answer

        if root is None:
            return 0

        stack = []
        node_heights = []

        stack.append(root)
        node_heights.append(1)

        maxDepth = 0

        while stack:
            node = stack.pop()
            height = node_heights.pop()

            maxDepth = max(height, maxDepth)

            if node.right != None:
                stack.append(node.right)
                node_heights.append(height+1)

            if node.left != None:
                stack.append(node.left)
                node_heights.append(height+1)

        return maxDepth

        # Time Complexity - O(N):
        # N represents the total nodes in the binary tree. We iterate through all the nodes in the tree once.

        # Space Complexity - O(S + T):
        # S represents the total nodes from the binary tree that we add to our stack 1. Size of our stack 1 is proportionate to the total amount of nodes in the binary tree.
        # T represents the total amount of node's height we keep track in our stack 2. The same for our stack 2, it's size is also proportionate to the total amount of nodes in the binary tree.

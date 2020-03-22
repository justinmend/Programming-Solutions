'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Implement using a stack
        # Assumptions:
        # 1. Are we given a binary tree with a depth greater than 0?
        # No, we can be given an input with no nodes.
        # 2. Is an empty tree a symmetric tree? Yes.

        # Brute Force:
        # How should we add the nodes from the tree to our stack?
        # Add in a dfs order? No, using stack but in bfs order.

        # 1. Check if initial input given is empty, if so return true
        # Check if initial root's left and right child are null, if so return true.
        # 2. Initialize our stack with the root.left and root.right
        # 3. While stack is not empty:
        # Pop two elements at the same time and store in temp variables.
        # Check if pop1 and pop2 are equal:
        # If pop1 and pop2 are null, continue
        # If pop1 or po2 are null, return false
        # If pop1's value and pop2's value are equal, contnue. Else return false.
        # 4. Add nodes in the stack in the order of:
        # pop1.left, pop2.right, pop1.right, pop2.left
        # 5. Return true in the end when stack becomes empty

        if root is None or (root.left is None and root.right is None):
            return True

        stack = []
        stack.append(root.right)
        stack.append(root.left)

        while stack:
            pop_left = stack.pop()
            pop_right = stack.pop()

            if pop_left is None and pop_right is None:
                continue
            if pop_left is None or pop_right is None:
                return False
            if pop_left.val != pop_right.val:
                return False

            stack.append(pop_left.left)
            stack.append(pop_right.right)
            stack.append(pop_left.right)
            stack.append(pop_right.left)

        return True

        # Time Complexity - O(N):
        # N represents the total nodes in the binary tree. We iterate through all the nodes in the tree once.
        # Worst case is that the binary tree is symmetric so
        # we are required to iterate through all the nodes in the binary tree.

        # Space Complexity - O(N):
        # N represents the total nodes from the binary tree that we add to our stack. The size of our stack is
        # proportional to the size of the input binary tree. Worst case is that the binary tree is symmetric so
        # we are required to add all the nodes from the binary tree to our stack.

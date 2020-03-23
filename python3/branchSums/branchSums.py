'''
Write a function that takes in a Binary Tree and returns a list of its branch sums (ordered from leftmost branch sum to rightmost branch sum). A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. Each Binary Tree node has a value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value.


'''

# This is the class of the input root. Do not edit it.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Implements using DFS with two stacks
    # Assumptions:
    # 1. For the input, are we given a binary tree whose height is greater than 0?

    # Brute Force:
    # The size of our result list is proportionate to how many leaf nodes there are in the
    # given binary tree?
    # Use two stacks?

    # 1. Check initially if root is null, if so return an empty list
    # Check if root.left and root.right are both null, if so return [root.value]
    # 2. Create a result list to store our leaf nodes sum values.
    # Create two stacks, one to store the nodes from the binary tree and the second is to keep track
    # of the current sum value for a node.
    # Initialize stack 1 and stack 2 with root node and root.value
    # 3. while stack:
    # pop from the stack and store the node in a temp variable
    # pop from the second stack and store the sum value in a temp variable
    # If temp.right and temp.left are both null, add temp sum value to result list
    # If temp.right is not null:
    # Add temp.right to stack 1
    # Add temp sum value + temp.right.value to stack 2
    # If temp.left is not null:
    # Add temp.left to stack 1
    # Add temp sum value + temp.left.value to stack 2

    # 4. Return the result list as our answer

    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.value]

    result = []
    stack = [root]
    node_sums = [root.value]

    while stack:
        temp = stack.pop()
        currSum = node_sums.pop()
        if temp.right is None and temp.left is None:
            result.append(currSum)

        if temp.right is not None:
            stack.append(temp.right)
            node_sums.append(currSum + temp.right.value)
        if temp.left is not None:
            stack.append(temp.left)
            node_sums.append(currSum + temp.left.value)

    return result

    # Time Complexity - O(N):
    # N represents the total amount of nodes we iterate through in the binary tree. We iterate through all the nodes
    # in the binary tree once.

    # Space Complexity - O(R + N + S):
    # R represents how many leaf nodes' sums there are in our result list. The size of our result list is proportionate
    # to how many leaf nodes the binary tree input has.
    # N represents the total amount of nodes there are from the binary tree that we add into our stack. The size of our stack
    # is proportionate to how many nodes there are in the binary tree input.
    # S represents the total amount of nodes' sums we keep track of in our node_sums stack. The size of our node_sums
    # stack is also proportionate to how many nodes there are in the binary tree input.

'''

  Write a function that takes in a potentially invalid Binary Search Tree (BST)
  and returns a boolean representing whether the BST is valid.
'''

# This is an input class. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time - O(N):
# N represents the total nodes in the bst where iterate through it once.

# Space - O(S + M):
# S represents the size of our first queue containing nodes. Our queue size is
# proportional to the total nodes in the bst input.
# M reperesents the size our second queue which holds boolean values used
# to track which side other nodes are on compared to the root node of the bst.
# The size of this queue is also proportionate to the total amount of nodes in the bst.

# We can combine both queue into one queue instead by making the node and boolean value
# a tuple when appending to one queue. This will improve the space complexity to O(N).


def validateBst(tree):
    # Assumptions:
    # Notes:

    # Brute Force:
    # Use BFS and a queue to traverse through tree.

    # Edge case:
    # Compare node to initial root node and make sure the BTS property is still satisfied.
    # Need to find a way to keep track of which side of the general bst branch the node is on
    # to determine how to compare values.
    # Use another stack for branch side tracking?
    # Use recursion instead?

    # Initially check root's left and right child that they exist before initializing
    # queue with root's left and right child.
    if tree.left is not None and tree.right is not None:
        if tree.value <= tree.left.value:
            return False
        if tree.value > tree.right.value:
            return False
    elif tree.left is not None:
        if tree.value <= tree.left.value:
            return False
    elif tree.right is not None:
        if tree.value > tree.right.value:
            return False

    queue = [tree.left, tree.right]
    queueSide = [True, False]

    while queue:
        curNode = queue.pop(0)
        isLeft = queueSide.pop(0)

        if curNode is not None:
            # Compare current node value to root tree value
            # and make sure it follows BST property.
            if isLeft:
                if curNode.value >= tree.value:
                    return False
            else:
                if curNode.value <= tree.value:
                    return False

            # Add left child
            if curNode.left is not None:
                if curNode.value <= curNode.left.value:
                    return False
                queue.append(curNode.left)
                queueSide.append(isLeft)

            # Add right child
            if curNode.right is not None:
                if curNode.value > curNode.right.value:
                    return False
                queue.append(curNode.right)
                queueSide.append(isLeft)

    return True

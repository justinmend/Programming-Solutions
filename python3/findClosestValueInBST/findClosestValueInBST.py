'''
  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.

  You can assume that there will only be one closest value.
'''

# Time - O(N) | Space - O(1)
# N represents the total amount of nodes in the given BST.
# Worst case is that our BST is not balanced where all the nodes
# are connected going in one direction, that is, all the nodes only have
# left child nodes. That means we would essentialy traverse through all
# the nodes in the BST.


def findClosestValueInBst(tree, target):
    # Assumptions:
    # 1. Are we given a non-empty node?

    # Notes:
    # 1. Given the head of a BST
    # 2. Given a target integer value. target >= 0 and target < 0
    # Can be negative or positive
    # 3. Return the closest value to the target value in the BST
    # 4. BST property:
    # Left child node values are less than the parent node
    # Right child node values are greater than the parent node

    # Brute Force:
    # How do we iterate through the BST?
    # How do we keep track of the node that has a value closest to the target?

    # Keep track of the closest node value to target value
    # Compare the closest to the current node.
    # Take the node value with the smallest difference to target value.
    # Use abs built in function.
    closest = float("inf")
    curNode = tree

    while curNode:
        # Make sure to also consider previous parent nodes, since they can be closer to the target value.
        if abs(target - closest) > abs(target - curNode.value):
            closest = curNode.value

        # Compare target value to current node.
        # This will dictate which direction in the BST we go to.
        if curNode.value == target:
            break
        elif curNode.value > target:
            curNode = curNode.left
        else:
            curNode = curNode.right

    return closest

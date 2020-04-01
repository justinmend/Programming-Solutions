'''

  Write a function that takes in a Binary Tree and inverts it. In other words,
  the function should swap every left node in the tree for its corresponding
  right node.


'''

# Time - O(N) | Space - O(M)
# N represents the total nodes we iteratr through in the binary tree once.
# M represents the size of our queue which is proportional to the total
# nodes in the binary tree input.


def invertBinaryTree(tree):
    # Assumptions:
    # Notes:

    # Brute Force:
    # BFS? Queue?
    # How do we properly swap nodes?

    queue = [tree]

    while queue:
        curNode = queue.pop(0)
        if curNode.left is not None:
            queue.append(curNode.left)
        if curNode.right is not None:
            queue.append(curNode.right)
        swap(curNode)


def swap(node):
    node.left, node.right = node.right, node.left

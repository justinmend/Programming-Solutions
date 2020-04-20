'''

  Write a function that takes in a Binary Tree and inverts it. In other words,
  the function should swap every left node in the tree for its corresponding
  right node.


'''

# Time - O(N) | Space - O(N)
# N represents the total amount of nodes in the binary tree.


def invertBinaryTree(tree):
    # Assumptions:
    # 1. Are we given a non-empty tree input?

    # Notes:
    # 1. Given the head of a binary tree
    # 2. Invert the binary tree

    # Brute Force:
    # BFS

    queue = [tree]

    while queue:
        curNode = queue.pop(0)  # 5

        # Make sure to check if current node's children are valid
        # before trying to append them to the queue.
        if curNode.left:
            queue.append(curNode.left)
        if curNode.right:
            queue.append(curNode.right)

        # Swap left child with right child
        curNode.left, curNode.right = curNode.right, curNode.left

'''

  Write three functions that take in a Binary Search Tree (BST) and an empty
  array, traverse the BST, add its nodes' values to the input array, and return
  that array. The three functions should traverse the BST using the in-order,
  pre-order, and post-order tree-traversal techniques, respectively.
'''

# Time - O(N):
# N represents the total nodes in the tree.
# Space - O(N):
# N represents the total size of our stack frame from our recursion calls which is proportional
# to the total nodes in the tree.


def inOrderTraverse(tree, array):
    # left, root, right
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

# Time - O(N):
# N represents the total nodes in the tree.
# Space - O(N):
# N represents the total size of our stack frame from our recursion calls which is proportional
# to the total nodes in the tree.


def preOrderTraverse(tree, array):
    # root, left, right
    if tree:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# Time - O(N):
# N represents the total nodes in the tree.
# Space - O(N):
# N represents the total size of our stack frame from our recursion calls which is proportional
# to the total nodes in the tree.


def postOrderTraverse(tree, array):
    # left, right, root
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

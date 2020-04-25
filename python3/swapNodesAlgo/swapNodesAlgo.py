#!/bin/python3

import os
import sys

# Time - O(Q * (D + M) + N)
# Space - O(Q * (D + M + L) + N)
# N represents the length of the indexes array.
# Q represents the length of queries array.
# D represents the max depth of the tree we created.
# M represents the total nodes in the tree.
# L represents all the nodes from the tree where we add into our item list in an in-order fashion.


def swapNodes(indexes, queries):
    # Assumptions:

    # Notes:
    # 1. Given indexes, an array of integers representing index values of each node[i],
    # beginning with node[0], the first element, as the root.
    # 2. Given queries, an array of integers, each representing a interval value.
    # For each interval, perform the swap operation and store the indices of your in-order traversal
    # to your result array.
    # Queries contain integers representing the interval where for every treeLevel[i] mod interval,
    # we swap the left and right child of every node in the (treeLevel[i]%interval).
    # 3. '-1' is used to represent a null/None node.
    # 4. Return a 2d array where each element is an array of integers representing
    # the node indices of an in-order traversal after a swap operation.

    # Brute Force:
    # Modifying the recursion limit in python because of runtime error in test cases #10 and #11
    sys.setrecursionlimit(1500)

    # Time - O(N) | Space - O(N)
    # N represents the length of the indexes array.
    tree, maxLevel = create_tree(indexes)

    result = []

    # Queries contain integers representing
    # the interval where for every treeLevel[i] mod interval,
    # we swap the left and right child of the current node for all nodes in the (treeLevel[i]%interval).

    # Time - O(Q * (D + 2M))          -> O(Q * (D + M))
    # Space - O(Q * (D + 2M + L))     -> O(Q * (D + M + L))
    # Q represents the length of queries array.
    for interval in queries:
        item = []

        # Time - O(D) | Space - O(D)
        # D represents the max depth of the tree we created.
        # Worst case is we add every level up to the max depth of the tree
        # into our levelsWithinInterval list.
        levelsWithinInterval = [x for x in range(
            1, maxLevel+1) if x % interval == 0]

        # Time - O(M) | Space - O(M)
        # M represents the total nodes in the tree.
        # We call the recursion method swap_tree() for every node in the tree.
        # The recursion calls take up space in our call stack frame.
        root = swap_tree(tree, levelsWithinInterval)

        # Time - O(M) | Space - O(M + L)
        # We call the recursion method traverse_inorder() for every node in the tree.
        # The recursion calls take up space in our call stack frame.
        # L represents all the nodes from the tree where we add into our item list in an in-order fashion.
        traverse_inorder(root, item)

        result.append(item)

    return result

# Time - O(M) | Space - O(M + L)
# We call the recursion method traverse_inorder() for every node in the tree.
# The recursion calls take up space in our call stack frame.
# L represents all the nodes from the tree where we add into our list in an in-order fashion.


def traverse_inorder(tree, item):
    # Traverse the tree in-order (left,root,right)
    if tree.left:
        traverse_inorder(tree.left, item)
    item.append(tree.data)
    if tree.right:
        traverse_inorder(tree.right, item)

# Time - O(N):
# N represents the length of the indexes array.
# Space - O(2N) -> O(N):
# Worst case is we add both values in the pair for all pairs in indexes array to our queue.


def create_tree(indexes):
    # Use BFS and queue to create tree
    root = Node(1, 1)
    queue = [root]

    # Initialize with root's level (1)
    # Not zero-based index
    maxLevel = 1

    # Time - O(N):
    # N represents the length of the indexes array.
    # Space - O(2N) -> O(N):
    # Worst case is we add both values in the pair for all pairs in indexes array to our queue.

    for left, right in indexes:
        cur = queue.pop(0)

        # '-1' denotes a node that is null/none
        if left != -1:
            leftNode = Node(left, cur.level + 1)
            cur.left = leftNode
            queue.append(leftNode)
        if right != -1:
            rightNode = Node(right, cur.level + 1)
            cur.right = rightNode
            queue.append(rightNode)

        # Finally the queue is empty, and cur is at lowest level.
        # Because there are always [-1, -1]s at the end of the indexes
        maxLevel = cur.level

    return (root, maxLevel)

# Time - O(M) | Space - O(M)
# M represents the total nodes in the tree.
# We call the recursion method swap_tree() for every node in the tree.
# The recursion calls take up space in our call stack frame.


def swap_tree(tree, levelsWithinInterval):
    if tree.left:
        swap_tree(tree.left, levelsWithinInterval)
    if tree.right:
        swap_tree(tree.right, levelsWithinInterval)
    if tree.level in levelsWithinInterval:
        tree.left, tree.right = tree.right, tree.left
    return tree

# tree node


class Node:
    def __init__(self, data, level):
        self.data = data
        self.left = None
        self.right = None
        self.level = level


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

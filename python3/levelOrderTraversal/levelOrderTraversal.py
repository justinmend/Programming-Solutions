'''
You are given a pointer to the root of a binary tree. You need to print the level order traversal of this tree. In level order traversal, we visit the nodes level by level from left to right. 

Constraints:
1 <= Nodes in the tree <= 500

Output Format:
Print the values in a single line separated by a space.


Sample Input:

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  

Sample Output:
1 2 5 3 6 4

Explanation:
We need to print the nodes level by level. We process each level from left to right.
Level Order Traversal: 1 -> 2 -> 5 -> 3 -> 6 -> 4.
'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
# Time - O(N) | Space - O(2N) -> O(N)
# N represents the total nodes in the binary tree.
# The size of our queue and result list is proportional to the total nodes in the binary tree.


def levelOrder(root):
    # Assumptions:

    # Notes:
    # 1. Given the root of a binary tree
    # 2. Print the level order traversal of the tree

    # Brute Force:
    # BFS

    result = []
    queue = [root]

    # print => 1 -> 2 -> 5 -> 3 -> 6 -> 4
    while queue:
        curNode = queue.pop(0)
        result.append(curNode.info)

        if curNode.left:
            queue.append(curNode.left)
        if curNode.right:
            queue.append(curNode.right)

    print(*result)

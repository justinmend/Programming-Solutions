'''
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

Constraints:
The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Implement using BFS
        # Assumptions:
        # 1. Are we given an input where the tree node's length is greater than 0?
        # No, the total number of nodes is between [0, 10^4].

        # Brute force:
        # Use a queue - FIFO
        # 0. Check if initial root is null, if so return 0
        # 1. Initialize queue with the root node.
        # 3. while queue is not empty:
        # 4. Iterate through the range of the size of the current layer in the queue
        # Pop the top item from queue.
        # Add all the child nodes of the recently popped item to the queue.
        # 3. After iterating through the range of the size of the current layer in the queue, we then increment max depth.
        # 4. Return max depth value as the answer

        if root is None:
            return 0

        queue = collections.deque()
        queue.append(root)

        maxDepth = 0

        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()

                for child in temp.children:
                    queue.append(child)

            maxDepth += 1

        return maxDepth

        # Time Complexity - O(N):
        # N represents the total nodes in the tree and we iterate it through it once.

        # Space Complexity - O(N):
        # N represents the total nodes from the tree that we add to our queue.

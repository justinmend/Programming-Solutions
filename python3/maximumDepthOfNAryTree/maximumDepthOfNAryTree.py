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

'''
Implement using BFS
'''


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


"""
Implement using DFS
"""


class Solution2:
    def maxDepth(self, root: 'Node') -> int:
        # Implement using DFS
        # Assumptions:
        # 1. For the input, are we given a tree with a height greater than 0? No, the input can be an empty tree.

        # Note:
        # 1. The depth of the n-ary tree is less than or equal to 1000.
        # 2. The total number of nodes is between [0, 10^4].

        # Brute Force:
        # Use a stack?
        # How should we add the nodes from the tree to our stack? DFS
        # How do we keep track of the max depth?
        # Use another stack to keep track of each node's height?

        # 1. Check initially if root is null, if so return 0
        # Check if root.children is null, if so return 1
        # 2. Initialize stack 1 and stack 2 with root node and value of 1 respectively.
        # 3. while stack is not empty:
        # Pop current node and store in temp variable
        # Also pop the height value of the current node from the second stack and store in a temp variable.
        # Set the max depth to the value between the max of current max depth and the height of the temp node.
        # 4. Iterate through the children of the temp node:
        # Add to stack from right to left so that when items are popped off from stack, the order is from left to right.
        # As we add nodes to the stack also add the height of the node to the second stack. When adding height, increment by 1.
        # 5. Return the max depth value as our answer when the stack becomes empty.

        if root is None:
            return 0
        if root.children is None:
            return 1

        stack = [root]
        node_heights = [1]

        maxDepth = 1

        while stack:
            temp = stack.pop()
            height = node_heights.pop()
            maxDepth = max(maxDepth, height)

            for child in reversed(temp.children):
                stack.append(child)
                node_heights.append(height+1)

        return maxDepth

        # Time Complexity - O(N):
        # N represents the total nodes in the tree that we iterate through. We iterate through all the nodes in the tree once.

        # Space Complexity - O(S + N):
        # S represents the total nodes from the tree that we add into our stack. The size of our stack is proportionate to the total amount of nodes in
        # the input tree we are given.
        # N represents the total amount of nodes' height in the tree we keep track of in our second stack. The size our node_heights stack is also proportionate
        # to the total amount of nodes in the input tree we are given.

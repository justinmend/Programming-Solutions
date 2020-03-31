# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Assumptions:
        # Notes:
        # Brute Force:
        # Use a stack?
        # Initialize stack with root(self)

        # Use a while loop for stack.
        # Add children from right to left, so pop order is correct, that is, left to right
        # When do we add current node name to array?
        # After we pop an item we can then add it to the array.

        # Time - O(N) | Space - O(S)
        # N represents the total nodes we iterate through in the tree once.
        # S represents the size of our stack which is proportionate to the size of the input tree.
        stack = [self]

        while stack:
            cur = stack.pop()
            array.append(cur.name)

            for child in reversed(cur.children):
                stack.append(child)

        return array

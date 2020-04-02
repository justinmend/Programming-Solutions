# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Time - O(H + |M - N|):
# H represents the max height between the two heights of the descendant inputs.
# Worst case is one of the descendants is at the bottom most of the tree
# which requires us to go through each level and one ancestral node at a time in the tree.
# M and N represents the height of the descendant inputs respectively.
# We go through the absolute difference between the difference of M and N, which
# is the number of levels required for us to go through to bring one of the descendant's
# height level at the same level as the other descendant height level.

# Space - O(1): Only using auxiliary space.


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Assumptions:
    # 1. Are we returning the node istelf or the node's name value? Node itself.
    # 2. For the initial input, can one of the descendant inputs be an ancestor to the other?
    # 3. There will always be a valid youngest common ancestor for the two descendant inputs? Yes.

    # Notes:

    # Brute Force:
    # How do we get the youngest common ancestor of the two descendant inputs?

    # Get the height for both descendants
    # Have both descendants be at the same height level
    # Check if they are at the same youngest common ancestor, if so return the node
    # Else, keep traversing up until we find the younges common ancestor.

    # Create helper method to get a descendant's height.

    descendOneHeight = getDescendantHeight(descendantOne)
    descendTwoHeight = getDescendantHeight(descendantTwo)

    while descendOneHeight != descendTwoHeight:
        if descendOneHeight > descendTwoHeight:
            descendantOne = descendantOne.ancestor
            descendOneHeight -= 1
        else:
            descendantTwo = descendantTwo.ancestor
            descendTwoHeight -= 1

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


def getDescendantHeight(node):
    count = 1
    while node.ancestor:
        node = node.ancestor
        count += 1

    return count

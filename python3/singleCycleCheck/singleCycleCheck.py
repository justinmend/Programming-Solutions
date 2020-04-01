# Time - O(N) | Space - O(1):
# N represents the total elements we iterate through in the array.


def hasSingleCycle(array):
    # Assumptions:
    # Notes:

    # Brute Force:
    # How do we check for a single cycle?
    # How do we wrap around?

    # If number of items visited is not equal to the length of array and
    # the index we come back to is not the first index,
    # there is not enough jump to visit all the elements in the array.

    elementsVisited = 0
    curIdx = 0

    while elementsVisited < len(array):
        # Edge case where index is not able to jump at all
        if elementsVisited > 0 and curIdx == 0:
            return False
        jump = array[curIdx]
        # Use mod operator to wrap around out of bound indexes.
        curIdx = (curIdx + jump) % len(array)
        elementsVisited += 1

    return elementsVisited == len(array) and curIdx == 0

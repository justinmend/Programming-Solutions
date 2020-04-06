# Time - O(N * 2^N):
# N represents the length of the input array.
# It takes O(2^N) time to generate all subsets and O(N) time to copy each subsset
# into the powerset result matrix.

# Space - O(N * 2^N):
# There were 2^N recursion calls to generate all subsets so there are O(2^N) recursion calls in our call stack frame which takes space.
# It takes O(N) space for every subset we generate.


def powerset(array):
    # Assumptions:

    # Notes:
    # 1. Given an array of unique integers.
    # 2. Return a 2d array containing the powerset
    # 3. The sets in the powerset do not need to be in any particular order.

    # Brute Force:
    # Use recusion
    # Start of with an empty set then work way up.
    # Do an initial recursion call the on an empty set then
    # start adding items from the array.

    # Add shallow copy of current set to our 2d matrix power set result.
    # Iterate through the array starting from the passed in startIdx.
    # Make sure to undo the adding of an item into the current set after a recursion call is finished.
    # This is so that we can continue generating the unique combinations of powerset.

    powerset = []

    generatePowerset(0, array, [], powerset)

    return powerset


def generatePowerset(startIdx, array, curset, powerset):
    powerset.append(curset[:])

    for i in range(startIdx, len(array)):
        curset.append(array[i])
        generatePowerset(i+1, array, curset, powerset)
        curset.pop()

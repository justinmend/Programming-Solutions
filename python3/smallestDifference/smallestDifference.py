'''

  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.


  You can assume that there will only be one pair of numbers with the smallest
  difference.
'''
# Time - O(Slog(S) + Mlog(M)):
# S represents the length of arrayOne input.
# M represents the length of arrayTwo input.
# We use the python built-in sorting function which uses the Timsort algorithm and takes O(NlogN) time.
# We perform the sort method on both input arrays.

# Space - O(S + M):
# We use the python built-in sorting function which uses the Timsort algorithm and takes O(N) space.
# We perform the sort method on both input arrays.


def smallestDifference(arrayOne, arrayTwo):
    # Assumptions:

    # Notes:
    # 1. Given two non-empty arrays of integers
    # 2. Find the pair of numbers whos absolute difference is closest to zero
    # 3. Return an array containing those two number, with the number from the first array in the first position

    # Brute Force:
    # How do we keep track of the global smallest differnce?

    # Sorth both arrays first?
    # Use two pointers to traverse through both arrays respectively
    # How do we dictate which pointer to move?

    # Take the difference between the current values from both array.
    # Compare the current difference to the smallest difference.
    # If current difference is less than smallest difference, update
    # smallest difference with the current difference.
    # Also, update result list with the values that have the smallest difference

    # Use built in python absolute value function?

    # Move the pointer of the array that currently has the smallest value?
    # How do we terminate iteration for comparing?

    arrayOne.sort()
    arrayTwo.sort()

    result = [arrayOne[0], arrayTwo[0]]
    smallestDiff = abs(result[0] - result[1])

    i = 0
    j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        currentDiff = abs(arrayOne[i] - arrayTwo[j])

        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
            result = [arrayOne[i], arrayTwo[j]]

        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1

    return result

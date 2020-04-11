'''

  Write a function that takes in a non-empty array of integers and returns the
  maximum sum that can be obtained by summing up all of the integers in a non-empty
  subarray of the input array. A subarray must only contain adjacent numbers.
'''
# Time - O(N) | Space - O(1)


def kadanesAlgorithm(array):
    # Assumptions:

    # Notes:
    # 1. Given a non-empty array
    # 2. Return the max sum that can be obtained by summing up all of the integers in a non-empty
    # subarray.
    # 3. A subarray must only contain adjacent numbers.

    # Brute Force:
    # Use dynamic programming?

    # Add previous dp max sum to current num or are
    # we better off with only the current num?

    # Keep track of the max sum
    # Compare between current current dp max sum or current max sum.
    # Adjust new max sum if necessary.

    # dp = [0] * len(array)
    # dp[0] = array[0]

    # We can save space as we don't need to use a list.
    # We only access the recent dp max sum and we can store that instead in a variable.

    dpSum = array[0]
    maxSum = array[0]

    # We start at index 1 since there is nothing to compare for the value
    # at index 0. We know the value at index 0 will allways be the max sum initially.
    for i in range(1, len(array)):

        dpSum = max(dpSum + array[i], array[i])
        maxSum = max(dpSum, maxSum)

    return maxSum

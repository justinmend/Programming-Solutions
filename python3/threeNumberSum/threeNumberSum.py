'''

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.


  If no three numbers sum up to the target sum, the function should return an
  empty array.
'''

# Time - O(Nlog(N) * N^2) -> O(N^2)
# N represents the length of the input array.
# Initially we sort the array which takes O(Nlog(N)) but O(N^2) is bigger and is the boundary
# therefore we can remove O(Nlog(N)).
# We iterate through the array once.
# For every number in the array, we iterate through the array again
# to find the other two complementary numbers and have a triplet that satisfies the target sum.

# Space - O(N):
# N represents the length of the input array.
# Worst case is all the numbers in the input array are solutions used for a triplet, so
# all the numbers in the input array will be found in the two dimensional result array.


def threeNumberSum(array, targetSum):
    # Assumptions:

    # Notes:
    # 1. Given a non-empty array of distince integers.
    # 2. Each triplet array should be sorted in ascending order.

    # Brute Force:
    # Sort the array first

    # Use two loops with three pointers.
    # Two pointers are used to increment or decrement the potential sum value

    # If potential sum equals target sum, append the triplets into the result array.

    # Return the result array as our answer

    result = []

    array.sort()

    for i in range(len(array)):
        j = i + 1
        k = len(array) - 1

        while j < k:
            potentialSum = array[i] + array[j] + array[k]
            if potentialSum == targetSum:
                result.append([array[i], array[j], array[k]])

            if potentialSum > targetSum:
                k -= 1
            else:
                j += 1

    return result

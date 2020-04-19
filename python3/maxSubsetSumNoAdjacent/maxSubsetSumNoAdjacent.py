'''
  Write a function that takes in an array of positive integers and returns the
  maximum sum of non-adjacent elements in the array.

  If a sum can't be generated, the function should return 0.
'''

# Solution 1:
# Time - O(N) | Space - O(N):
# N represents the length of the input array.
# The size of our dp list is proportional to the length of the input array.

# Solution 2:
# Time - O(N) | Space - O(N):
# We can improve the space complexity since we only access the two
# previous dp calculations we can store them in variables instead.
# We can get rid of the dp list and reduce our space complexity to constant space.


def maxSubsetSumNoAdjacent(array):
    # Assumptions:
    # 1. Are we given a non-empty array? No. It could be empty.

    # Notes:
    # 1. Given an array of positive integers. array[i] > 0
    # 2. Return the max sum of non-adjacent elements in the array.
    # 3. Return 0 if a sum can't be generated.
    # 4. Non adjacent:
    # Elements have to be one or more indexes spaced out.

    if len(array) == 0:
        return 0

    # dp = [0] * len(array) # [75, 105]
    # dp[0] = array[0]

    prevDP = 0
    recentDP = array[0]

    for i in range(1, len(array)):
        num = array[i]

        # dp[i] = max(dp[i-1], dp[i-2] + num)

        tempDP = recentDP
        recentDP = max(recentDP, prevDP + num)
        prevDP = tempDP

    # return dp[-1]
    return recentDP

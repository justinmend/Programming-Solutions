'''

  Given an array of positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the number of ways to make change for
  that target amount using the given coin denominations.

  Note that an unlimited amount of coins is at your disposal.
'''
# Time - O (D * N) | Space - O(N)
# D represents the length of the denoms list.
# N represents the value of the n input.
# For every denom in the denoms list, we iterate i up to the range of n where we try to
# determine if we can make change with the current denom value out of the current target i.
# The size ouf our dp list is proportionate to the input value n.


def numberOfWaysToMakeChange(n, denoms):
    # Assumptions:
    # Notes:
    # 1. Given an array of positive integers. denoms[i] > 0
    # 2. Given a single non-negative integer n representing a target amount of money. n >= 0

    # Brute Force:
    # Create a dp list to store previous calculations
    # Initialize dp with values of 0 and length of n + 1.
    # Add 1 to n to handle zero-based index
    dp = [0] * (n + 1)

    # Initialize dp[0] to 1, so that when we reference the dp value for the difference between target amount and denom,
    # where it happens to be a perfect exact change, we will get a value of 1 instead of 0 from dp[0].
    # A perfect exact change with a denom to the target value should count as a way to make change.
    dp[0] = 1

    # Iterate through the denoms:
    for denom in denoms:
        # For every current target amount populate dp list
        # if we can make change out of it with the current denom.
        for targetAmount in range(n + 1):
            # Make sure to only consider current target amount if they are
            # greater than or equal to the current denom. If the current target amount is less
            # than the denom then we know we can't make a change out of it.
            if targetAmount >= denom:
                # Get the cached dp value of the complement amount
                # to the current denom value necessary to make a complete change out of the current target amount.
                complementAmount = targetAmount - denom
                dp[targetAmount] = dp[targetAmount] + dp[complementAmount]

    return dp[n]

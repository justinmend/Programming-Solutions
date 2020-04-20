'''

  Given an array of positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the number of ways to make change for
  that target amount using the given coin denominations.

  Note that an unlimited amount of coins is at your disposal.
'''
# Time - O(D * N) | Space - O(N)
# D represents the length of denoms list
# N represents the integer value of n


def numberOfWaysToMakeChange(n, denoms):
    # Assumptions:
    # 1. Does not using a denom to make change out of an amount count as a way to make change? Yes.

    # Notes:
    # 1. Given an array of positive integers representing coin denominations. denoms[i] > 0
    # 2. Given a single non-negative integer n representing a target amount of money. n >= 0
    # 3. Return the number of ways to make change for the target amount

    # Brute Force:

    # PSEUDOCODE:
    # Iterate through the denoms:
    # Iterate up through n:
    # If we can make change out of the curent amount with our current denom,
    # populate current dp value.
    # Make sure to add to the current dp value the complementary changes' dp value (other ways to make change)
    # return dp[n]

    dp = [0] * (n+1)
    # Not using a denom counts as a way to make a change
    dp[0] = 1

    for denom in denoms:
        for amount in range(n + 1):
            if amount >= denom:
                dp[amount] = dp[amount] + dp[amount-denom]

    return dp[n]

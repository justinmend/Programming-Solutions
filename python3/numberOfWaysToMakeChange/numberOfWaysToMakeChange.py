'''

  Given an array of positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the number of ways to make change for
  that target amount using the given coin denominations.

  Note that an unlimited amount of coins is at your disposal.
'''
# Time - O(D * N) | Space - O(N)


def numberOfWaysToMakeChange(n, denoms):
    # Assumptions:
    # 1. Can we make a change, where n == 0?

    # Notes:
    # 1. Given an array of positive integers
    # 2. Given a non-negative integer n as the target amount of money. n >= 0

    # Brute Force:
    # What if we are given n as 0?

    # Create a dp list to store previous calculations
    # Initialize with 0 values and length of n
    dp = [0] * (n+1)

    # Initialze dp[0] to 1 so that when we encounter a denom that has an exact change for current target value
    # we can reference dp[0] as exact change and get a value of 1.
    dp[0] = 1

    for denom in denoms:
        for curTarget in range(1, n+1):
            # Only calculate for target values where target value is greater than or equal to denom.
            # If curTarget is less than current denom then we know we can't make a change for the
            # curTarget with the current denom.

            if curTarget >= denom:
                # For dp[curTarget-denom], get the complement's value from the previous calculations in dp
                dp[curTarget] = dp[curTarget] + dp[curTarget-denom]

    return dp[n]

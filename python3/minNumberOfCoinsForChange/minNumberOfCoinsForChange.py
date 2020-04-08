'''

  Given an array of positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the smallest number of coins needed to
  make change for that target amount using the given coin denominations.

  
  If it's impossible to make change for the target amount, return -1.
  
'''
# Time - O(D * N):
# D represents the length of of the denoms list input.
# N represents the value of input n.
# For every denom in the denoms list, we iterate for every amount i up to N.

# Space - O(N):
# N represents the size of our dp list used for storing our previous calculations.
# The size of our dp list is proportionate to value of input n.
def minNumberOfCoinsForChange(n, denoms):
    # Assumptions:
	
	# Notes:
	# 1. Given an array of positive integers representing coin denominations. denoms[i] > 0
	# 2. Given a non-negative integer n representing a target amount of money. n >= 0
	# 3. Return the smallest number of coins needed to make change for the target amount using the given
	# coin denominations.
	# 4. If it's impossible to make change for the target amount, return -1.
	
	# Brute Force:
	# Initialize dp list with float('inf') to have values higher than any int value
	# and represent that each amount up to n have not had their minimum number of coins for change calculated.
	
	# As we calculate the minimum number of coins for change for every amount i up to n,
	# if we happen to not be able to make change for that amount i with our current denom, 
	# we would never be able to compare the minimum number of coins for that amount i, 
	# thus the minimum number of coins for that amount would remain positive infinity in our dp list,
	# meaning we cannot make a change for that amount with our denom.
	dp = [float('inf')] * (n + 1)
	dp[0] = 0
	
	for denom in denoms:
		for amount in range(1, n+1):
			if amount >= denom:
				# We try to get the quantity of coin changes from the remaining amount after subracting denom from amount.
				remainAmount = amount - denom
				remainCoinChanges = dp[remainAmount]
				
				# SINGLE_CHANGE_DENOM represents one count of change for the current denom
				# and this is added on top of the remainCoinChanges.
				SINGLE_CHANGE_DENOM = 1
				dp[amount] = min(dp[amount], remainCoinChanges + SINGLE_CHANGE_DENOM)
	
	# Return -1 if the minimum number of coins for change for the target amount
	# is positive infinity (value higher than any other int), it means we were not able
	# to make any coin changes for the target amount with our set of denoms.
	return dp[n] if dp[n] != float('inf') else -1
	
	
	
	
	
	
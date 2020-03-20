'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Implement using DP
        # Assumptions:
        # 1. Given an input list with length greater than 1? List can actually be empty so return 0 as the answer.

        # Note:
        # 1. Cannot sell a stock before you buy one

        # Brute Force:
        # 0. Check if prices list is greater than 1. If not return 0.
        # 1. Create our dp list for caching previous calculations
        # Initialize the dp list with zero values.
        # 2. Iteratet through the prices list (start at index 1):
        # 3. Set current dp value to the max value between the (current price value minus the
        # the global min value) and the previous dp value.
        # 4. Keep track of the global min value as we iterate through the prices list.
        # Initialize the min value by setting it to the first value of the prices list
        # 5. Set the min value to the min between current min value and current price value
        # 6. Return the last value in the dp list as the result

        if len(prices) < 2:
            return 0

        dp = [0] * len(prices)
        minValue = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max((prices[i]-minValue), dp[i-1])
            minValue = min(minValue, prices[i])

        return dp[-1]

        # Time Complexity - O(N) - N is the length of prices list where we iterate through it once.
        # Space Complexity - O(N) - N is the amount of cached calculations in dp list. The dp list we created is proportionate
        # to the size of the prices list.

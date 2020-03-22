'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # Implement using DP
        # Assumptions:

        # Note:
        # Given input n will be a positive integer, that is, n > 0.

        # Brute force:
        # 1. Create a dp list to store our previous calculations. Make the size of our dp list (n+1). We want n to be inclusive
        # so that when store or access our dp calculations we use the actual number value as the index and not zero-based index.
        # 2. Initialize dp[1] and dp[2] with 1 and 2 respectively
        # 3. Check if n is equal to 1, if so return 1
        # 4. Iterate through the range of n (start at index 3 and end range of n + 1):
        # We use the previous two cached calculations. We set the current dp value
        # to the sum of dp[i-1] and dp[i-2]?
        # 5. Return the value of the last item in the dp list as our answer

        dp = [0] * (n + 1)

        if n == 1:
            return 1

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

        # Time Complexity - O(N):
        # N represents the positive integer n. We iterate through the range of n once.

        # Space Complexity - O(N):
        # N represents the total amount of cached calculations in our dp list. The size of our dp list
        # is proportionate to the value of the input n.

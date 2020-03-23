'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Implement using DP
        # Assumptions:
        # 1. Are we given an input list with a length greater than 0? No, the list can be empty

        # Note:
        # 1. We are given a list of non-negative integers. Values can be greater than or equal to 0.
        # 2. Max sum has to be from values not adjacent to each other, that is, the values are from every other index.

        # Brute Force:
        # How do we keep track of the max profit?

        # 1. Check initialy if list is empty, if so return 0.
        # Check if length of list is equal to 1, if so return first element in the list.
        # Also, check if length of list is equal to 2, if so return the max between the fist element and second element in the nums list.
        # 2. Create a dp list to cache our previous calculations.
        # Initialize dp list with zero values and length of nums.
        # Initialize dp[0] with value from nums[0].
        # 3. Iterate through nums list (start at index 1):
        # Set current dp value to the max between dp[i-1] and (current nums value + dp[i-2])
        # 4. Return last value in our dp list as the answer

        num_len = len(nums)

        if num_len <= 0:
            return 0
        if num_len == 1:
            return nums[0]
        if num_len == 2:
            return max(nums[0], nums[1])

        dp = [0] * num_len  # [2, 2, 3, 4]
        dp[0] = nums[0]

        for i in range(1, num_len):  # 3, 4
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])  # 3, 2 + 2

        return dp[-1]

        # Time Complexity - O(N):
        # N represents the total amount of values in nums list we iterate through. We iterate through nums list once.

        # Space Complexity - O(N):
        # N represents the total amount of cached calculations we have in our dp list. The size of our dp list is proportionate to the
        # size of nums list.

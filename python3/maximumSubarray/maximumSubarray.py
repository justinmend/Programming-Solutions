class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Implement using DP        
        # Assumptions:
        # 1. Will be given a valid array, that is, array length greater than 0.
                
        # Brute force:
        # Create a dp list to cache previous calculations.
        # Initialize dp[0] with first value in nums list
        dp = [0] * len(nums) # [-2, 1, -2, 4, 3, 5, 6, 1, 5]
        dp[0] = nums[0] # -2
        
        #keep track of maximum sum
        maxSum = dp[0] # 6
        
        # Iterate through the nums list (start at index 1):
        # Set current dp value with the sum of current num value and previous dp value if previous dp value is greater than 0?
        # Take the max between current dp value recently set and the current maxSum value
        for i in range(1, len(nums)): # 9, 9(exclusive)
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0) # 4 + 1
            maxSum = max(dp[i], maxSum) # max(5, 6)
        
        # Return the maximum sum after iterating through the nums list
        return maxSum
    
        # Time Complexity - O(n) - where n is the length of nums list and we iterate once through the list.
        # Space Complexity - O(n) - where n is the length of nums list. 
        # The length of dp list we create is proportionate to the length of the nums list.
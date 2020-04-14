'''
Given a collection of distinct integers, return all possible permutations.
'''
# Time - O(N * N!):
# N represents the length of the nums list input.
# Generating permutations takes O(N *N!) time.

# Space - O(N * N!):
# We make O(N * N!) recursion calls which takes up space in our call stack frame.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Implement using recursion

        # Assumptions
        # Notes
        # 1. Give a collection of distinct integers. nums[i] can negative or positive
        # 2. Return all possible permutations.

        # Brute Force:
        # PSEUDOCODE:
        # Create a recursion helper method.
        # Parameter: start index, nums array, result array

        # Base case:
        # If start index > len(nums) - 1:
        # Add current snapshot of nums array to the result array
        # return nothing to exit out of recursion

        # Iterate starting from start index until length of array
        # Swap between i index and start index?
        # Call recursion:
        # When calling the recursion method make sure to increment start index by 1?
        # Revert swap between i index and start index?

        result = []
        self.getPermute(0, nums, result)

        return result

    def getPermute(self, startIdx, nums, result):
        if startIdx > len(nums) - 1:
            result.append(nums[:])
            return

        for i in range(startIdx, len(nums)):
            self.swap(i, startIdx, nums)
            self.getPermute(startIdx + 1, nums, result)
            self.swap(i, startIdx, nums)

    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

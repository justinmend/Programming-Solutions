'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
# Time - O(log(N)) | Space - O(1)
# N represents the length of the nums array.
# Binary search takes O(log(N)) time.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Assumptions:
        # 1. No duplicate exists in the array.
        # 2. Are we given non-negative integers in the nums array? No. It can contain negative numbers.
        
        # Notes:
        # 1. Given a rotated sorted array
        # 2. Given a target value to search in the rotated sorted array
        # 3. Return the target value's index if it exist i nthe array, otherwise return -1
        # 4. Algorithm's runtime complexity must be in the order of O(log(N))
        
        # Brute Force:
        leftIdx = 0
        rightIdx = len(nums) - 1

        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx)//2
            midValue = nums[midIdx]
        
            if target == midValue:
                return midIdx
            # Check left default:
            # If midValue is greater than or equal to the left value,
            # then we know that the left part side is sorted. We would prefer
            # to apply binary search within a sublist that is already sorted.
            elif midValue >= nums[leftIdx]:
                # Go left
                if target < midValue and target >= nums[leftIdx]:
                    rightIdx = midIdx - 1
                # Go right
                else:
                    leftIdx = midIdx + 1
            # Check right:
            # If the left side sublist is not sorted then that means the
            # right side sublist must already be sorted.
            else:
                # Go right
                if target > midValue and target <= nums[rightIdx]:
                    leftIdx = midIdx + 1
                # Go left
                else:
                   rightIdx = midIdx - 1 
        
        return -1
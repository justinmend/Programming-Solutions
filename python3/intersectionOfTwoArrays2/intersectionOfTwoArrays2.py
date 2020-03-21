'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Implement using a map
        # Assumptions:
        # 1. Does the intersection have to be subsequent? No, basically just return a list with the
        # common elements between the two nums list input.

        # Note:
        # Result of our answer can be in any order

        # Brute Force:
        # 1. Map the number and the frequency it occurs in the nums1 list.
        # 2. Iterate through nums2:
        # 3. Add to result list if current number appears in the map and also decrment frequency for the number.
        # 4. Return the result list as the answer
        counts = {}
        result = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result

        # Time Complexity - O(M + N):
        # M and N represents the length of the lists nums1 and nums2 respectively.
        # We iterate through both list once.

        # Space Complexity - O(M + R):
        # M represents the amount of unique numbers in nums1 mapped to the counts dictionary. Worst case is that nums1 contains all unique numbers so
        # therefore we have to map all the unique numbers to the dictionary.
        # R represents the length of result list which contains the numbers that are in the intersection of the two input nums array (nums1 and nums2).
        # Worst case is that nums1 and nums2 consist of only unique numbers and also contain the same unique numbers. We therefore have to append the
        # entire unique elements that are both in nums1 and nums2 to our result list.

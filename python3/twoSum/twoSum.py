# Time - O(N) | Space - O(N)
# N represents the length of the nums input list


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assuming we are given unique integers

        # map the integers
        # Look for complement in map
        # avoid using same element
        dic = collections.defaultdict()

        # Time - O(N) | Space - O(N)
        for i, val in enumerate(nums):
            complement = target - val
            if complement in dic:
                return[i, dic[complement]]

            dic[val] = i

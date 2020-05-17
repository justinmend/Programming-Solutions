# Time - O(K * log(N)) | Space - O(N)
# N represents the length onf the nums input list
# K represents the top k frequent elements we only want


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given a non-empty array of integers.
        # Return the k most frequent elements.
        # Time complexity must be better than O(Nlog(N))

        # Time - O(N) | Space - O(N)
        counter = collections.Counter(nums)

        # Time - O(N) | Space - O(N)
        max_heap = [(-value, key) for key, value in counter.items()]

        # Time - O(N) | Space - O(1)
        # Worst case, building heap (heapify) takes linear time and constant space.
        heapq.heapify(max_heap)

        result = []

        # Time - O(K * log(N)) | Space - O(K)
        # K represents the top k frequent elements we only want
        # Worst case, pop takes log(N) time and constant space
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result

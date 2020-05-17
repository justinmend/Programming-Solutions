# Time - O(N) | Space - O(1)
# N represents the length of string S


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_Occurence = dict()

        # Time - O(N) | Space - O(1)
        # N represents the length of string S
        # If we are only using english alphabet letters (26 characters),
        # we only have to store 26 character keys in our dictionary therefore
        # we can assume space is constant.
        for i, letter in enumerate(S):
            last_Occurence[letter] = i

        max_distance = 0
        partitionLen = 0
        result = []

        # Time - O(N) | Space - O(1)
        # Worst case is the input string S consist only of all
        # the unique english alpahbets. At most, we would have
        # 26 integer values in our result list representing the
        # partition parts for each character therefore we can assume space is constant.
        for i, letter in enumerate(S):
            partitionLen += 1

            if last_Occurence[letter] > max_distance:
                max_distance = last_Occurence[letter]

            if i == max_distance:
                result.append(partitionLen)
                partitionLen = 0

        return result

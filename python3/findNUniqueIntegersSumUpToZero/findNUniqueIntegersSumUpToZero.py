# Time - O(N) | Space - O(N)
# N represents the integer input n value.


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Solve using symmetry.
        # Integers are still unique just symmetric to each other
        # in terms of negative and positive value.

        # odd and even case:
        # if odd add 0 to result list initially
        # else, list is initially empty

        symmetryLen = n//2
        result = []

        if n % 2 != 0:
            result.append(0)

        for i in range(1, symmetryLen+1):
            result.append(-i)
            result.append(i)

        return result

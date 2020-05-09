# Time - O(R + C) | Space - O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix) - 1
        col = 0

        # Time - O(R + C) | Space - O(1)
        while row >= 0 and col <= len(matrix[0]) - 1:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1

        return False

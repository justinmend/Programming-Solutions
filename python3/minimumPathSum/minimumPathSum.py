# Time - O(N * M) | Space - O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Assuming we can modify the grid.

        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]

        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                # Add to current cell value, the value
                # of the min between previous paths (left, up).
                grid[row][col] += min(grid[row][col-1], grid[row-1][col])

        return grid[-1][-1]

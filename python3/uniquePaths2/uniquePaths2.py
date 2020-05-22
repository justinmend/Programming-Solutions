# Time - O(N * M) | Space - O(1)
# N and M represents the height and width of the obstacle grid input.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Can only move down or right
        # Obstacle (1) and Empty space (0)
        # Return total unique paths to finish line (grid[-1][-1])

        # Brute Force:
        # Try DFS - recursion? Memory Space heavy.

        # Try DP? Assuming we can modify grid in place.

        # Can we assume we will always have a valid starting point in grid?
        # Can we assume we are given a non empty grid?
        # Can we asumme we will always have a valid finish line?

        if not obstacleGrid:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, width):
            obstacleGrid[0][i] = int(
                obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1)

        for i in range(1, height):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        for i in range(1, height):
            for j in range(1, width):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + \
                        obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]

# Time - O(N * M) | Space - O(N * M)
# N and M represent the length of rows and columns of the grid respectively.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Movements: 4
        # return min minutes for all oranges to be rotten else return -1

        queue = deque()
        counter = 0

        # Time - O(N * M) | Space - O(N * M)
        # N and M represent the length of rows and columns of the grid respectively.
        # Worst case is majority of our cells are rotten and we would have to add all of the rotten cells
        # initialy to our queue.
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    counter += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        # BFS - Queue:
        # Time - O(N * M) | Space - O(N * M)
        # N and M represent the length of rows and columns of the grid respectively.
        # Worst case is we have to add all the recently converted rotten orange cells in the grid to the queue if majority of our cells contain fresh oranges.

        simulations = 0
        while queue and counter > 0:
            simulations += 1
            for _ in range(len(queue)):
                item = queue.popleft()
                for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    row = item[0] + move[0]
                    col = item[1] + move[1]
                    if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                        counter -= 1
                        grid[row][col] = 2
                        queue.append((row, col))

        # simulations = max(simulations-1,0)
        return simulations if counter == 0 else -1

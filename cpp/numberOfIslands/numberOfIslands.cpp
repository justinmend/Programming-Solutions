/********************************************************************************** 
 * 
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
 * You may assume all four edges of the grid are all surrounded by water.
 * 
 * Example 1:
 *   11110
 *   11010
 *   11000
 *   00000
 * Answer: 1
 * 
 * Example 2:
 *   11000
 *   11000
 *   00100
 *   00011
 * Answer: 3
 *               
 **********************************************************************************/

class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        // Implement using DFS

        /*
        1. Initialy check if grid is valid
        2. Iterate through 2D array
        3. Check if cell is a valid land
        If valid, call recursion; pass in current indexes i and j
        4. increment count
        */
        int m = grid.size();
        int n = m ? grid[0].size() : 0;

        if (n == 0)
        {
            return 0;
        }

        int count = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == '1')
                {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;

        /*
        Time Complexity - O(N) - N is for number of cells in 2D array
        Since we are marking already visited cells we are not doing any unnecessary recursion
        calls therfore it is a linear time complexity.
        Space Complexity - is O(N) - Worst case is when grid has all lands
        Recursion stack is for however many cells in 2D array
        */
    }

private:
    /* 
    recursion method:
    1. check if i and j are valid boundaries or current cell is a land
    else return
    2. List of coordinate points:
    Up (-1,0)
    Down (1, 0)
    Left (0, -1)
    Right (0, 1)
    3. Mark current cell as visited; use '0'
    4. Call dfs recursion method for all 4 movements.
    */
    void dfs(vector<vector<char>> &grid, int i, int j)
    {
        if (!isValid(grid, i, j))
        {
            return;
        }
        grid[i][j] = '0';
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }

    bool isValid(vector<vector<char>> &grid, int i, int j)
    {
        int m = grid.size();
        int n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0')
        {
            return false;
        }
        return true;
    }
};
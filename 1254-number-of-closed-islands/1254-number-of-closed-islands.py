class Solution(object):
    def dfs(self, grid, i, j):
        if grid[i][j] == 1:
            return True
        if i <= 0 or i >= len(grid) - 1 or j <= 0 or j >= len(grid[0]) - 1:
            return False
        grid[i][j] = 1
        up = self.dfs(grid, i - 1, j)
        down = self.dfs(grid, i + 1, j)
        left = self.dfs(grid, i, j - 1)
        right = self.dfs(grid, i, j + 1)
        return up and down and left and right
        
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    num_islands += 1
        return num_islands

    
                    
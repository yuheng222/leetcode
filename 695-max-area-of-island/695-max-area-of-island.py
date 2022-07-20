class Solution(object):
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        area = 1
        grid[i][j] = 0
        area += self.dfs(grid, i + 1, j)
        area += self.dfs(grid, i - 1, j)
        area += self.dfs(grid, i, j + 1)
        area += self.dfs(grid, i, j - 1)
        return area
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        largest_area = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    largest_area = max(largest_area, self.dfs(grid, i, j))
        return largest_area
        
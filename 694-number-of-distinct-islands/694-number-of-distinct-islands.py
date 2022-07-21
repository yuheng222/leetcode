class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j, direction):
            if i < 0 or i >= len(grid) or j < 0  or j >= len(grid[0]):
                return
            if (i, j) in seen or not grid[i][j]:
                return
            seen.add((i, j))
            path_signature.append(direction)
            dfs(i + 1, j, "D")
            dfs(i - 1, j, "U")
            dfs(i, j + 1, "R")
            dfs(i, j - 1, "L")
            path_signature.append("0")
        
        seen = set()
        unique_islands = set()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                path_signature = []
                dfs(i, j, "0")
                if path_signature:
                    unique_islands.add(tuple(path_signature))
        return len(unique_islands)
            
        
        
        
        
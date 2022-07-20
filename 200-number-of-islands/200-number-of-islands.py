class Solution(object):
    def bfs(self, grid, i, j):
        neighbours = collections.deque([(i, j)]) # append the first found land to the neighbours queue
        while neighbours:
            row, col = neighbours.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] == '0':
                continue
            grid[row][col] = '0'
            # add neighbours into the queue
            neighbours.extend([(row + 1, col)])
            neighbours.extend([(row - 1, col)])
            neighbours.extend([(row, col + 1)])
            neighbours.extend([(row, col - 1)])
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    total += 1
                    self.bfs(grid, i, j)
        return total
            
        
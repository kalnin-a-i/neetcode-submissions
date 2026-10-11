class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        colors = [[0 for i in range(n)] for i in range(m)]
        def dfs(grid, i, j, colors):
            
            colors[i][j] = 1

            dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

            for dx, dy in zip(dxs, dys):
                if 0 <= i + dx < m  and 0 <= j + dy < n and colors[i + dx][j + dy] == 0 and grid[i + dx][j + dy] == '1':
                    dfs(grid, i + dx, j + dy, colors)
            
            colors[i][j] = 2
        
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and colors[i][j] == 0:
                    dfs(grid, i, j, colors)
                    counter += 1
        
        return counter 
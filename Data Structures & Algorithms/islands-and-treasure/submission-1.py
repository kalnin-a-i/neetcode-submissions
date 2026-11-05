class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        def bfs(grid):
            queue = deque()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        queue.append((i, j, 0))
                        seen = set([(i, j)])
            
            while queue:
                i, j, dist = queue.popleft()
                grid[i][j] = min(dist, grid[i][j])
                dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

                for dx, dy in zip(dxs, dys):
                    x, y = i + dx, j + dy

                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] < 0:
                        continue
                    if not (x, y) in seen:
                        queue.append((x, y, dist + 1))
                        seen.add((x, y))

        bfs(grid)
        return 
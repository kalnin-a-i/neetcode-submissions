class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n, m = len(grid), len(grid[0])

        q = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i, j))

        answer = 0
        k = 0
        while q:
            i, j, minute = q.popleft()

            dxs = [1, -1, 0, 0]
            dys = [0, 0, 1, -1]
            
            answer = max(answer, minute)
            for dx, dy in zip(dxs, dys):
                if 0 <= i + dx < n and 0 <= j + dy < m and grid[i+dx][j+dy] == 1:
                    q.append((i + dx, j + dy, minute + 1))
                    # visited.add((i + dx, j + dy))
                    grid[i+dx][j+dy] = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return answer
                         
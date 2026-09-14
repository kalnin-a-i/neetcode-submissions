class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        colors = [0] * numCourses

        def dfs(v):
            colors[v] = 1
            for u in graph[v]:
                c = colors[u]
                if c == 1:
                    return False
                if c == 0 and not dfs(u):
                    return False
            colors[v] = 2
            return True

        for i in range(numCourses):
            if colors[i] == 0 and not dfs(i):
                return False
        return True
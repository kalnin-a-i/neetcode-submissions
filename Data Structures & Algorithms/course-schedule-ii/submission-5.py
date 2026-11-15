class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        from collections import defaultdict

        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)

        colors = [0] * numCourses
        answer = []

        def dfs(v):
            if colors[v] == 1:
                return False  # Cycle
            if colors[v] == 2:
                return True   # Already processed

            colors[v] = 1
            for u in graph[v]:
                if not dfs(u):
                    return False

            colors[v] = 2
            answer.append(v)
            return True

        for v in range(numCourses):
            if colors[v] == 0 and not dfs(v):
                return []

        return answer[::-1]
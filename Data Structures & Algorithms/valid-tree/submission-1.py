class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        
        def dfs(v, graph, colors, parent):
            if colors[v] == 1:
                return False
            colors[v] = 1
            for u in graph[v]:
                
                if u == parent:
                    continue
                if colors[u] == 1 or not dfs(u, graph, colors, v):
                    return False
            
            colors[v] == 2
            return True

        colors = [0 for i in range(n)]
        res = dfs(0, graph, colors, -1)
        return res and min(colors) > 0
            
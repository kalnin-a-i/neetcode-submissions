class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        from collections import defaultdict
        graph_front = defaultdict(set)
        graph_invert = defaultdict(set)

        for a, b in trust:
            graph_front[a].add(b)
            graph_invert[b].add(a)

        candidates = []
        for i in range(1, n + 1):
            if len(graph_front[i]) == 0 and len(graph_invert[i]) == n-1:
                candidates.append(i)
        
        if len(candidates) == 1:
            return candidates[0]
        return -1
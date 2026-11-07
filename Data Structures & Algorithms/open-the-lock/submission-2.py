class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque 

        q = deque()
        q.append(('0000', 0))
        seen = set()
        while q:
            state, turns = q.popleft()
            if state in deadends:
                continue
            if state == target:
                return turns
            
            neigbours = []
            for i in range(len(state)):
                digit_up = str((int(state[i]) + 1) % 10)
                digit_down = str((int(state[i]) - 1) % 10)
                neigbours.append(state[:i] + digit_up +  state[i+1:])
                neigbours.append(state[:i] + digit_down +  state[i+1:])


            for n in neigbours:
                if not n in deadends and not n in seen:
                    q.append((n, turns + 1))
                    seen.add(n)
            
        return -1

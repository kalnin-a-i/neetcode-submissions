class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            if not stack or stack[-1][1] >= temperatures[i]:
                stack.append((i, temperatures[i]))
            else:
                while stack and stack[-1][1] < temperatures[i]:
                    j = stack[-1][0]
                    answer[j] = i - j
                    stack.pop()
                stack.append((i, temperatures[i]))
        return answer
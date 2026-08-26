from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1
        i = 0
        j = 1
        seen = defaultdict(int)
        seen[s[i]] += 1
        answer = 1
        while j < len(s):
            while s[j] in seen:
                seen[s[i]] -= 1
                if seen[s[i]] == 0:
                    del seen[s[i]]
                i += 1
            answer = max(answer, j-i+1)
            seen[s[j]] += 1
            j += 1
        return answer

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
        seen[s[i]] = 0
        answer = 1
        for j in range(1, len(s)):
            if s[j] in seen:
                i = max(seen[s[j]] + 1, i)
            answer = max(j - i + 1, answer)
            seen[s[j]] = j
        return answer

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        if len(s) != len(t):
            return False

        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for c, v in zip(s, t):
            count_s[c] += 1
            count_t[v] += 1
        
        for c in count_s:
            if not c in count_t or count_s[c] != count_t[c]:
                return False
        return True

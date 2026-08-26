class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "#" + str(len(s)) + "#"
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            i += 1
            s_len_s = ""
            while s[i] != "#":
                s_len_s += s[i]
                i += 1
            s_len = int(s_len_s)
            start = i + 1
            end = i + s_len + 1
            strs.append(s[start:end])
            i = end
        return strs
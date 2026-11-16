class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palidrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True 

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palidrome(s[left + 1: right + 1]) or is_palidrome(s[left: right])
            else:
                left += 1
                right -= 1
        return True
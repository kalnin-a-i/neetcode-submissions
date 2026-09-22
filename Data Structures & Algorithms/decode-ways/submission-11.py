class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s))]

        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) < 2:
            return dp[-1]

        if s[1] == "0":
            if int(s[:2]) >= 27:
                return 0
            else:
                dp[1] = 1
        else:
            if int(s[:2]) < 27:
                dp[1] = 2
            else:
                dp[1] = 1
        

        for i in range(2, len(s)):
            if s[i] == "0":
                if int(s[i-1:i+1]) >= 27 or s[i-1] == "0":
                    return 0
                else:
                    dp[i] = dp[i-2]
            else:
                if s[i-1] == "0":
                    dp[i] = dp[i-1]
                elif int(s[i-1:i+1]) < 27:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        print(dp)
        return dp[-1]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            
            dp[i] = i + 1
            # print(dp[i])
            for coin in coins:
                if i-coin >= 0 and dp[i- coin] != -1:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            # print(dp[i])
            if dp[i] == i + 1:
                dp[i] = -1 
        # print(dp)
        return dp[-1]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[j-1] < prices[j]:
                profit += prices[j] - prices[j-1]
                j += 1
            i = j
            # print(i, j)
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        min_i = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[min_i]:
                min_i = i
            else:
                answer = max(answer, prices[i] - prices[min_i])
        return answer
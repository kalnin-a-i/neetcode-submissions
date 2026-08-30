class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        cur_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            else:
                answer = max(answer, prices[i] - cur_min)
        return answer
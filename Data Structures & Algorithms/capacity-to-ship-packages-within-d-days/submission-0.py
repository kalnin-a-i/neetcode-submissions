class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) - 1
        right = sum(weights)

        def check(weights, capacity, days):
            i = 0
            for day in range(days):
                total = 0
                if i >= len(weights):
                    return True
                while i < len(weights) and total + weights[i] <= capacity:
                    total += weights[i]
                    i += 1
            if i >= len(weights):
                return True  
            return False
            
        while left + 1 < right:
            mid = (left + right) // 2
            if check(weights, mid, days):
                right = mid
            else:
                left = mid
        
        return right
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0 for i in range(len(nums) + 1)]
        
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i-1] + nums[i-1]

        ans = 0
        seen = defaultdict(int)
        for i in range(len(prefix)):
            
            if prefix[i] - k in seen:
                ans += seen[prefix[i] - k]
            seen[prefix[i]] += 1
        return ans


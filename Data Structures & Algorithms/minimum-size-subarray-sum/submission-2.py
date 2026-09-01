class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        answer = len(nums) + 1
        running_sum = 0
        for right in range(0, len(nums)):
            
            running_sum += nums[right]
            if running_sum < target:
                continue
            while left < right and running_sum >= target:
                running_sum -= nums[left]
                left += 1

            if left == right and nums[right] >= target:
                return 1

            answer = min(answer, right - left + 2)     
            
        return 0 if answer == len(nums) + 1 else answer
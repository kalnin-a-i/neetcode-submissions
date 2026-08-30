class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]

        while right - left > 1:
            mid = (right + left) // 2

            if  nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
        
        return min(nums[right], nums[left])
            
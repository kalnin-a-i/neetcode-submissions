class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        step = 0
        key = 0
        i = 0
        while i < len(nums):
            if counts[key] > step:
                nums[i] = key
                step += 1
                i += 1
            else:
                key += 1
                step = 0

        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            a = nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == -a:
                    answer.append([nums[k], nums[i], nums[j]])
                    i += 1
                    while i < len(nums) and nums[i] == nums[i-1]:
                        i += 1
                    j -= 1
                    while j > k and nums[j+1] == nums[j]:
                        j -= 1
                elif nums[i] + nums[j] < -a:
                    i += 1
                else:
                    j -= 1
        return answer
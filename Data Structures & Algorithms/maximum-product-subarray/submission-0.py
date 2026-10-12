class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_max_prod = nums[0]
        cur_min_prod = nums[0]

        for i in range(1, len(nums)):
            cur_min_prod, cur_max_prod = min(cur_min_prod * nums[i], 
                                cur_max_prod * nums[i],
                                nums[i]), \
                                max(cur_min_prod * nums[i], 
                                cur_max_prod * nums[i],
                                nums[i])

            # print(nums[i], cur_min_prod, cur_max_prod)
            ans = max(ans, cur_max_prod)

        return ans
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return nums
        cur_i = 0
        new_i = (cur_i + k) % n
        i = 0
        while i < n:
            # print(nums[cur_i], nums[new_i])
            # print(cur_i, new_i)
            nums[cur_i], nums[new_i] = nums[new_i], nums[cur_i]
            # print(nums)
            new_i = (new_i + k) % n
            if new_i == cur_i:
                cur_i += 1
                new_i = (cur_i + k) % n
                i += 1
            i += 1
            
        return nums
        # for i in range(k):
        #     new_i = (i + k) % n
        #     nums[i], nums[new_i] = nums[new_i], nums[i]

        # [1,2,3,4,5,6,7,8]
        # [4,5,6,1,2,3,7,8]
        # new_i = k-1
        # for i in range(n-1, 2 * k - 1, -1):
        #     nums[i], nums[new_i] = nums[new_i], nums[i]
        #     new_i -= 1

        # for i in range()
        # [4,7,8,1,2,3,5,6]
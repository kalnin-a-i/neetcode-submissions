class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer = 0

        def enum_all_subsets(cur_xor, i):
            nonlocal answer
            if i >= len(nums):
                return
            enum_all_subsets(cur_xor, i + 1)
            cur_xor = cur_xor ^ nums[i]
            answer += cur_xor
            enum_all_subsets(cur_xor, i + 1)

        enum_all_subsets(0, 0)
        return answer
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_starts = set()
        if len(nums) == 0:
            return 0
        for num in nums:
            if not num - 1 in nums_set:
                seq_starts.add(num)
        max_length = 1

        for start in seq_starts:
            length = 1
            last = start
            while last + 1 in nums_set:
                last += 1
                length += 1

            if length > max_length:
                max_length = length
        return max_length
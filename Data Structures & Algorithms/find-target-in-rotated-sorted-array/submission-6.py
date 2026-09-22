class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r - 1:
            mid = (r + l) // 2 

            if nums[mid] > nums[mid] + 1:
                break
            
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        
        if nums[l] > nums[r]:
            shift = l + 1
        else:
            shift = 0
        print(shift)
        l, r = 0, len(nums) - 1
        n = len(nums)
        while l < r - 1:
            mid = (l + r) // 2
            if nums[(mid + shift) % n] == target:
                return (mid + shift) % n

            if nums[(mid + shift) % n] < target:
                l = mid
            else:
                r = mid
        if nums[(l + shift)%n] == target:
            return (l + shift)%n
        if nums[(r + shift)%n] == target:
            return (r + shift)%n
        return -1
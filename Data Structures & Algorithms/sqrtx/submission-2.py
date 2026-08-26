class Solution:
    def mySqrt(self, x: int) -> int:
        top = x
        down = 0
        if x == 1:
            return 1
        while top - down > 1:
            mid = (top + down) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                top = mid
            else:
                down = mid
        return down
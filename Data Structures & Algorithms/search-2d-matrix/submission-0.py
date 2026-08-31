class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        if matrix[0][0] == target or matrix[rows - 1][cols - 1] == target:
            return True
        # print(left, right)
        while right - left > 1:
            # print(left, right)
            mid = (left + right) // 2
            i = mid // cols
            j = mid % cols

            if matrix[i][j] <= target:
                left = mid
            else:
                right = mid
            
        i = left // cols
        j = left % cols
        # print(i, j)
        return matrix[i][j] == target

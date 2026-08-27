class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        [1,  2, 4, 8]
        [10,11,12,13]
        [14,20,30,40]
        
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


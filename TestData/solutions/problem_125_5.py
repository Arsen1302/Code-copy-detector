class Solution:
    def solution_125_5(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        
        top = 0
        right = cols-1
        
        bottom = rows-1
        left = 0

        while bottom >= top and left <= right:
            if matrix[bottom][left] == target:
                return True
            if matrix[bottom][left] > target:
                bottom -= 1
            elif matrix[bottom][left] < target:
                left += 1
        return False
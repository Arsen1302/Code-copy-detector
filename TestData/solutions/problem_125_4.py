class Solution:
    def solution_125_4(self, matrix, target):
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0: 
            return False
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
		```
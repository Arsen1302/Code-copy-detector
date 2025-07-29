class Solution:
    def solution_1068_3(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row, col = [0]*m, [0]*n
        for i, j in product(range(m), range(n)): 
            if mat[i][j]: row[i], col[j] = 1 + row[i], 1 + col[j]
        return sum(mat[i][j] and row[i] == 1 and col[j] == 1 for i, j in product(range(m), range(n)))
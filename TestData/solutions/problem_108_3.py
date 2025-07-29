class Solution:
    def solution_108_3(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        prev, curr = [0]*n, [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    curr[j] = min(curr[j-1] if j > 0 else 0,
                                  prev[j-1] if j > 0 else 0,
                                  prev[j]) + 1
                    if curr[j] > result:
                        result = curr[j]
            prev, curr = curr, [0]*n
        return result*result
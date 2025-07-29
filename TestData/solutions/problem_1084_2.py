class Solution:
    def solution_1084_2(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n,m=len(rowSum),len(colSum)
        matrix = [[0 for i in range(m)] for j in range(n)]
        total = 0
        for i in range(n):
            matrix[i][0] = rowSum[i]
            total += rowSum[i]
        for c in range(m):
            if total == colSum[c]:
                break
            else:
                nextTotal = total - colSum[c]
                total = nextTotal
                for r in range(n):
                    curr = min(matrix[r][c],total)
                    matrix[r][c] -= curr
                    total -= curr
                    if c+1 < m:
                        matrix[r][c+1] = curr
                total = nextTotal
        return matrix
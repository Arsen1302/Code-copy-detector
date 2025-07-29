class Solution:
    def solution_1084_3(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R = sorted([r, i] for i, r in enumerate(rowSum))
        C = sorted([c, j] for j, c in enumerate(colSum))
        # print(R, C)
        i, j, m, n = 0, 0, len(rowSum), len(colSum)
        ans = [[0]*n for _ in range(m)]
        while i < m and j < n:
            r, ir = R[i]
            c, jc = C[j]
            if r == c:
                ans[ir][jc] = r
                i += 1
                j += 1
            elif r < c:
                ans[ir][jc] = r
                C[j][0] = c-r
                i += 1
            else:
                ans[ir][jc] = c
                R[i][0] = r-c
                j += 1
        return ans
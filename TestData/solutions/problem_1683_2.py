class Solution:
    def solution_1683_2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # ps is our 2D array to store prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        ps[1][1] = grid[0][0]

        # prepare prefix sum
        for i in range(2, n + 1):
            ps[1][i] = grid[0][i - 1] + ps[1][i - 1]
        for i in range(2, m + 1):
            ps[i][1] = grid[i - 1][0] + ps[i - 1][1]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + grid[i - 1][j - 1]

        # go through each square of (9 cells)
        res = 0
        for i in range(3, m + 1):
            for j in range(3, n + 1):
                curr = ps[i][j] - grid[i - 2][j - 3] - grid[i - 2][j - 1]
                curr = curr - ps[i][j - 3] - ps[i - 3][j] + ps[i - 3][j - 3]
                res = max(res, curr)
                # print(ps[i][j])
        return res
class Solution:
    def solution_89_1_1(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        def solution_89_1_2(i, j):
            grid[i][j] = '2'
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ii, jj = i+di, j+dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                    solution_89_1_2(ii, jj)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    solution_89_1_2(i, j)
                    ans += 1
        return ans
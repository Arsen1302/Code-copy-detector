class Solution:
    def solution_495_3(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [max(x) for x in grid]
        col = [max(x) for x in zip(*grid)]
        ans = 0 
        for i in range(m):
            for j in range(n): 
                ans += min(row[i], col[j]) - grid[i][j]
        return ans
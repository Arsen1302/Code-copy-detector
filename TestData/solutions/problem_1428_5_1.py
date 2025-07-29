class Solution:
    def solution_1428_5_1(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        @cache
        def solution_1428_5_2(i, j):
            nonlocal m, n
            if i + 1 < m and j - 1 > -1 and j + 1 < n and grid[i][j] == 1:
                left = solution_1428_5_2(i+1, j-1)
                bottom = solution_1428_5_2(i+1, j)
                right = solution_1428_5_2(i+1, j+1)
                return 1 + min(left, bottom, right)
            else:
                return grid[i][j]
        
        @cache
        def solution_1428_5_3(i, j):
            nonlocal m, n
            if i - 1 > -1 and j - 1 > -1 and j + 1 < n and grid[i][j] == 1:
                left = solution_1428_5_3(i-1, j-1)
                top = solution_1428_5_3(i-1, j)
                right = solution_1428_5_3(i-1, j+1)
                return 1 + min(left, top, right)
            else:
                return grid[i][j]
            
        ans = 0
            
        for i in range(m):
            for j in range(n):
                if solution_1428_5_2(i, j) != 0:
                    ans += solution_1428_5_2(i, j) - 1
                if solution_1428_5_3(i, j) != 0:
                    ans += solution_1428_5_3(i, j) - 1

        return ans
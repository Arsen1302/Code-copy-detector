class Solution:
    def solution_1078_1_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def solution_1078_1_2(i, j): 
            """Return maximum &amp; minimum products ending at (i, j)."""
            if i == 0 and j == 0: return grid[0][0], grid[0][0]
            if i < 0 or j < 0: return -inf, inf
            if grid[i][j] == 0: return 0, 0
            mx1, mn1 = solution_1078_1_2(i-1, j) # from top
            mx2, mn2 = solution_1078_1_2(i, j-1) # from left 
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j]
            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = solution_1078_1_2(m-1, n-1)
        return -1 if mx < 0 else mx % 1_000_000_007
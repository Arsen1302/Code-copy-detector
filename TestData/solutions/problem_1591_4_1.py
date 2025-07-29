class Solution:
    def solution_1591_4_1(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def solution_1591_4_2(i, j):
            """Return min cost of moving from (i, j) to bottom row."""
            if i == m-1: return grid[i][j]
            ans = inf 
            for jj in range(n): 
                ans = min(ans, grid[i][j] + solution_1591_4_2(i+1, jj) + moveCost[grid[i][j]][jj])
            return ans 
        
        return min(solution_1591_4_2(0, j) for j in range(n))
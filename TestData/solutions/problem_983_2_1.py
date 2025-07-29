class Solution:
    def solution_983_2_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def solution_983_2_2(i, j, jj): 
            """Return max cherries picked so far when two robots are at (i, j) and (i, jj)"""
            if not (0 <= i < m and 0 <= j < n and 0 <= jj < n) or j > i or jj < n-1-i or jj < j: return 0
            if i == 0: return grid[0][0] + grid[0][n-1]
            return grid[i][j] + (jj != j) * grid[i][jj] + max(solution_983_2_2(i-1, k, kk) for k in range(j-1, j+2) for kk in range(jj-1, jj+2))
                    
        return max(solution_983_2_2(m-1, j, jj) for j in range(n) for jj in range(n))
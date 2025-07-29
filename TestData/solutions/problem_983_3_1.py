class Solution:
    def solution_983_3_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def solution_983_3_2(i, j, k): 
            """Return maximum cherries picked when two robots start at (i, j) and (i, k)."""
            if not 0 <= j <= k < n: return -inf 
            if i == m: return 0
            ans = grid[i][j] + (j!=k) * grid[i][k]
            return ans + max(solution_983_3_2(i+1, jj, kk) for jj in (j-1, j, j+1) for kk in (k-1, k, k+1))
        
        return solution_983_3_2(0, 0, n-1)
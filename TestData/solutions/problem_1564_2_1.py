class Solution:
    def solution_1564_2_1(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @cache
        def solution_1564_2_2(i, j, v): 
            """Return True if value of v at (i, j) is possible."""
            if i == m-1 and j == n-1: return v == 0 
            for ii, jj in (i+1, j), (i, j+1): 
                if 0 <= ii < m and 0 <= jj < n: 
                    if grid[ii][jj] == '(': vv = v+1
                    else: vv = v-1
                    if 0 <= vv <= min(ii+jj+1, m+n-ii-jj) and solution_1564_2_2(ii, jj, vv): return True 
            return False 
        
        return solution_1564_2_2(0, 0, 1)
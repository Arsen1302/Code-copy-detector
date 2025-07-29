class Solution:
    def solution_661_4_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mask = 0
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1: start = (i, j)
                if grid[i][j] in (-1, 1): mask ^= 1 << i*n+j
        
        @cache
        def solution_661_4_2(i, j, mask): 
            """Return unique paths from (i, j) to end"""
            if grid[i][j] == 2 and mask == (1<<m*n) - 1: return 1
            ans = 0
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n: 
                    kk = ii*n + jj 
                    if not mask &amp; 1<<kk: ans += solution_661_4_2(ii, jj, mask ^ 1<<kk)
            return ans 
                
        return solution_661_4_2(*start, mask)
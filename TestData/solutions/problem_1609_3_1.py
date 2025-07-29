class Solution:
    def solution_1609_3_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def solution_1609_3_2(i, j):
            ans = 1
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] < grid[i][j]: ans += solution_1609_3_2(ii, jj)
            return ans % 1_000_000_007
        
        return sum(solution_1609_3_2(i, j) for i in range(m) for j in range(n)) % 1_000_000_007
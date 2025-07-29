class Solution:
    def solution_1052_1_1(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def solution_1052_1_2(i, j, d): 
            """Traverse the grid to find cycle via backtracking."""
            if grid[i][j] != "BLACK": 
                val = grid[i][j]
                grid[i][j] = "GRAY" # mark visited in this trial
                for ii, jj, dd in ((i-1, j, -2), (i, j-1, -1), (i, j+1, 1), (i+1, j, 2)):
                    if 0 <= ii < m and 0 <= jj < n and d + dd != 0: # in range &amp; not going back 
                        if grid[ii][jj] == "GRAY": return True #cycle found 
                        if grid[ii][jj] == val: solution_1052_1_2(ii, jj, dd)
                grid[i][j] = val 
        
        for i in range(m):
            for j in range(n):
                if solution_1052_1_2(i, j, 0): return True
                grid[i][j] = "BLACK" # mark "no cycle"
        return False
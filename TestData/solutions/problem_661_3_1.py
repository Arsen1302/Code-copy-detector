class Solution:
    def solution_661_3_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # dimensions 
        empty = 0 
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1: start = (i, j)
                elif grid[i][j] == 0: empty += 1 # empty squares 
        
        def solution_661_3_2(i, j, empty): 
            """Count paths via backtracking."""
            nonlocal ans 
            if grid[i][j] == 2: 
                if empty == -1: ans += 1
                return 
            grid[i][j] = -1 # mark as visited 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != -1: 
                    solution_661_3_2(ii, jj, empty-1)
            grid[i][j] = 0 # backtracking
        
        ans = 0 
        solution_661_3_2(*start, empty)
        return ans
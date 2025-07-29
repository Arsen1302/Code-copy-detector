class Solution:
    def solution_1428_1_1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vals = [[inf]*n for _ in range(m)]
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 0: vals[i][j] = 0
                elif j == 0: vals[i][j] = 1
                else: vals[i][j] = min(vals[i][j], 1 + vals[i][j-1])
                if grid[i][~j] == 0: vals[i][~j] = 0
                elif j == 0: vals[i][~j] = 1
                else: vals[i][~j] = min(vals[i][~j], 1 + vals[i][~j+1])
        
        def solution_1428_1_2(vals): 
            """Return count of pyramid in given grid."""
            ans = 0 
            for j in range(n):
                width = 0
                for i in range(m): 
                    if vals[i][j]: width = min(width+1, vals[i][j])
                    else: width = 0
                    ans += max(0, width-1)
            return ans 
        
        return solution_1428_1_2(vals) + solution_1428_1_2(vals[::-1])
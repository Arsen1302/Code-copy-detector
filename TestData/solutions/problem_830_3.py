class Solution:
    def solution_830_3(self, grid):
        m, n = len(grid), len(grid[0])
        row = defaultdict(int)
        col = defaultdict(int)
        tot = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    tot += 1
             
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and row[i] ==1 and col[j] == 1:
                    res += 1
        return tot - res
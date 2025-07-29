class Solution:
    def solution_89_4_1(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0: return 0
        
        r, c = len(grid), len(grid[0])
        dsu = DSU(r * c)
        
        # solution_89_4_4 an island with its adjacent islands
        for i in range(r):
            for j in range(c):
                if int(grid[i][j]) == 1:
                    
                    # add this island first
                    dsu.numIsl += 1
                    
                    # solution_89_4_4 4 adjacent islands if exist
                    if i - 1 >= 0 and int(grid[i - 1][j]) == 1:
                        dsu.solution_89_4_4((i - 1) * c + j, i * c + j)
                    if i + 1 < r and int(grid[i + 1][j]) == 1:
                        dsu.solution_89_4_4(i * c + j, (i + 1) * c + j)
                    if j - 1 >= 0 and int(grid[i][j - 1]) == 1:
                        dsu.solution_89_4_4(i * c + (j - 1), i * c + j)
                    if j + 1 < c and int(grid[i][j + 1]) == 1:
                        dsu.solution_89_4_4(i * c + j, i * c + (j + 1))
                            
        return dsu.numIsl
    
class DSU:
    def solution_89_4_2(self, num):
        self.numIsl = 0
        self.par = list(range(num))
        self.rnk = [0] * num

    def solution_89_4_3(self, x):
        if self.par[x] != x:
            self.par[x] = self.solution_89_4_3(self.par[x])
        return self.par[x]
    
    def solution_89_4_4(self, x, y):
        xr, yr = self.solution_89_4_3(x), self.solution_89_4_3(y)
        if xr == yr:
			return
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.numIsl -= 1
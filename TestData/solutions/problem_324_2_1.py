class Solution:
    def solution_324_2_1(self, M: List[List[int]]) -> int:
        dsu = DSU(len(M))
        for i, r in enumerate(M):
            for j, v in enumerate(r):
                if j > i - 1: break
                if v == 1:
                    dsu.solution_324_2_4(i, j)
        return dsu.numFrdCir
    
class DSU:
    def solution_324_2_2(self, num):
        self.numFrdCir = num
        self.par = list(range(num))
        self.rnk = [0] * num
        
    def solution_324_2_3(self, x):
        if self.par[x] != x:
            self.par[x] = self.solution_324_2_3(self.par[x])
        return self.par[x]
    
    def solution_324_2_4(self, x, y):
        xr, yr = self.solution_324_2_3(x), self.solution_324_2_3(y)
        if xr == yr:
			return
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.numFrdCir -= 1
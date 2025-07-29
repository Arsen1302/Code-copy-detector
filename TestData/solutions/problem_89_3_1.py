class UF:
    def solution_89_3_1(self, n):
        self.p = [i for i in range(n)]
        self.n = n
        self.size = n

    def solution_89_3_2(self, i, j):
        pi, pj = self.solution_89_3_3(i), self.solution_89_3_3(j)
        if pi != pj:
            self.size -= 1
            self.p[pj] = pi

    def solution_89_3_3(self, i):
        if i != self.p[i]:
            self.p[i] = self.solution_89_3_3(self.p[i])
        return self.p[i]


class Solution:
    def solution_89_3_4(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    d[i, j] = idx
                    idx += 1
        uf = UF(idx)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        uf.solution_89_3_2(d[i-1, j], d[i, j])
                    if j > 0 and grid[i][j-1] == '1':
                        uf.solution_89_3_2(d[i, j-1], d[i, j])
        return uf.size
class Solution:
    def solution_80_5_1(self, i, j):
        if j == (self.n - 1) and i == (self.m - 1):
            return max(1, 1 - self.grid[i][j])
        if j == self.n or i == self.m :
            return 99999
        if self.ans[i][j] != -99999:
            return self.ans[i][j]
        anss = min(self.solution_80_5_1(i+1, j), self.solution_80_5_1(i, j+1)) - self.grid[i][j]
        if anss > 0 :
            self.ans[i][j] = anss
        else:
            self.ans[i][j] = 1
        return self.ans[i][j]

    def solution_80_5_2(self, dungeon: List[List[int]]) -> int:
        self.m = len(dungeon)
        self.n = len(dungeon[0])
        self.grid = dungeon
        self.ans = [[-99999 for _ in range(self.n)] for _ in range(self.m)]
        return self.solution_80_5_1(0,0)
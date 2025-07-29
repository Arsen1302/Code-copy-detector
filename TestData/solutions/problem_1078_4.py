class Solution:
    def solution_1078_4(self, grid):
        m, n = len(grid), len(grid[0])

        max_ = [[0]*n for _ in range(m)]
        min_ = [[0]*n for _ in range(m)]

        max_[0][0] = min_[0][0] = grid[0][0]

        for i in range(1,m):
            max_[i][0] = grid[i][0]*max_[i-1][0]
            min_[i][0] = grid[i][0]*min_[i-1][0]

        for j in range(1,n):
            max_[0][j] = grid[0][j]*max_[0][j-1]
            min_[0][j] = grid[0][j]*min_[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] > 0:
                    max_[i][j] = max(max_[i-1][j],max_[i][j-1])*grid[i][j]
                    min_[i][j] = min(min_[i-1][j],min_[i][j-1])*grid[i][j]
                else:
                    max_[i][j] = min(min_[i-1][j],min_[i][j-1])*grid[i][j]
                    min_[i][j] = max(max_[i-1][j],max_[i][j-1])*grid[i][j]

        return max_[-1][-1]%(10**9+7) if max_[-1][-1] >= 0 else -1
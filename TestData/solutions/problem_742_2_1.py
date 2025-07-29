class Solution:
    NO_CLEAR_PATH = -1

    def solution_742_2_1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        dp = [[None] * n for _ in range(n)]

        def solution_742_2_2(i, j):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] == 1: return self.NO_CLEAR_PATH
            if (i, j) == (n-1, n-1): return 1
            #if dp[i][j] is not None: return dp[i][j] # memoization removed

            result = math.inf
            grid[i][j] = 1

            for di, dj in dirs:
                ii, jj = i + di, j + dj

                cellsToTarget = solution_742_2_2(ii, jj)
                if cellsToTarget < 1: continue
                result = min(result, 1 + cellsToTarget)

            if result == math.inf: result = self.NO_CLEAR_PATH
            grid[i][j] = 0
            dp[i][j] = result
            return result
        
        return solution_742_2_2(0, 0)
class Solution:
    def solution_1689_1(self, grid: List[List[int]], k: int) -> int:
        dp = [[[0 for i in range(k)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        rem = grid[0][0] % k
        dp[0][0][rem] = 1
        for i in range(1, len(grid[0])):
            dp[0][i][(rem + grid[0][i]) % k] = 1
            rem = (rem + grid[0][i]) % k
        rem = grid[0][0] % k
        for j in range(1, len(grid)):
            dp[j][0][(rem + grid[j][0]) % k] = 1
            rem = (rem + grid[j][0]) % k
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                for rem in range(k):
                    dp[i][j][(rem + grid[i][j]) % k] = dp[i - 1][j][rem] + dp[i][j - 1][rem]
        return dp[-1][-1][0] % (10**9 + 7)
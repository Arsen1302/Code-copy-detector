class Solution:
    def solution_268_5(self, S, M, N):
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for s in S:
            x, y = s.count('1'), s.count('0')
            for i in range(N - x, -1, -1):
                for j in range(M - y, -1, -1):
                    dp[i + x][j + y] = max(dp[i + x][j + y], dp[i][j] + 1)
        return dp[-1][-1]
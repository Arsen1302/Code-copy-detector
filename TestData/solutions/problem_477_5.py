class Solution:
    def solution_477_5(self, n, flights, src, dst, k):
        dp = [[float("inf")]*(k+2) for _ in range(n)]
        dp[src][0] = 0

        for col in range(1,k+2):
            for row in range(n):
                dp[row][col] = dp[row][col-1]
            for s,e,v in flights:
                dp[e][col] = min(dp[s][col-1] + v,dp[e][col])

        return dp[dst][-1] if dp[dst][-1] != float("inf") else -1
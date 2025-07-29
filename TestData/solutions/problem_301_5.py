class Solution:
    def solution_301_5(self, s: str) -> int:
        
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for r in range(N-2, -1, -1):
            for c in range(r+1, N):
                if s[r] == s[c]:
                    dp[r][c] = 2 + dp[r+1][c-1] 
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c-1])
        return dp[0][-1]
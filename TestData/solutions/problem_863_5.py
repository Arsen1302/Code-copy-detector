class Solution:
    def solution_863_5(self, s: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        r = s[::-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1] == r[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return len(s)-dp[-1][-1]
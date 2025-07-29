class Solution:
    def solution_180_2(self, n):
        if n == 0:
            return 1

        if n == 1:
            return 10

        dp = [0]*(n+1)

        dp[0], dp[1] = 1, 10

        for i in range(2,n+1):
            dp[i] = (dp[i-1]-dp[i-2])*(10-(i-1)) + dp[i-1]

        return dp[-1]
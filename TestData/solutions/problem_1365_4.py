class Solution:
    def solution_1365_4(self, nextVisit):
        n, mod = len(nextVisit), 10**9 + 7
        dp = [0]*n 

        for i in range(1,n):
            dp[i] = (dp[i-1] + (dp[i-1] - dp[nextVisit[i-1]] + 1) + 1)%mod

        return dp[-1]
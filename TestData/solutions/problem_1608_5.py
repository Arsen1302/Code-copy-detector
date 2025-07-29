class Solution:
    def solution_1608_5(self, n, delay, forget):
        dp, total = [0]*n, 0

        dp[0] = 1

        for i in range(1,n):
            dp[i] = total = total + dp[i-delay] - dp[i-forget]

        return sum(dp[n-forget:])%(10**9+7)
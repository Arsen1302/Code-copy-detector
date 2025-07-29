class Solution:
    def solution_1365_2(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        mod = int(1e9+7)
        for i in range(n-1):
            # dp[i]: moves need to visited `i`
            # dp[i] - dp[nextVisit[i]] + 1: odd visit at i, then back to nextVisited[i] (+1), then move back to i (dp[i] - dp[nextVisit[i]]) for even visit
            # dp[i] + 1: even visit at i, then from i to i+1
            dp[i+1] = (dp[i] - dp[nextVisit[i]] + 1 + dp[i] + 1) % mod
        return dp[n-1]
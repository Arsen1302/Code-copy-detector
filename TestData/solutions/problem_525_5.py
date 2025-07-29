class Solution:
    def solution_525_5(self, n: int, k: int, maxPts: int) -> float:
        dp = collections.deque([float(i <= n) for i in range(k, k + maxPts)])
        s = sum(dp)
        for i in range(k):
            dp.appendleft(s / maxPts)
            s += dp[0] - dp.pop()
        
        return dp[0]
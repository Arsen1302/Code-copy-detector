class Solution:
    def solution_180_5(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(1, n+1):
            count = 0
            for j in range(i):
                count += dp[j]*(9-j)
            dp[i] = count
        return sum(dp)
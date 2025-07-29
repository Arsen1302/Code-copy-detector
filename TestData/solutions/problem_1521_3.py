class Solution:
    def solution_1521_3(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
		# edge case handling
        if numCarpets * carpetLen >= n:
            return 0
        if carpetLen == 1:
            return max(sum([int(c) for c in floor]) - numCarpets, 0)
		# DP initialization
        dp = [[None] * (numCarpets + 1) for _ in range(n + 1)]
        for j in range(numCarpets + 1):
            dp[0][j] = 0
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + int(floor[i - 1])
		# DP transition formula
        for i in range(1, n + 1):
            for j in range(1, numCarpets + 1):
                dp[i][j] = min(dp[i - 1][j] + int(floor[i - 1]), dp[max(i - carpetLen, 0)][j - 1])
        return dp[n][numCarpets]
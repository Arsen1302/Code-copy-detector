class Solution(object):
    def solution_764_2_1(self, n, dp):
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        if dp[n] != 0: return dp[n]
        dp[n] = self.solution_764_2_1(n - 1, dp) + self.solution_764_2_1(n - 2, dp) + self.solution_764_2_1(n - 3, dp)
        return dp[n]
    def solution_764_2_2(self, n):
        dp = [0] * (n + 1)
        return self.solution_764_2_1(n, dp)
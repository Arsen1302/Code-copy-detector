class Solution:
    def solution_1685_1(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for l in range(1, (n - i) // 2 + 1):
                if s[i : i + l] == s[i + l : i + 2 * l]:
                    dp[i] = max(dp[i], 1 + dp[i + l])
        return dp[0]
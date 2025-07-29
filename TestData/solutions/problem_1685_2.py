class Solution:
    def solution_1685_2(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp, M = [1] * n, [1] * n
        for i in range(n - 2, -1, -1):
            for l in range(1, (n - i) // 2 + 1):
                if dp[i] >= M[i + l] + 1:
                    break
                if s[i : i + l] == s[i + l : i + 2 * l]:
                    dp[i] = max(dp[i], 1 + dp[i + l])
            M[i] = max(dp[i], M[i + 1])
        return dp[0]
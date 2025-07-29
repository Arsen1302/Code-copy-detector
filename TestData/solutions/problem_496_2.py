class Solution:
    def solution_496_2(self, n: int) -> float:
        if n > 4275: return 1                                        # handle special case
        n = n // 25 + (n%25 > 0)                                     # count size of tabulation
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[n][n] = 1
        for i in range(n, 0, -1):                                    # starting from (n, n) for each soup
            for j in range(n, 0, -1):
                for a, b in [[4, 0], [3, 1], [2, 2], [1, 3]]:
                    dp[max(0, i-a)][max(0, j-b)] += dp[i][j] * 0.25  # traverse backwards from (n,n) to (0,0)
        ans = dp[0][0] / 2                                           # half the probability when `a` &amp; `b` both use up at the same time
        for j in range(1, n+1):                                      # plus when `a` use up first
            ans += dp[0][j]
        return ans
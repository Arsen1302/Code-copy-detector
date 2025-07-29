class Solution:
    def solution_1725_3(self, S, K, M):
        N = len(S)
        P = '2357'
        help = lambda a, b: a not in P and b in P
        if not help(S[-1], S[0]) or K * M > N: return 0
        dp = [1] * (N - M)
        mod = 10 ** 9 + 7
        for j in range(1, K):
            dp2 = [0] * (N - M)
            for i in range(j * M - 1, N - M):
                dp2[i] = (dp2[i - 1] + dp[i - M] * int(help(S[i], S[i + 1]))) % mod
            dp = dp2
        return dp[-1]
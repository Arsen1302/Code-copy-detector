class Solution:
    def solution_436_3(self, s: str) -> int:
        n, MOD = len(s), 10 ** 9 + 7
        s = [ord(c) - ord('a') for c in s]
        charcnt, first, last = [[0] * n for _ in range(n)], [-1] * 4, [-1] * 4
        for i in range(n):
            if first[s[i]] == -1: first[s[i]] = i
            last[s[i]] = i
            cs = set()
            for j in range(i, n):
                cs.add(s[j])
                charcnt[i][j] = len(cs)
        left, right = [[-1] * 4 for _ in range(n)], [[-1] * 4 for _ in range(n)]
        for i in range(1, n):
            left[i] = left[i - 1][:]
            left[i][s[i - 1]] = i - 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1][:]
            right[i][s[i + 1]] = i + 1
        ans, dp = charcnt[0][n - 1], [[0] * n for _ in range(n)]
        for l, r in zip(first, last): dp[l][r] = 1
        for step in range(1, n):
            for l in range(step):
                r = l + n - step
                if not dp[l][r]: continue
                for nk in range(4):
                    nl, nr = right[l][nk], left[r][nk]
                    if nr < r and nl > l and nl < nr:
                        dp[nl][nr] = (dp[nl][nr] + dp[l][r]) % MOD
                ans = (ans + dp[l][r] * (1 + charcnt[l + 1][r - 1])) % MOD
        return ans
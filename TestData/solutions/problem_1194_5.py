class Solution:
    def solution_1194_5(self, s: str) -> int:
        MOD = 10**9 + 7
        groups = [list(g) for k, g in itertools.groupby(s)]
        res = 0
        for g in groups:
            n = len(g)
            res += (n + 1) * n // 2
        return res % MOD
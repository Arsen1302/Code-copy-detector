class Solution:
    def solution_1725_1_1(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9 + 7

        def solution_1725_1_2(c):
            return c in ['2', '3', '5', '7']

        @lru_cache(None)
        def solution_1725_1_3(i, k):
            if k == 0 and i <= n:
                return 1
            if i >= n:
                return 0

            ans = solution_1725_1_3(i+1, k)  # Skip
            if solution_1725_1_2(s[i]) and not solution_1725_1_2(s[i-1]):  # Split
                ans += solution_1725_1_3(i+minLength, k-1)
            return ans % MOD

        if not solution_1725_1_2(s[0]) or solution_1725_1_2(s[-1]): return 0

        return solution_1725_1_3(minLength, k-1)
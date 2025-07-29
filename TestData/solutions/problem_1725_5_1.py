class Solution:
    def solution_1725_5_1(self, s: str, k: int, minLength: int) -> int:
        n, primes, mod = len(s), set('2357'), (10 ** 9) + 7
        @cache
        def solution_1725_5_2(i, at_start, k):
            if i == n: return int(k == 0)
            if i > n or k == 0 or s[i] not in primes and at_start: return 0
            if s[i] in primes:
                if at_start: return solution_1725_5_2(i + minLength - 1, False, k)
                else: return solution_1725_5_2(i + 1, False, k)
            return (solution_1725_5_2(i + 1, True, k - 1) + solution_1725_5_2(i + 1, False, k)) % mod
        return solution_1725_5_2(0, True, k)
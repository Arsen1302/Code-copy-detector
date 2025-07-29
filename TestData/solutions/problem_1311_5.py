class Solution:
    def solution_1311_5(self, n: int) -> int:
        p = 10**9 + 7

        if n % 2 == 0:
            return pow(20, n // 2, p)
        else:
            return (5 * pow(20, (n-1) // 2, p)) % p
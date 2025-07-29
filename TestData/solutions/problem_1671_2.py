class Solution:
    def solution_1671_2(self, n: int) -> int:
		# alternatively, we can use GCD to calculate LCM
        return (2 * n) // gcd(2, n)
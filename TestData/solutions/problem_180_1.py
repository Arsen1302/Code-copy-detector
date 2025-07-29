class Solution:
    def solution_180_1(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10

        res = 91
        mult = 8
        comb = 81
        for i in range(n - 2):
            comb *=  mult
            mult -= 1
            res += comb

        return res
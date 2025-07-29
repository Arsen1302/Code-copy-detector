class Solution:
    def solution_1660_5(self, start: int, end: int, k: int) -> int:
        d = abs(start - end)
        if (k + d) % 2:
            return 0
        r = (k + d) // 2
        return math.comb(k, r) % (10**9 + 7)
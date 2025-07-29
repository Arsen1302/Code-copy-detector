class Solution:
    def solution_118_2(self, n: int) -> int:
        res, cur = 0, 1
        while cur <= n:
            res += n // (cur * 10) * cur + min(max(n % (cur * 10) - cur + 1, 0), cur)
            cur *= 10
        return res
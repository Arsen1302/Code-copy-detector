class Solution:
    def solution_85_1(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&amp;1)
            n>>=1
        return res
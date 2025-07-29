class Solution:
    def solution_85_3(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res<<1) + (n&amp;1)
            n>>=1
        return res
class Solution:
    def solution_1543_3(self, t: int, m: int, n: int) -> int:
        a = t // m
        res = 0 
        for x in range(0, a + 1):
            res += 1 + (t-m*x)//n

        return res
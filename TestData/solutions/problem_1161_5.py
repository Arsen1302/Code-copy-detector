class Solution:
    def solution_1161_5(self, n: int) -> int:
        q, r = divmod(n, 7)
        return ((7*q + (49+2*r))*q + r*(r+1))//2
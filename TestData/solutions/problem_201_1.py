class Solution:
    def solution_201_1(self, n: int) -> int:
        if n == 1: return 1
        if n&amp;1: n -= 1
        return n + 2 - 2*self.solution_201_1(n//2)
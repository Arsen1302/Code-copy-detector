class Solution:
    def solution_1042_1(self, n: int, k: int) -> str:
        if k == 1: return "0"
        if k == 2**(n-1): return "1"
        if k < 2**(n-1): return self.solution_1042_1(n-1, k)
        return "0" if self.solution_1042_1(n-1, 2**n-k) == "1" else "1"
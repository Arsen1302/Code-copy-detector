class Solution:
    def solution_630_1(self, A: List[int]) -> str:
        hh = mm = -1
        for x in set(permutations(A, 4)): 
            h = 10*x[0] + x[1]
            m = 10*x[2] + x[3]
            if h < 24 and m < 60 and 60*h + m > 60*hh + mm: hh, mm = h, m
        return f"{hh:02}:{mm:02}" if hh >= 0 else ""
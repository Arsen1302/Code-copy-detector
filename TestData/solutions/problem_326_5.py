class Solution:
    def solution_326_5(self, n: int) -> int:
        f0, f1, f2 = 1, 1, 0
        g0, g1, g2 = 1, 0, 0 
        for _ in range(n-1): 
            f0, f1, f2, g0, g1, g2 = (f0+f1+f2) % 1_000_000_007, f0, f1, (f0+f1+f2+g0+g1+g2) % 1_000_000_007, g0, g1
        return (f0+f1+f2+g0+g1+g2) % 1_000_000_007
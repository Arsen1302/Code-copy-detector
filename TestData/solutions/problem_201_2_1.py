class Solution:
    def solution_201_2_1(self, n: int) -> int:
        
        def solution_201_2_2(n): 
            """Return the final number of a list of length n."""
            if n == 1: return 1
            if n&amp;1: n -= 1
            return n + 2*(1 - solution_201_2_2(n//2))
        
        return solution_201_2_2(n)
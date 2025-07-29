class Solution:
    def solution_363_3_1(self, n: int, k: int) -> int:
        
        @cache
        def solution_363_3_2(n, k):
            """Return number of ways for n numbers with k inverse pairs."""
            if k == 0: return 1 
            if n <= 0 or k < 0: return 0 
            return solution_363_3_2(n-1, k) + solution_363_3_2(n, k-1) - solution_363_3_2(n-1, k-n)
        
        return solution_363_3_2(n, k) % 1_000_000_007
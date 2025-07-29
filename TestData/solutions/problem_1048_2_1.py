class Solution:
    def solution_1048_2_1(self, n: int) -> int:
        
        @lru_cache(None)
        def solution_1048_2_2(n):
            if n <= 1: return n
            return 1 + min(n%2 + solution_1048_2_2(n//2), n%3 + solution_1048_2_2(n//3))
        
        return solution_1048_2_2(n)
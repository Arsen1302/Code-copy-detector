class Solution:
    def solution_1284_2_1(self, n: int) -> int:
        
        @cache
        def solution_1284_2_2(n, k): 
            """Return min moves for n floors and k eggs."""
            if k == 1: return n 
            if n == 0: return 0 
            ans = inf 
            for x in range(1, n+1): 
                ans = min(ans, 1 + max(solution_1284_2_2(x-1, k-1), solution_1284_2_2(n-x, k)))
            return ans 
        
        return solution_1284_2_2(n, 2)
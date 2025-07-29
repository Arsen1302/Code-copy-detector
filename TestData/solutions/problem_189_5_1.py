class Solution:
    def solution_189_5_1(self, n: int) -> int:
        
        @lru_cache(None)
        def solution_189_5_2(lo, hi): 
            """The cost of guessing a number where lo <= x <= hi."""
            if lo >= hi: return 0 # no need to guess 
            ans = inf
            for mid in range(lo, hi+1): 
                ans = min(ans, mid + max(solution_189_5_2(lo, mid-1), solution_189_5_2(mid+1, hi)))
            return ans 
        
        return solution_189_5_2(1, n)
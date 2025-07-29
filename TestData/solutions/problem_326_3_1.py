class Solution:
    def solution_326_3_1(self, n: int) -> int:
        
        @lru_cache(100)
        def solution_326_3_2(i, absent, late): 
            """Return number of attendance eligible for award."""
            if i == n: return 1
            ans = solution_326_3_2(i+1, absent, 0) # present 
            if absent == 0: ans += solution_326_3_2(i+1, 1, 0) # absent 
            if late < 2: ans += solution_326_3_2(i+1, absent, late+1) # late 
            return ans % 1_000_000_007
        
        return solution_326_3_2(0, 0, 0)
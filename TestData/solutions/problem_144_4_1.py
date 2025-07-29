class Solution:
    def solution_144_4_1(self, n: int) -> bool:
        
        @lru_cache(None)
        def solution_144_4_2(k):
            """Return True if there is a winning strategy with k stones left."""
            if k <= 3: return True 
            for kk in range(1, 4):
                if not solution_144_4_2(k - kk): return True #opponent cannot win 
            return False 
        
        return solution_144_4_2(n)
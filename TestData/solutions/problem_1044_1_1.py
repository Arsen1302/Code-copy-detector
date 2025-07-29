class Solution:
    def solution_1044_1_1(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def solution_1044_1_2(lo, hi): 
            """Return cost of cutting [lo, hi]."""
            cc = [c for c in cuts if lo < c < hi] #collect cuts within this region 
            if not cc: return 0
            ans = inf
            for mid in cc: ans = min(ans, solution_1044_1_2(lo, mid) + solution_1044_1_2(mid, hi))
            return ans + hi - lo
        
        return solution_1044_1_2(0, n)
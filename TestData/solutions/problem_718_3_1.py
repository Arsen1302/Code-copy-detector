class Solution:
    def solution_718_3_1(self, values: List[int]) -> int:
        
        @cache
        def solution_718_3_2(lo, hi): 
            """Return minimum score triangulation of values[lo:hi]."""
            if lo+3 > hi: return 0 
            ans = inf
            for mid in range(lo+1, hi-1): 
                ans = min(ans, values[lo]*values[mid]*values[hi-1] + solution_718_3_2(lo, mid+1) + solution_718_3_2(mid, hi))
            return ans 
        
        return solution_718_3_2(0, len(values))
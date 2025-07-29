class Solution:
    def solution_327_3_1(self, nums: List[int]) -> str:
        
        @cache
        def solution_327_3_2(lo, hi): 
            """Return max division of nums[lo:hi]."""
            if lo + 1 == hi: return str(nums[lo])
            ans = "-inf" 
            for mid in range(lo+1, hi): 
                cand = solution_327_3_2(lo, mid) + "/"
                if mid + 1 < hi: cand += "(" + solution_327_3_3(mid, hi) + ")"
                else: cand += solution_327_3_3(mid, hi)
                ans = max(ans, cand, key=eval)
            return ans 
        
        @cache
        def solution_327_3_3(lo, hi): 
            """Return min division of nums[lo:hi]."""
            if lo + 1 == hi: return str(nums[lo])
            ans = "inf"
            for mid in range(lo+1, hi):
                cand = solution_327_3_3(lo, mid) + "/"
                if mid + 1 < hi: cand += "(" + solution_327_3_2(mid, hi) + ")"
                else: cand += solution_327_3_2(mid, hi)
                ans = min(ans, cand, key=eval)
            return ans 
        
        return solution_327_3_2(0, len(nums))
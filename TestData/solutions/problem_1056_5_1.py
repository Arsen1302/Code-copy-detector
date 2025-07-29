class Solution:
    def solution_1056_5_1(self, stoneValue: List[int]) -> int:
        # prefix sum 
        prefix = [0]
        for x in stoneValue: prefix.append(prefix[-1] + x)
        
        @lru_cache(None)
        def solution_1056_5_2(lo, hi):
            """Return the score of arranging values from lo (inclusive) to hi (exclusive). """
            if lo+1 == hi: return 0 
            val = 0
            for mid in range(lo+1, hi): 
                lower = prefix[mid] - prefix[lo]
                upper = prefix[hi] - prefix[mid]
                if lower < upper: val = max(val, lower + solution_1056_5_2(lo, mid))
                elif lower > upper: val = max(val, upper + solution_1056_5_2(mid, hi))
                else: val = max(val, lower + max(solution_1056_5_2(lo, mid), solution_1056_5_2(mid, hi)))
            return val 
                
        return solution_1056_5_2(0, len(stoneValue))
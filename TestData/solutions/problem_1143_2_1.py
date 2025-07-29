class Solution:
    def solution_1143_2_1(self, stones: List[int]) -> int:
        prefix = [0]
        for x in stones: prefix.append(prefix[-1] + x)
        
        @lru_cache(1000)
        def solution_1143_2_2(lo, hi): 
            """Return difference of scores."""
            if lo == hi: return 0
            return max(prefix[hi] - prefix[lo+1] - solution_1143_2_2(lo+1, hi), prefix[hi-1] - prefix[lo] - solution_1143_2_2(lo, hi-1))
            
        return solution_1143_2_2(0, len(stones))
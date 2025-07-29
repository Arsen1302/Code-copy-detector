class Solution:
    def solution_1368_2_1(self, s: str) -> int:
        
        @cache
        def solution_1368_2_2(mask): 
            """Return length of longest palindromic sequence."""
            if not mask: return 0
            if not mask &amp; (mask-1): return 1
            lo = int(log2(mask &amp; ~(mask-1))) # least significant set bit
            hi = int(log2(mask)) # most significant set bit 
            if s[lo] == s[hi]: return 2 + solution_1368_2_2(mask^(1<<lo)^(1<<hi))
            return max(solution_1368_2_2(mask^(1<<lo)), solution_1368_2_2(mask^(1<<hi)))
        
        ans = 0
        for mask in range(1 << len(s)): 
            comp = (1 << len(s)) - 1 ^ mask
            ans = max(ans, solution_1368_2_2(mask) * solution_1368_2_2(comp))
        return ans
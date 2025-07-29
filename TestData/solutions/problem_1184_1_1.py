class Solution:
    def solution_1184_1_1(self, s: str) -> bool:
        mp = {}
        for i in range(2*len(s)-1): 
            lo, hi = i//2, (i+1)//2
            while 0 <= lo <= hi < len(s) and s[lo] == s[hi]: 
                mp.setdefault(lo, set()).add(hi)
                lo -= 1
                hi += 1
        
        @lru_cache(None)
        def solution_1184_1_2(i, k): 
            """Return True if s[i:] can be split into k palindromic substrings."""
            if k < 0: return False 
            if i == len(s): return k == 0
            return any(solution_1184_1_2(ii+1, k-1) for ii in mp[i])
        
        return solution_1184_1_2(0, 3)
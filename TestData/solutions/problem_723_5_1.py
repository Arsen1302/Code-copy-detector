class Solution:
    def solution_723_5_1(self, s: str) -> str:
        mod = 1_000_000_007
        
        def solution_723_5_2(k): 
            """Return duplicated substring of length k."""
            p = pow(26, k, mod)
            hs = 0
            seen = {}
            for i, ch in enumerate(s): 
                hs = (26*hs + ord(ch) - 97) % mod
                if i >= k: hs = (hs - (ord(s[i-k])-97)*p) % mod # rolling hash 
                if i+1 >= k:
                    if hs in seen and s[i+1-k:i+1] in seen[hs]: return s[i+1-k:i+1] # resolve hash collision
                    seen.setdefault(hs, set()).add(s[i+1-k:i+1])
            return ""
        
        lo, hi = 0, len(s)-1
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if solution_723_5_2(mid): lo = mid
            else: hi = mid - 1
        return solution_723_5_2(lo)
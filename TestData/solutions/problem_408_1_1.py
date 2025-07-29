class Solution:
    def solution_408_1_1(self, stickers: List[str], target: str) -> int:
        freqs = [Counter(x) for x in stickers]
        
        @cache
        def solution_408_1_2(x):
            """Return min sticks to give x."""
            if not x: return 0 
            ans = inf
            freq = Counter(x)
            for cnt in freqs: 
                if x[0] in cnt: 
                    xx = "".join(k*v for k, v in (freq - cnt).items())
                    ans = min(ans, 1 + solution_408_1_2(xx))
            return ans 
        
        ans = solution_408_1_2(target)
        return ans if ans < inf else -1
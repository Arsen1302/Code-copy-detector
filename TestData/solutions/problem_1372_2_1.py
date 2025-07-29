class Solution:
    def solution_1372_2_1(self, n: int, rides: List[List[int]]) -> int:
        mp = {}
        for start, end, tip in rides: 
            mp.setdefault(start, []).append((end, tip))
        
        @cache
        def solution_1372_2_2(x): 
            """Return max earning at x."""
            if x == n: return 0 
            ans = solution_1372_2_2(x+1)
            for xx, tip in mp.get(x, []): 
                ans = max(ans, xx - x + tip + solution_1372_2_2(xx))
            return ans 
        
        return solution_1372_2_2(1)
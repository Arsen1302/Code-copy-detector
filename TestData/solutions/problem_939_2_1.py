class Solution:
    def solution_939_2_1(self, stoneValue: List[int]) -> str:
        
        @cache
        def solution_939_2_2(i): 
            """Return max value obtained from stoneValue[i:]."""
            if i >= len(stoneValue): return 0 
            ans = -inf
            for ii in range(i, i+3): 
                ans = max(ans, sum(stoneValue[i:ii+1]) - solution_939_2_2(ii+1))
            return ans 
        
        ans = solution_939_2_2(0)
        if ans > 0: return "Alice"
        if ans == 0: return "Tie"
        return "Bob"
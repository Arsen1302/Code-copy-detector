class Solution:
    def solution_1590_1(self, brackets: List[List[int]], income: int) -> float:
        ans = prev = 0 
        for hi, pct in brackets: 
            hi = min(hi, income)
            ans += (hi - prev)*pct/100
            prev = hi 
        return ans
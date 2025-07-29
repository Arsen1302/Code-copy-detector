class Solution:
    def solution_1206_1_1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        toppingCosts *= 2
        
        @cache
        def solution_1206_1_2(i, x):
            """Return sum of subsequence of toppingCosts[i:] closest to x."""
            if x < 0 or i == len(toppingCosts): return 0
            return min(solution_1206_1_2(i+1, x), toppingCosts[i] + solution_1206_1_2(i+1, x-toppingCosts[i]), key=lambda y: (abs(y-x), y))
        
        ans = inf
        for bc in baseCosts: 
            ans = min(ans, bc + solution_1206_1_2(0, target - bc), key=lambda x: (abs(x-target), x))
        return ans
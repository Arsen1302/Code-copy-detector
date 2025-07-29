class Solution:
    def solution_1206_2_1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        @cache
        def solution_1206_2_2(i, cost):
            """Return sum of subsequence closest to target."""
            if cost >= target or i == len(toppingCosts): return cost
            return min(solution_1206_2_2(i+1, cost), solution_1206_2_2(i+1, cost+toppingCosts[i]), key=lambda x: (abs(x-target), x))
        
        ans = inf
        toppingCosts *= 2
        for cost in baseCosts: 
            ans = min(ans, solution_1206_2_2(0, cost), key=lambda x: (abs(x-target), x))
        return ans
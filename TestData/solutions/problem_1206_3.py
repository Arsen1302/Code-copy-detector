class Solution:
    def solution_1206_3(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        top = {0}
        for x in toppingCosts*2: 
            top |= {x + xx for xx in top}
        top = sorted(top)
        
        ans = inf 
        for bc in baseCosts: 
            k = bisect_left(top, target - bc)
            if k < len(top): ans = min(ans, bc + top[k], key=lambda x: (abs(x-target), x))
            if k: ans = min(ans, bc + top[k-1], key=lambda x: (abs(x-target), x))
        return ans
class Solution:
    def solution_663_5_1(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def solution_663_5_2(i):
            """Return minimum cost of traveling on days[i:]"""
            if i == len(days): return 0 # boundary condition (no more travel)
            ans = inf
            for cost, d in zip(costs, (1, 7, 30)): 
                ii = bisect_left(days, days[i]+d)
                ans = min(ans, cost + solution_663_5_2(ii))
            return ans 
        
        return solution_663_5_2(0)
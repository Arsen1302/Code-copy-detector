class Solution:
    def solution_663_4_1(self, days: List[int], costs: List[int]) -> int:
                
        days = set(days)        
        graph = {0 : 1, 1 : 7, 2: 30}
        
        @functools.lru_cache(None)
        def solution_663_4_2(day, end):
            
            if day > end:
                return 0
            
            if day not in days:
                return solution_663_4_2(day+1, end)
            
            return min([
                c + solution_663_4_2(day+graph[i], end)
                for i,c in enumerate(costs)   
            ])
        
        return solution_663_4_2(1, max(days))
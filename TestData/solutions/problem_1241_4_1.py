class Solution:
    def solution_1241_4_1(self, obstacles: List[int]) -> int:
                                
        @functools.lru_cache(None)
        def solution_1241_4_2(idx, lane):                    
            if idx >= len(obstacles): return 0            
            if obstacles[idx] == lane: return float('inf')            
            return min([
                (1 if l != lane else 0) + solution_1241_4_2(idx+1, l)
                for l in range(1, 4)
                if l != obstacles[idx]
            ])
        
        return solution_1241_4_2(0, 2)
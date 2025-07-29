class Solution:
    def solution_727_1_1(self, stones: List[int]) -> int:
        
        @lru_cache(None)
        def solution_727_1_2(i, v): 
            """Return minimum weight of stones[i:] given existing weight."""
            if i == len(stones): return abs(v)
            return min(solution_727_1_2(i+1, v - stones[i]), solution_727_1_2(i+1, v + stones[i]))
        
        return solution_727_1_2(0, 0)
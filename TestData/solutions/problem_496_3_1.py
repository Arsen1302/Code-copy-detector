class Solution:
    def solution_496_3_1(self, N: int) -> float:
        if N > 5000: return 1
        
        @lru_cache(None)
        def solution_496_3_2(x, y): 
            """Return """
            if x <= 0 and y <= 0: return 0.5
            if x <= 0 or y <= 0: return x <= 0
            return 0.25*(solution_496_3_2(x-100, y) + solution_496_3_2(x-75, y-25) + solution_496_3_2(x-50, y-50) + solution_496_3_2(x-25, y-75))
        
        return solution_496_3_2(N, N)
class Solution:
    def solution_496_5_1(self, n: int) -> float:
        if n >= 4276: return 1.0

        @lru_cache(None)
        def solution_496_5_2(a: int, b: int)->float:
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            return (solution_496_5_2(a-100,b) + solution_496_5_2(a-75,b-25) + solution_496_5_2(a-50,b-50) + solution_496_5_2(a-25,b-75))*.25
        
        return solution_496_5_2(n,n)
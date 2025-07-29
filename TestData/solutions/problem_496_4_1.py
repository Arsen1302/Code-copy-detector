class Solution:
    def solution_496_4_1(self, n):
        @lru_cache(None)
        def solution_496_4_2(a,b):
            if a<=0 and b<=0: return 0.5
            if a<=0: return 1
            if b<=0: return 0

            return 0.25*(solution_496_4_2(a-100,b) + solution_496_4_2(a-75,b-25) + solution_496_4_2(a-50,b-50) + solution_496_4_2(a-25,b-75))

        return solution_496_4_2(n,n) if n < 4840 else 1
class Solution:
    def solution_33_3_1(self, a: List[List[int]]) -> int:
        @cache
        def solution_33_3_2(level, i):            
            return 0 if level >= len(a) else a[level][i] + min(solution_33_3_2(level + 1, i), solution_33_3_2(level + 1, i+1))        
        return solution_33_3_2(0, 0)
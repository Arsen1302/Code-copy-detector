class Solution:
    def solution_935_2_1(self, satisfaction: List[int]) -> int:
        satisfaction.sort() # ascending order 
        
        @cache
        def solution_935_2_2(i, k): 
            """Return max sum of like-time coefficient of satisfation[i:]."""
            if i == len(satisfaction): return 0 
            return max(satisfaction[i]*k + solution_935_2_2(i+1, k+1), solution_935_2_2(i+1, k))
        
        return solution_935_2_2(0, 1)
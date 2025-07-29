class Solution:
    def solution_924_1_1(self, slices: List[int]) -> int:
        
        @cache
        def solution_924_1_2(i, k, first): 
            """Return max sum of k pieces from slices[i:]."""
            if k == 0: return 0 
            if i >= len(slices) or first and i == len(slices)-1: return -inf 
            if i == 0: return max(solution_924_1_2(i+1, k, False), slices[i] + solution_924_1_2(i+2, k-1, True))
            return max(solution_924_1_2(i+1, k, first), slices[i] + solution_924_1_2(i+2, k-1, first))
        
        return solution_924_1_2(0, len(slices)//3, None)
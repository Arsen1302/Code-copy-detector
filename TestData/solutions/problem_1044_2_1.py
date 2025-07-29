class Solution:
    def solution_1044_2_1(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        
        @lru_cache(None)
        def solution_1044_2_2(i, j): 
            """Return cost of cutting from cuts[i] to cuts[j]."""
            if i+1 == j: return 0 #no cut in (i, j)
            return cuts[j] - cuts[i] + min(solution_1044_2_2(i, k) + solution_1044_2_2(k, j) for k in range(i+1, j))
        
        return solution_1044_2_2(0, len(cuts)-1)
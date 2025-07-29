class Solution:
    def solution_422_2_1(self, s1: str, s2: str) -> int:
        
        @lru_cache(None)
        def solution_422_2_2(i, j): 
            """Return minimum ASCII delete sum for s1[i:] and s2[j:]."""
            if i == len(s1): return sum(ord(s2[jj]) for jj in range(j, len(s2)))
            if j == len(s2): return sum(ord(s1[ii]) for ii in range(i, len(s1)))
            if s1[i] == s2[j]: return solution_422_2_2(i+1, j+1)
            return min(ord(s1[i]) + solution_422_2_2(i+1, j), ord(s2[j]) + solution_422_2_2(i, j+1))
        
        return solution_422_2_2(0, 0)
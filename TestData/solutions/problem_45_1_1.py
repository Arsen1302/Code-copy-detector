class Solution:
    def solution_45_1_1(self, s: str) -> int:
        #pre-processing
        palin = dict()
        for k in range(len(s)):
            for i, j in (k, k), (k, k+1):
                while 0 <= i and j < len(s) and s[i] == s[j]: 
                    palin.setdefault(i, []).append(j)
                    i, j = i-1, j+1
                
        #dp 
        @lru_cache(None)
        def solution_45_1_2(i):
            """Return minimum palindrome partitioning of s[i:]"""
            if i == len(s): return 0
            return min(1 + solution_45_1_2(ii+1) for ii in palin[i])
        
        return solution_45_1_2(0)-1
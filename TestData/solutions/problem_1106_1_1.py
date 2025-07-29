class Solution:
    def solution_1106_1_1(self, s: str, t: str) -> int:
        m, n = len(s), len(t) 
        
        @cache
        def solution_1106_1_2(i, j, k): 
            """Return number of substrings ending at s[i] and t[j] with k=0/1 difference."""
            if i < 0 or j < 0: return 0 
            if s[i] == t[j]: return solution_1106_1_2(i-1, j-1, k) + (k==0)
            else: return 0 if k == 0 else 1 + solution_1106_1_2(i-1, j-1, 0)
        
        return sum(solution_1106_1_2(i, j, 1) for i in range(m) for j in range(n))
class Solution:
    def solution_10_5_1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @lru_cache(None)
        def solution_10_5_2(i, j):
            if j == n:
                return i == m
            
            match = i != m and (p[j] == '.' or s[i] == p[j])
            if j == n - 1 or p[j + 1] != '*':
                return match and solution_10_5_2(i + 1, j + 1)
            
            return solution_10_5_2(i, j + 2) or (match and solution_10_5_2(i + 1, j))
        
        return solution_10_5_2(0, 0)
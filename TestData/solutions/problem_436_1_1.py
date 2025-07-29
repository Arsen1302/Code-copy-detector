class Solution:
    def solution_436_1_1(self, s:str) -> int:
        
        @cache
        def solution_436_1_2(ch, i, j):
            if i > j:
                return 0
            
            if i == j and s[i] == ch:
                return 1
            
            if s[i] == s[j] == ch:
                return 2 + solution_436_1_2('a', i+1, j-1) + solution_436_1_2('b', i+1, j-1) + solution_436_1_2('c', i+1, j-1) + solution_436_1_2('d', i+1, j-1)
            elif s[i] != ch:
                return solution_436_1_2(ch, i+1, j)
            elif s[j] != ch:
                return solution_436_1_2(ch, i, j-1)
        
        
        n = len(s)
        return (solution_436_1_2('a', 0, n-1) + solution_436_1_2('b', 0, n-1) + solution_436_1_2('c', 0, n-1) + solution_436_1_2('d', 0, n-1)) % (10**9+7)
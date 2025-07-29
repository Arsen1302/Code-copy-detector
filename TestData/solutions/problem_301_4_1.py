class Solution:
    def solution_301_4_1(self, s: str) -> int:
        
        def solution_301_4_2(l= 0, r= len(s)-1):
            if l > r:
                return 0
            elif l == r:
                return 1
            if (l, r) in cache:
                return cache[(l, r)]
            if s[l] == s[r]:
                cache[(l, r)] = 2 + solution_301_4_2(l+1, r-1)
            else: 
                cache[(l, r)] = max(solution_301_4_2(l+1, r), solution_301_4_2(l, r-1))
            return cache[(l, r)]
        
        cache = {}
        return solution_301_4_2()
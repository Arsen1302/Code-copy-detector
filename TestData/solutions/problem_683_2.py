class Solution:
    def solution_683_2(self, s: str) -> bool:
        incomplete = True
        
        while incomplete:
            if 'abc' in s:
                s= s.replace('abc','')
            else:
                incomplete = False
        
        return s == ''
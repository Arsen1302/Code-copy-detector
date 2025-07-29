class Solution:
    def solution_683_5(self, s: str) -> bool:
        while len(s) > 0 : 
            if 'abc' in s : 
                s = s.replace('abc', '')
            else : 
                return False
        return True
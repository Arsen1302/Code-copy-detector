class Solution:
    def solution_143_4(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        ma = {}
        rev = {}
        if len(s) != len(pattern) :
            return False
        for i in range(len(pattern)) :
            if pattern[i] in ma :
                if ma[pattern[i]]!=s[i] :
                    return False
            elif s[i] in rev :
                return False
            else :
                ma[pattern[i]] = s[i]
                rev[s[i]] = pattern[i]
                
        return True
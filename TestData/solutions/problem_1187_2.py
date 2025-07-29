class Solution:
    def solution_1187_2(self, s: str) -> int:
        while len(s) >= 2 and s[0] == s[-1]: 
            s = s.strip(s[0])
        return len(s)
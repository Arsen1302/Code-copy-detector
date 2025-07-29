class Solution:
    def solution_516_2_1(self, s: str) -> int:
        def solution_516_2_2(sub, t):
            num=0
            for c in sub:
                if c==t:
                    num+=1
            return num==1
            
        r=0
        for c in string.ascii_uppercase:
            for i in range(len(s)):
                for j in range(i, len(s)):
                    if solution_516_2_2(s[i:j+1], c):
                        r+=1
        return r
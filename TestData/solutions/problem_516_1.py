class Solution:
    def solution_516_1(self, s: str) -> int:
        r=0
        for i in range(len(s)):
            for j in range(i, len(s)):
                ss=s[i:j+1]
                unique=sum([ 1 for (i,v) in Counter(ss).items() if v == 1 ])
                r+=unique
        return r
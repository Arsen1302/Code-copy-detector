class Solution:
    def solution_1153_5(self, s: str) -> bool:
        n=len(s)
        s=s.lower()
        a,b=s[:n//2],s[n//2:]
        vol="aeiou"
        c1,c2=0,0
        for i in a:
            if i in vol:
                c1+=1
        for i in b:
            if i in vol:
                c2+=1
        return c1==c2
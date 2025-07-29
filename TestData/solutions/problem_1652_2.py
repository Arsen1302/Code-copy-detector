class Solution:
    def solution_1652_2(self, s: str) -> str:
        c,n=0,len(s)
        t=""
        for i in range(n-1,-1,-1):
            if s[i]=='*':
                c+=1
            else:
                if c==0:
                    t+=s[i]
                else:
                    c-=1
        return t[-1::-1]
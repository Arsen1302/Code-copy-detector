class Solution:
    def solution_1090_4(self, s: str) -> int:
        m,c,n=0,0,len(s)
        for i in range(n):
            if s[i]=='(':
                c+=1
                m=max(c,m)
            elif s[i]==')': c-=1
        return m
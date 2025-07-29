class Solution:
    def solution_175_4(self, s: str) -> str:
        l="aeiouAEIOU"
        s=list(s)
        i,j=0,len(s)-1
        while(i<j):
            if s[i] in l and s[j] in l:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in l:
                i+=1
            elif s[j] not in l:
                j-=1
        return ''.join(s)
class Solution:
    def solution_1065_2(self, s: str) -> str:
        if len(s)==1:  #if input contains only a '?'
            if s[0]=='?':
                return 'a'
        s=list(s)
        for i in range(len(s)):
            if s[i]=='?':
                for c in 'abc':
                    if i==0 and s[i+1]!=c: #if i=0 means it is first letter so there is no s[ i-1]
                        s[i]=c
                        break
                    if i==len(s)-1 and s[i-1]!=c: #if i=len(s) means it is last letter so there is no s[i+1]
                        s[i]=c
                        break
                    if (i>0 and i<len(s)-1) and s[i-1]!=c and s[i+1]!=c: 
                        s[i]=c
                        break
        return ''.join(s)
	```
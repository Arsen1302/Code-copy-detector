class Solution:
    def solution_701_4(self, s: str) -> str:
        a,n=[],len(s)
        i=j=0
        t=''
        while i<n:
            print(s[i],"s[i]")
            if a and a[-1]=='(' and s[i]==')':
                a.pop()
            elif len(a)==0 and s[i]=='(' and i>0:
                t+=s[j+1:i-1]
                j=i
                a.append(s[i])
            else:
                a.append(s[i])
            i+=1
        t+=s[j+1:i-1]
        return t
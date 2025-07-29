class Solution:
    def solution_623_4(self, s: str) -> List[int]:
        l=len(s)
        x=0
        f=[]
        for i in range(len(s)):
            if(s[i]=='I'):
                f.append(x)
                x+=1
            else:
                f.append(l)
                l-=1
        f.append(x)
        return f
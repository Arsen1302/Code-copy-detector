class Solution:
    def solution_725_2(self, s: str) -> str:
        ans=[]
        for a in s:
            if(len(ans)>0 and ans[-1]==a):
                ans.pop()
            else:
                ans.append(a)
        return("".join(ans))
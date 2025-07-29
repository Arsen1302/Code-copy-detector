class Solution:
    def solution_701_2(self, S: str) -> str:
        ans=[];o=0
        for i in S:
            if i=='(' and o>0:
                ans.append(i)
            if i==')' and o>1:
                ans.append(')')
            o+=1 if i=='(' else -1
        return ''.join(ans)
class Solution:
    def solution_1531_3(self, s: str) -> int:
        x0,x1,x01,x10,ans = 0,0,0,0,0
        for i in s:
            if i=="1": x1+=1;x01+=x0;ans+=x10
            else: x0+=1;x10+=x1;ans+=x01
        return ans
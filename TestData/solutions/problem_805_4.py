class Solution:
    def solution_805_4(self, s: str) -> int:
        ans =0 
        count = 0
        for i in s:
            if i=='R':
                count+=1
            else:
                count-=1
            if count==0:
                ans +=1
                
        return ans
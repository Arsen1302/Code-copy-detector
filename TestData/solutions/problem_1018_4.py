class Solution:
    def solution_1018_4(self, s: str) -> int:
        
        res=0
        one_rt = 0
        
        for c in s:
            if c == '0':
                one_rt=0
            else:
                one_rt+=1
                res+=one_rt
                
        return res % 1000000007
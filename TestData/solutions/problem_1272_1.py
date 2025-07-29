class Solution:
    def solution_1272_1(self, s: str) -> bool:
        zero_in=temp=0
        for i in s:
            if i=="0":
                temp+=1
                if temp>zero_in:
                    zero_in=temp
            else:
                temp=0
        # Longest contiguous 0 in s is zero_in    
        return "1"*(zero_in+1) in s #return boolean value
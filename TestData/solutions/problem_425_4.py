class Solution:
    def solution_425_4(self, bits: List[int]) -> bool:
        idx =0
        flag = True
        while(idx<len(bits)):
            if(bits[idx]==0):
                idx+=1
                flag =True
            else:
                idx+=2
                flag = False
        return flag
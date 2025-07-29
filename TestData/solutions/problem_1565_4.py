class Solution:
    def solution_1565_4(self, num: int, k: int) -> int:
        count = 0
        i = 0 
        while i< len(str(num))-k+1:
            subs = int(str(num)[i:i+k])
            if subs!=0:
                if num%subs==0:
                    count+=1              
            i+=1
        return count
class Solution:
    def solution_1287_5(self, s: str) -> int:
        ret = len(s)
        onesOdd = 0 
        onesEven = 0
        for i, digit in enumerate(s):
            if i % 2 == 0 and digit == "1":
                onesEven += 1
            elif i % 2 == 1 and digit == "1":
                onesOdd += 1
                    
        total = onesEven + onesOdd
        for i in range(len(s)):
           
            #target: 010101...
            flips = onesEven + (len(s)//2 - onesOdd)
            ret = min(ret, flips)
            
            #target: 101010...
            flips = (len(s)-len(s)//2 - onesEven) + onesOdd
            ret = min(ret, flips)
            
            if len(s) % 2 == 0:
                break  
            else:
                onesEven = onesOdd + (1 if s[i] == "1" else 0)
                onesOdd = total - onesEven
        return ret
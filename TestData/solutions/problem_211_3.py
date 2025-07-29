class Solution:
    def solution_211_3(self, n: int) -> int:
       
        # integer digit, 1~9 integer digits is 1, 10~19 integer digits is 2
        d = 1
        
        # total digits at a integer level, base = 9*10**(d-1)*d
        base = 0
        
        while n > 9*10**(d-1)*d + base:
            
            base += 9*10**(d-1)*d
            d+=1
        
        # closest number for nth digits
        number = (10**(d-1) - 1) + (n-base)//d
        number = int(number)
        # remainder
        rmd = (n-base)%d
        
        if rmd == 0:
            return int(str(number)[-1])
        else:
            return int(str(number+1)[rmd-1])
class Solution:
    table = dict()
    def solution_888_5 (self, num: int) -> int:
        
        step = 0
        while num != 0 :
            
            step += 1
            
            if num &amp; 1 == 1:
                # odd number, subtract by 1
                num -= 1

            else:
                # even number, divide by 2 <=> right shift one bit
                num >>= 1
        
        return step
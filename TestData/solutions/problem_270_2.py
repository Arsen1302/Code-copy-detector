class Solution:
    def solution_270_2(self, num: int) -> int:
        res, n = 0, 0
        while num:
            if not num &amp; 1:
                res += 2**n
                
            num >>= 1
            n += 1
        
        return res
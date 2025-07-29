class Solution:
    def solution_9_1(self, x: int) -> bool:
        if x < 0:
            return False
        
        res = 0
        temp = x
        
        while temp:
            temp, n = divmod(temp, 10)
            res = (res * 10) + n
                
        return res == x
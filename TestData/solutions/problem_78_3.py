class Solution:
    def solution_78_3(self, n: int) -> int:
        if n<5:
            return 0
        x=0
        while n != 0:
            x += n // 5
            n //= 5
            
        return x
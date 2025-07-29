class Solution:
    def solution_1708_5_1(self, n: int, target: int) -> int:
        
        def solution_1708_5_2(x):
            
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
                
            return total
        
        res = 0
        base = 1
        
        while solution_1708_5_2(n + res) > target:
            base = base * 10
            res = base - (n % base)
            
        return res
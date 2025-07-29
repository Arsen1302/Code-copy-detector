class Solution:
    def solution_173_3(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1                # must break into 1 &amp; (n-1)
        
        num_3 = n // 3                  # break the number into (3+3+3+...) + remainder
        
        if n%3 == 0:                    
            return 3**num_3             # (3+3+3+...)
        if n%3 == 2:
            return (3**num_3) * 2       # (3+3+3+...) + 2     
        if n%3 == 1:
            return 3**(num_3-1) * 4     # (3+3+3+...) + 1 --> (3+3+...) + 3 + 1 -- > (3+3+...) + 4
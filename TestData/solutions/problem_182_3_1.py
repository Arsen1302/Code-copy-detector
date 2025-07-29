class Solution:
    def solution_182_3_1(self, x: int, y: int, z: int) -> bool:
        if not z: return True #edge case 
        
        def solution_182_3_2(x, y): 
            """Return greatest common divisor via Euclidean algo"""
            if x < y: x, y = y, x
            while y: x, y = y, x%y
            return x
        
        return z <= x + y and z % solution_182_3_2(x, y) == 0
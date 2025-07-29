class Solution:
    def solution_270_1(self, num: int) -> int:
        
        bit_mask = 2**num.bit_length() -1 
        
        return ( num ^ bit_mask )
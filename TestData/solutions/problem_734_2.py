class Solution(object):
    def solution_734_2(self, arr1, arr2):
        """
        to add two "-2" based numbers up
        we can simply do the calculation per bit
        and map out all the possible cases with carry
        
        in "-2" based numbers, because the values of bits
        alter between negative and positive, so the carry/borrow
        will be reversed to -1/1
        
        so when the sum on one bit >= 2, the carry can be -1 to 
        the higher bit
        and if the higher bit with carry sum to -1, it needs to 
        borrow from the even higher bit, resulting in a carry of 1
        
        # 12 possible cases in 5 categories in total
        # case (| case) -> bit sum -> (bit, carry)
        # 0,0,-1 -> -1 -> (1, 1)
        # 0,0,0 | 1,0,-1 | 0,1,-1 -> 0 -> (0, 0)
        # 0,0,1 | 1,0,0 | 0,1,0 | 1,1,-1 -> 1 -> (1, 0)
        # 1,1,0 | 1,0,1 | 0,1,1 -> 2 -> (0, -1)
        # 1,1,1 -> 3 -> (1, -1)
        
        the 2nd catogery can produce leading zeros
        """
        
        CASE_MAPS = {
            -1: (1, 1),
            0: (0, 0),
            1: (1, 0),
            2: (0, -1),
            3: (1, -1),
        }
        
        res, carry = [], 0
        
        while arr1 or arr2 or carry:
            bit = carry
            
            if arr1: bit += arr1.pop()
            if arr2: bit += arr2.pop()
            
            bit, carry = CASE_MAPS[bit]
            
            res += [bit]
            
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return res[::-1]
class Solution:
    def solution_50_5(self, nums: List[int]) -> int:

        single_num = 0
        
        # compute single number by bit masking
        for bit_shift in range(32):
            
            sum = 0
            
            for number in nums:
                
                # collect the bit sum
                sum += ( number >> bit_shift ) &amp; 1

            # Extract bit information of single number by modulo
            # Other number's bit sum is removed by mod 3 (i.e., all other numbers appear three times)
            single_num |= ( sum % 3 ) << bit_shift
            
            
        
        if ( single_num &amp; (1 << 31) ) == 0:
            return single_num
        else:
			# handle for negative number
            return -( (single_num^(0xFFFF_FFFF))+1 )
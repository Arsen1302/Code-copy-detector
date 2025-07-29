class Solution(object):
    def solution_86_4(self, n):
	
        mask_sum_2bit = 0x55555555
        mask_sum_4bit = 0x33333333
        mask_sum_8bit = 0x0F0F0F0F
        mask_sum_16bit = 0x00FF00FF
        mask_sum_32bit = 0x0000FFFF
        
        n = (n &amp; mask_sum_2bit) + ((n >> 1) &amp; mask_sum_2bit)
        n = (n &amp; mask_sum_4bit) + ((n >> 2) &amp; mask_sum_4bit)
        n = (n &amp; mask_sum_8bit) + ((n >> 4) &amp; mask_sum_8bit)
        n = (n &amp; mask_sum_16bit) + ((n >> 8) &amp; mask_sum_16bit)
        n = (n &amp; mask_sum_32bit) + ((n >> 16) &amp; mask_sum_32bit)
        
        return n
class Solution:
    def solution_410_5(self, n: int) -> bool:
	    # To check whether it has alternating bits i.e if alternating then all bits becomes 1.		
        n = n ^ (n >> 1)
		# To check if all bits are 1
        return True if (n+1) &amp; n == 0 else False
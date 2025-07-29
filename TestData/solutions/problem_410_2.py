class Solution:
	def solution_410_2(self, n: int) -> bool:
		while n > 1:
			bit1 = n &amp; 1
			n >>= 1
			bit2 = n &amp; 1
			if bit1 == bit2:
				return False
		return True
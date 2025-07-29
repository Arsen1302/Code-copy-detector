class Solution:
	def solution_78_4(self, n: int) -> int:
		count = 0

		while(n >= 5):
			n //= 5 # integer division, we don't need decimal numbers
			count += n

		return count
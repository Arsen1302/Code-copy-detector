class Solution:
	def solution_556_4(self, n: int) -> bool:

		num = sorted(str(n))

		for i in range(32):

			current_num = sorted(str(2**i))

			if num == current_num:
				return True

		return False
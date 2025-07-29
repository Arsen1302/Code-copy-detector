class Solution:
	def solution_900_5(self, n: int) -> int:

		result = 1

		modulo = 1000000007

		for i in range(1,n+1):
		
			result = result * i

			result = result % modulo

			result = result * (2*i - 1)

			result = result % modulo

		result = result % modulo

		return result
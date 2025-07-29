class Solution:
	def solution_1135_2(self, n: int) -> int:

		binary = ''

		for num in range(1, n+1):

			binary = binary + bin(num)[2:]

		result = int(binary, 2)

		return result % (10**9 + 7)
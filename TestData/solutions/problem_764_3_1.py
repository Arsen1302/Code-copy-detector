class Solution:

	def solution_764_3_1(self, n: int) -> int:
		lst = [-1 for i in range(n + 1)]

		def solution_764_3_2(n):
			if n == 0:
				return 0
			if n == 1:
				return 1
			if n == 2:
				return 1

			if lst[n] == -1:
				lst[n] = solution_764_3_2(n - 1) + solution_764_3_2(n - 2) + solution_764_3_2(n - 3)
			return lst[n]

		return solution_764_3_2(n)
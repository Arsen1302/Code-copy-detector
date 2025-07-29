class Solution:
	def solution_895_5_1(self, grid: List[List[int]]) -> int:

		def solution_895_5_2(array):

			low = 0
			high = len(array) - 1

			while low <= high:

				mid = (low + high ) // 2

				if array[mid] < 0:
					high = mid - 1

				elif array[mid] >= 0:
					low = mid + 1

			return low

		result = 0

		for row in grid:

			result = result + len(row) - solution_895_5_2(row)

		return result
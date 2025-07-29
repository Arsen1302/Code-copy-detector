class Solution:
	def solution_137_2(self, n: int) -> int:

		result = 1

		low = 1
		high = n

		while low <= high:

			mid = (low + high) //2

			if isBadVersion(mid) == False:
				low = mid + 1

			else:
				high = mid - 1

				result = mid

		return result
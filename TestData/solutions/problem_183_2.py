class Solution:
	def solution_183_2(self, num: int) -> bool:

		low  = 1
		high = num

		while low <= high:

			mid = ( low + high ) //2

			if mid * mid == num:
				return mid

			elif mid * mid < num:
				low = mid + 1

			elif mid * mid > num:
				high = mid - 1

		return False